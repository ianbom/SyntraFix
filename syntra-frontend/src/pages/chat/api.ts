import { authService } from "@/lib/auth"
import type { DocumentReference, Message } from "./types"

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000").replace(/\/$/, "")

interface ApiErrorPayload {
  detail?: unknown
  message?: unknown
}

interface ChatReferenceApiResponse {
  id: number
  document_id: number
  quote: string
  page_number: number | null
  document_title: string
}

interface ChatApiResponse {
  id: number
  conversation_id: number
  role: "user" | "bot"
  message: string
  created_at: string
  references: ChatReferenceApiResponse[]
}

interface ConversationApiResponse {
  id: number
  title: string
  is_pinned: boolean
  created_at: string
  updated_at: string
  chats: ChatApiResponse[]
}

interface PostChatRequestBody {
  message: string
  conversation_id?: number
}

interface PostChatParams {
  message: string
  conversationId?: number
  signal?: AbortSignal
}

interface PostChatStreamParams extends PostChatParams {
  onStart?: (conversationId: number) => void
  onChunk?: (chunk: string) => void
}

interface ListConversationsParams {
  limit?: number
  offset?: number
  signal?: AbortSignal
}

interface GetConversationParams {
  conversationId: number
  signal?: AbortSignal
}

interface GetDocumentDownloadUrlParams {
  documentUrl: string
  signal?: AbortSignal
}

interface DocumentDownloadApiResponse {
  download_url: unknown
  filename?: unknown
}

interface ChatStreamStartEvent {
  type: "start"
  conversation_id: number
}

interface ChatStreamChunkEvent {
  type: "chunk"
  content: string
}

interface ChatStreamDoneEvent {
  type: "done"
  chat: ChatApiResponse
}

interface ChatStreamErrorEvent {
  type: "error"
  message: string
}

type ChatStreamEvent =
  | ChatStreamStartEvent
  | ChatStreamChunkEvent
  | ChatStreamDoneEvent
  | ChatStreamErrorEvent

export interface ConversationSummary {
  id: number
  title: string
  updatedAt: string
}

export interface ConversationDetail {
  id: number
  title: string
  isPinned: boolean
  createdAt: string
  updatedAt: string
  chats: Message[]
}

export interface PostChatResult {
  id: number
  conversationId: number
  role: "user" | "assistant"
  message: string
  createdAt: string
  references: DocumentReference[]
}

export interface DocumentDownloadResult {
  downloadUrl: string
  filename: string
}

const toErrorMessage = (
  payload: ApiErrorPayload,
  fallbackMessage: string
): string => {
  if (typeof payload.message === "string" && payload.message.trim().length > 0) {
    return payload.message
  }

  if (typeof payload.detail === "string" && payload.detail.trim().length > 0) {
    return payload.detail
  }

  return fallbackMessage
}

const getErrorMessage = async (
  response: Response,
  fallbackMessage: string
): Promise<string> => {
  const contentType = response.headers.get("content-type") ?? ""

  if (contentType.includes("application/json")) {
    const payload = (await response.json()) as ApiErrorPayload
    return toErrorMessage(payload, fallbackMessage)
  }

  const text = await response.text()
  return text || fallbackMessage
}

const getAuthHeaders = (includeJsonContentType: boolean): HeadersInit => {
  const accessToken = authService.getAccessToken()
  if (!accessToken) {
    throw new Error("Sesi login tidak ditemukan. Silakan login ulang.")
  }

  if (includeJsonContentType) {
    return {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json",
    }
  }

  return {
    Authorization: `Bearer ${accessToken}`,
  }
}

const mapChatReference = (
  reference: ChatReferenceApiResponse
): DocumentReference => ({
  id: String(reference.id),
  title: reference.document_title,
  excerpt: reference.quote,
  pageNumber: reference.page_number ?? 1,
  documentUrl: `${API_BASE_URL}/documents/${reference.document_id}/download`,
})

const mapChatRoleToMessageRole = (
  role: ChatApiResponse["role"]
): Message["role"] => (role === "bot" ? "assistant" : "user")

const mapChatMessage = (chat: ChatApiResponse): Message => {
  const references = chat.references.map(mapChatReference)

  return {
    id: String(chat.id),
    content: chat.message,
    role: mapChatRoleToMessageRole(chat.role),
    timestamp: new Date(chat.created_at),
    references: references.length > 0 ? references : undefined,
  }
}

const mapConversationSummary = (
  conversation: ConversationApiResponse
): ConversationSummary => ({
  id: conversation.id,
  title: conversation.title,
  updatedAt: conversation.updated_at,
})

const mapConversationDetail = (
  conversation: ConversationApiResponse
): ConversationDetail => ({
  id: conversation.id,
  title: conversation.title,
  isPinned: conversation.is_pinned,
  createdAt: conversation.created_at,
  updatedAt: conversation.updated_at,
  chats: conversation.chats.map(mapChatMessage),
})

