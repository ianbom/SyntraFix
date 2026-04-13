export interface Document {
  id: string
  title: string
  creator: string
  keywords: string[]
  doi: string
  publishedAt: string | null
  createdAt: string
  status: "published" | "draft" | "pending"
}

export type DocumentType = "journal" | "conference" | "thesis" | "report" | "book"

export interface DocumentListItem {
  id: number
  title: string
  creator: string | null
  type: DocumentType
  doi: string | null
  isPrivate: boolean
  publishedAt: string | null
  createdAt: string
}

export interface DocumentListResponse {
  documents: DocumentListItem[]
  total: number
  page: number
  perPage: number
  pages: number
}

export interface BulkUploadItemResult {
  filename: string
  status: "pending" | "processing" | "error"
  documentId: number | null
  error: string | null
}

export interface BulkUploadResponse {
  total: number
  processingCount: number
  errorCount: number
  results: BulkUploadItemResult[]
}

export interface UploadedFile {
  id: string
  file: File
  status: "pending" | "uploading" | "success" | "error"
  progress: number
  errorMessage?: string
}

export type ProcessDocumentStatus = "processing" | "completed" | "failed"

export interface ProcessDocument {
  id: string
  title: string
  creator: string
  uploadedAt: string
  progress: number
  status: ProcessDocumentStatus
}

export interface ProcessMonitorSummary {
  total: number
  processing: number
  completed: number
  failed: number
}

export interface ProcessMonitorResponse {
  documents: ProcessDocument[]
  summary: ProcessMonitorSummary
}
