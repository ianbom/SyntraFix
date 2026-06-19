import type {
  BulkUploadItemResult,
  BulkUploadResponse,
  DocumentListItem,
  DocumentListResponse,
  DocumentType,
  GeneratePossiblyQuestionsResponse,
  ProcessDocument,
  ProcessDocumentStatus,
  ProcessMonitorResponse,
} from "./types"
import type { ChunkType, DocumentChunk, DocumentDetail, JsonValue, ProcessingStatus } from "./edit-types"
import { authService } from "@/lib/auth"

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000").replace(/\/$/, "")
const DOCUMENT_TYPES: DocumentType[] = ["journal", "conference", "thesis", "report", "book"]
const CHUNK_TYPES: ChunkType[] = ["title", "abstract", "paragraph", "table", "image", "reference"]
const PROCESSING_STATUSES: ProcessingStatus[] = ["uploading", "processing", "completed", "failed"]

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

interface DocumentDetailApiChunk {
  id: number
  document_id: number
  chunk_index: number
  content: string
  token_count: number | null
  embedding: unknown | null
  possibly_questions: unknown
  possibly_question_embedding: unknown | null
  chunk_metadata: unknown
  page_number: number | null
  section_title: string | null
  chunk_type: string | null
  created_at: string
  updated_at: string | null
}

interface DocumentDetailApiDocument {
  id: number
  title: string
  creator: string | null
  keywords: string | null
  description: string | null
  publisher: string | null
  contributor: string | null
  date: string | null
  type: string | null
  format: string | null
  identifier: string | null
  source: string | null
  language: string | null
  relation: string | null
  coverage: string | null
  rights: string | null
  doi: string | null
  abstract: string | null
  citation_count: number | null
  file_path: string | null
  is_private: boolean | null
  is_metadata_complete: boolean | null
  processing_status: string | null
  processing_progress: number | null
  processing_error: string | null
  created_at: string
  updated_at: string | null
}

interface DocumentDetailApiResponse {
  document: DocumentDetailApiDocument
  chunks: DocumentDetailApiChunk[]
  chunk_count: number
}

interface GetDocumentDetailParams {
  documentId: number
  signal?: AbortSignal
}

interface GetDocumentDownloadUrlParams {
  documentId: number
  signal?: AbortSignal
}

interface DocumentDownloadApiResponse {
  download_url: unknown
  filename?: unknown
}