const mapPostChatResult = (chat: ChatApiResponse): PostChatResult => ({
  id: chat.id,
  conversationId: chat.conversation_id,
  role: mapChatRoleToMessageRole(chat.role),
  message: chat.message,
  createdAt: chat.created_at,
  references: chat.references.map(mapChatReference),
})

export const postChat = async ({
  message,
  conversationId,
  signal,
}: PostChatParams): Promise<PostChatResult> => {
  const requestBody: PostChatRequestBody = { message }
  if (typeof conversationId === "number") {
    requestBody.conversation_id = conversationId
  }

  const response = await fetch(`${API_BASE_URL}/chats/`, {
    method: "POST",
    headers: getAuthHeaders(true),
    body: JSON.stringify(requestBody),
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengirim pesan."))
  }

  const payload = (await response.json()) as ChatApiResponse
  return mapPostChatResult(payload)
}

const parseChatStreamEvent = (line: string): ChatStreamEvent => {
  const payload = JSON.parse(line) as { type?: unknown; [key: string]: unknown }

  if (payload.type === "start" && typeof payload.conversation_id === "number") {
    return {
      type: "start",
      conversation_id: payload.conversation_id,
    }
  }

  if (payload.type === "chunk" && typeof payload.content === "string") {
    return {
      type: "chunk",
      content: payload.content,
    }
  }

  if (payload.type === "done" && typeof payload.chat === "object" && payload.chat) {
    return {
      type: "done",
      chat: payload.chat as ChatApiResponse,
    }
  }

  if (payload.type === "error" && typeof payload.message === "string") {
    return {
      type: "error",
      message: payload.message,
    }
  }

  throw new Error("Format respons streaming tidak valid.")
}

export const postChatStream = async ({
  message,
  conversationId,
  signal,
  onStart,
  onChunk,
}: PostChatStreamParams): Promise<PostChatResult> => {
  const requestBody: PostChatRequestBody = { message }
  if (typeof conversationId === "number") {
    requestBody.conversation_id = conversationId
  }

  const response = await fetch(`${API_BASE_URL}/chats/stream`, {
    method: "POST",
    headers: getAuthHeaders(true),
    body: JSON.stringify(requestBody),
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengirim pesan."))
  }

  if (!response.body) {
    throw new Error("Respons streaming tidak tersedia.")
  }

  const reader = response.body.getReader()
  const decoder = new TextDecoder()
  let buffered = ""
  let finalResult: PostChatResult | null = null

  const handleLine = (line: string) => {
    if (!line) {
      return
    }

    const event = parseChatStreamEvent(line)

    if (event.type === "start") {
      onStart?.(event.conversation_id)
      return
    }

    if (event.type === "chunk") {
      onChunk?.(event.content)
      return
    }

    if (event.type === "error") {
      throw new Error(event.message || "Gagal menerima streaming jawaban.")
    }

    finalResult = mapPostChatResult(event.chat)
  }

  while (true) {
    const { done, value } = await reader.read()
    buffered += decoder.decode(value, { stream: !done })

    const lines = buffered.split("\n")
    buffered = lines.pop() ?? ""

    for (const line of lines) {
      handleLine(line.trim())
    }

    if (done) {
      break
    }
  }

  if (buffered.trim().length > 0) {
    handleLine(buffered.trim())
  }

  if (!finalResult) {
    throw new Error("Respons streaming tidak lengkap.")
  }

  return finalResult
}

export const getDocumentDownloadUrl = async ({
  documentUrl,
  signal,
}: GetDocumentDownloadUrlParams): Promise<DocumentDownloadResult> => {
  const response = await fetch(documentUrl, {
    method: "GET",
    headers: getAuthHeaders(false),
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal membuka dokumen."))
  }

  const payload = (await response.json()) as DocumentDownloadApiResponse

  if (typeof payload.download_url !== "string" || payload.download_url.trim().length === 0) {
    throw new Error("Download URL dokumen tidak valid.")
  }

  return {
    downloadUrl: payload.download_url,
    filename:
      typeof payload.filename === "string" && payload.filename.trim().length > 0
        ? payload.filename
        : "Dokumen",
  }
}

export const listConversations = async ({
  limit = 20,
  offset = 0,
  signal,
}: ListConversationsParams): Promise<ConversationSummary[]> => {
  const params = new URLSearchParams({
    limit: String(limit),
    offset: String(offset),
  })

  const response = await fetch(`${API_BASE_URL}/chats/conversations?${params.toString()}`, {
    method: "GET",
    headers: getAuthHeaders(false),
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengambil riwayat chat."))
  }

  const payload = (await response.json()) as ConversationApiResponse[]
  return payload.map(mapConversationSummary)
}

export const getConversation = async ({
  conversationId,
  signal,
}: GetConversationParams): Promise<ConversationDetail> => {
  const response = await fetch(`${API_BASE_URL}/chats/conversations/${conversationId}`, {
    method: "GET",
    headers: getAuthHeaders(false),
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal memuat percakapan."))
  }

  const payload = (await response.json()) as ConversationApiResponse
  return mapConversationDetail(payload)
}
