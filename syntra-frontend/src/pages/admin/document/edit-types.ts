export type DocumentType = "journal" | "conference" | "thesis" | "book" | "report"
export type ChunkType = "title" | "abstract" | "paragraph" | "table" | "image" | "reference"
export type ProcessingStatus = "uploading" | "processing" | "completed" | "failed"

export type JsonValue =
  | string
  | number
  | boolean
  | null
  | { [key: string]: JsonValue }
  | JsonValue[]

export interface DocumentChunk {
  id: number
  document_id: number
  chunk_index: number
  content: string
  token_count: number | null
  embedding: JsonValue | null
  possibly_questions: string[] | null
  possibly_question_embedding: JsonValue | null
  page_number: number | null
  section_title: string | null
  chunk_type: ChunkType | null
  chunk_metadata: JsonValue | null
  created_at: string
  updated_at: string | null
}

export interface DocumentDetail {
  id: number

  // Dublin Core Metadata
  title: string
  creator: string | null
  keywords: string | null
  description: string | null
  publisher: string | null
  contributor: string | null
  date: string | null
  type: DocumentType
  format: string | null
  identifier: string | null
  source: string | null
  language: string | null
  relation: string | null
  coverage: string | null
  rights: string | null

  // Extended metadata
  doi: string | null
  abstract: string | null
  citation_count: number

  // File storage
  file_path: string | null

  // Processing status
  processing_status: ProcessingStatus
  processing_progress: number
  processing_error: string | null

  // Status flags
  is_private: boolean
  is_metadata_complete: boolean

  // Timestamps
  created_at: string
  updated_at: string | null

  // Chunks
  chunk_count: number
  chunks: DocumentChunk[]
}

export interface DocumentUpdatePayload {
  // Dublin Core Metadata
  title?: string
  creator?: string | null
  keywords?: string | null
  description?: string | null
  publisher?: string | null
  contributor?: string | null
  date?: string | null
  type?: DocumentType
  format?: string | null
  identifier?: string | null
  source?: string | null
  language?: string | null
  relation?: string | null
  coverage?: string | null
  rights?: string | null

  // Extended metadata
  doi?: string | null
  abstract?: string | null
  citation_count?: number

  // Status flags
  is_private?: boolean
  is_metadata_complete?: boolean
}

export interface ChunkUpdatePayload {
  content?: string
  page_number?: number | null
  section_title?: string | null
  chunk_type?: ChunkType | null
  chunk_metadata?: JsonValue | null
}