export interface DocumentDownloadResult {
  downloadUrl: string
  filename: string
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

const getAuthHeaders = (): HeadersInit => {
  const accessToken = authService.getAccessToken()
  if (!accessToken) {
    throw new Error("Sesi login tidak ditemukan. Silakan login ulang.")
  }

  return {
    Authorization: `Bearer ${accessToken}`,
  }
}

const isDocumentType = (value: string | null | undefined): value is DocumentType => {
  if (!value) {
    return false
  }

  return DOCUMENT_TYPES.includes(value as DocumentType)
}

const isChunkType = (value: string | null | undefined): value is ChunkType => {
  if (!value) {
    return false
  }

  return CHUNK_TYPES.includes(value as ChunkType)
}

const isProcessingStatus = (
  value: string | null | undefined
): value is ProcessingStatus => {
  if (!value) {
    return false
  }

  return PROCESSING_STATUSES.includes(value as ProcessingStatus)
}

const toStringArray = (value: unknown): string[] | null => {
  if (!Array.isArray(value)) {
    return null
  }

  const normalized = value
    .filter((item): item is string => typeof item === "string")
    .map((item) => item.trim())
    .filter((item) => item.length > 0)

  return normalized.length > 0 ? normalized : null
}

const isJsonValue = (value: unknown): value is JsonValue => {
  if (value === null) {
    return true
  }

  if (typeof value === "string" || typeof value === "number" || typeof value === "boolean") {
    return true
  }

  if (Array.isArray(value)) {
    return value.every((item) => isJsonValue(item))
  }

  if (typeof value === "object") {
    return Object.values(value).every((item) => isJsonValue(item))
  }

  return false
}

const toJsonValue = (value: unknown): JsonValue | null => {
  if (isJsonValue(value)) {
    return value
  }

  return null
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

const mapDocumentChunk = (chunk: DocumentDetailApiChunk): DocumentChunk => ({
  id: chunk.id,
  document_id: chunk.document_id,
  chunk_index: chunk.chunk_index,
  content: chunk.content,
  token_count: chunk.token_count,
  embedding: toJsonValue(chunk.embedding),
  possibly_questions: toStringArray(chunk.possibly_questions),
  possibly_question_embedding: toJsonValue(chunk.possibly_question_embedding),
  page_number: chunk.page_number,
  section_title: chunk.section_title,
  chunk_type: isChunkType(chunk.chunk_type) ? chunk.chunk_type : null,
  chunk_metadata: toJsonValue(chunk.chunk_metadata),
  created_at: chunk.created_at,
  updated_at: chunk.updated_at,
})

const mapDocumentDetail = (payload: DocumentDetailApiResponse): DocumentDetail => {
  const chunks = payload.chunks.map(mapDocumentChunk)
  const { document } = payload

  return {
    id: document.id,
    title: document.title,
    creator: document.creator,
    keywords: document.keywords,
    description: document.description,
    publisher: document.publisher,
    contributor: document.contributor,
    date: document.date,
    type: isDocumentType(document.type) ? document.type : "journal",
    format: document.format,
    identifier: document.identifier,
    source: document.source,
    language: document.language,
    relation: document.relation,
    coverage: document.coverage,
    rights: document.rights,
    doi: document.doi,
    abstract: document.abstract,
    citation_count: document.citation_count ?? 0,
    file_path: document.file_path,
    processing_status: isProcessingStatus(document.processing_status)
      ? document.processing_status
      : "processing",
    processing_progress: document.processing_progress ?? 0,
    processing_error: document.processing_error,
    is_private: document.is_private ?? false,
    is_metadata_complete: document.is_metadata_complete ?? false,
    created_at: document.created_at,
    updated_at: document.updated_at,
    chunk_count: payload.chunk_count ?? chunks.length,
    chunks,
  }
}

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

export const getDocumentDetail = async ({
  documentId,
  signal,
}: GetDocumentDetailParams): Promise<DocumentDetail> => {
  const response = await fetch(`${API_BASE_URL}/documents/${documentId}`, {
    method: "GET",
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengambil detail dokumen."))
  }

  const payload = (await response.json()) as DocumentDetailApiResponse

  if (!payload?.document || !Array.isArray(payload.chunks)) {
    throw new Error("Format respons detail dokumen tidak valid.")
  }

  return mapDocumentDetail(payload)
}

export const getDocumentDownloadUrl = async ({
  documentId,
  signal,
}: GetDocumentDownloadUrlParams): Promise<DocumentDownloadResult> => {
  const response = await fetch(`${API_BASE_URL}/documents/${documentId}/download`, {
    method: "GET",
    headers: getAuthHeaders(),
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

interface ListProcessingDocumentsParams {
  signal?: AbortSignal
}

interface GeneratePossiblyQuestionsParams {
  documentId: number
  signal?: AbortSignal
}

interface ProcessingMonitorApiItem {
  id: number
  title: string
  creator: string | null
  uploaded_at: string
  processing_status: string
  processing_progress: number
  processing_error: string | null
  chunk_count: number
  possibly_question_count: number
  possibly_question_missing_count: number
  possibly_question_progress: number
}

interface ProcessingMonitorApiSummary {
  total: number
  processing: number
  completed: number
  failed: number
}

interface ProcessingMonitorApiResponse {
  documents: ProcessingMonitorApiItem[]
  summary: ProcessingMonitorApiSummary
}

interface GeneratePossiblyQuestionsApiResponse {
  document_id: number
  task_id: string
  status: "queued"
  chunk_count: number
  possibly_question_count: number
  missing_possibly_question_count: number
}

const mapBulkUploadResult = (item: BulkUploadApiItemResult): BulkUploadItemResult => ({
  filename: item.filename,
  status: item.status,
  documentId: item.document_id,
  error: item.error,
})

const mapProcessingStatus = (status: string): ProcessDocumentStatus => {
  if (status === "completed" || status === "failed" || status === "processing") {
    return status
  }

  return "processing"
}

const mapProcessingDocument = (item: ProcessingMonitorApiItem): ProcessDocument => ({
  id: String(item.id),
  title: item.title,
  creator: item.creator ?? "-",
  uploadedAt: item.uploaded_at,
  progress: item.processing_progress,
  status: mapProcessingStatus(item.processing_status),
  chunkCount: item.chunk_count ?? 0,
  possiblyQuestionCount: item.possibly_question_count ?? 0,
  possiblyQuestionMissingCount: item.possibly_question_missing_count ?? 0,
  possiblyQuestionProgress: item.possibly_question_progress ?? 100,
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

export const listProcessingDocuments = async ({
  signal,
}: ListProcessingDocumentsParams): Promise<ProcessMonitorResponse> => {
  const response = await fetch(`${API_BASE_URL}/documents/processing-monitor`, {
    method: "GET",
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengambil data proses dokumen."))
  }

  const payload = (await response.json()) as ProcessingMonitorApiResponse

  return {
    documents: payload.documents.map(mapProcessingDocument),
    summary: payload.summary,
  }
}

export const generatePossiblyQuestions = async ({
  documentId,
  signal,
}: GeneratePossiblyQuestionsParams): Promise<GeneratePossiblyQuestionsResponse> => {
  const response = await fetch(
    `${API_BASE_URL}/documents/${documentId}/possibly-questions/generate`,
    {
      method: "POST",
      signal,
    }
  )

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal menjalankan generate question."))
  }

  const payload = (await response.json()) as GeneratePossiblyQuestionsApiResponse

  return {
    documentId: payload.document_id,
    taskId: payload.task_id,
    status: payload.status,
    chunkCount: payload.chunk_count,
    possiblyQuestionCount: payload.possibly_question_count,
    missingPossiblyQuestionCount: payload.missing_possibly_question_count,
  }
}
