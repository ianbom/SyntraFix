import type {
  BulkUploadItemResult,
  BulkUploadResponse,
  DocumentListItem,
  DocumentListResponse,
  DocumentType,
} from "./types"

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000").replace(/\/$/, "")

interface ListDocumentsApiItem {
  id: number
  title: string
  creator: string | null
  type: DocumentType
  doi: string | null
  is_private: boolean
  created_at: string
  publication_date?: string | null
  date?: string | null
}

interface ListDocumentsApiResponse {
  documents: ListDocumentsApiItem[]
  total: number
  page: number
  per_page: number
  pages: number
}

interface ListDocumentsParams {
  page: number
  perPage: number
  search?: string
  signal?: AbortSignal
}

interface ApiErrorPayload {
  detail?: unknown
  message?: unknown
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

const mapDocumentItem = (item: ListDocumentsApiItem): DocumentListItem => ({
  id: item.id,
  title: item.title,
  creator: item.creator,
  type: item.type,
  doi: item.doi,
  isPrivate: item.is_private,
  publishedAt: item.publication_date ?? item.date ?? null,
  createdAt: item.created_at,
})

export const listDocuments = async ({
  page,
  perPage,
  search,
  signal,
}: ListDocumentsParams): Promise<DocumentListResponse> => {
  const params = new URLSearchParams({
    page: String(page),
    per_page: String(perPage),
  })

  const normalizedSearch = search?.trim()
  if (normalizedSearch) {
    params.set("search", normalizedSearch)
  }

  const response = await fetch(`${API_BASE_URL}/documents/?${params.toString()}`, {
    method: "GET",
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengambil daftar dokumen."))
  }

  const payload = (await response.json()) as ListDocumentsApiResponse

  return {
    documents: payload.documents.map(mapDocumentItem),
    total: payload.total,
    page: payload.page,
    perPage: payload.per_page,
    pages: payload.pages,
  }
}

interface BulkUploadApiItemResult {
  filename: string
  status: "pending" | "processing" | "error"
  document_id: number | null
  error: string | null
}

interface BulkUploadApiResponse {
  total: number
  processing_count: number
  error_count: number
  results: BulkUploadApiItemResult[]
}

interface UploadDocumentsBulkParams {
  files: File[]
  type?: DocumentType
  isPrivate?: boolean
  clientId?: string
  signal?: AbortSignal
}

const mapBulkUploadResult = (item: BulkUploadApiItemResult): BulkUploadItemResult => ({
  filename: item.filename,
  status: item.status,
  documentId: item.document_id,
  error: item.error,
})

export const uploadDocumentsBulk = async ({
  files,
  type = "journal",
  isPrivate = false,
  clientId,
  signal,
}: UploadDocumentsBulkParams): Promise<BulkUploadResponse> => {
  if (files.length === 0) {
    throw new Error("Harap pilih minimal 1 dokumen.")
  }

  const formData = new FormData()
  files.forEach((file) => {
    formData.append("files", file, file.name)
  })

  const params = new URLSearchParams({
    type,
    is_private: String(isPrivate),
  })

  const normalizedClientId = clientId?.trim()
  if (normalizedClientId) {
    params.set("client_id", normalizedClientId)
  }

  const response = await fetch(`${API_BASE_URL}/documents/upload-bulk?${params.toString()}`, {
    method: "POST",
    body: formData,
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengunggah dokumen."))
  }

  const payload = (await response.json()) as BulkUploadApiResponse

  return {
    total: payload.total,
    processingCount: payload.processing_count,
    errorCount: payload.error_count,
    results: payload.results.map(mapBulkUploadResult),
  }
}
