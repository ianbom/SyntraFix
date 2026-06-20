export type EvaluationMode = "pipeline" | "score_only"
export type DatasetStatus = "uploaded" | "validating" | "ready" | "invalid"
export type RunStatus =
  | "queued"
  | "preparing"
  | "running_rag"
  | "running_ragas"
  | "aggregating"
  | "completed"
  | "partial_failed"
  | "failed"
  | "cancelled"
export type SampleStatus = "pending" | "processing" | "completed" | "failed"

export interface RagDatasetRow {
  id: number
  rowNumber: number
  testCaseId: string | null
  userInput: string
  reference: string | null
  response: string | null
  retrievedContexts: string[] | null
  category: string | null
  sourceDocumentIds: unknown[] | null
  notes: string | null
  validationStatus: string
  validationMessage: string | null
}

export interface RagDataset {
  id: number
  name: string
  description: string | null
  sourceType: string
  evaluationMode: EvaluationMode
  originalFilename: string | null
  filePath: string | null
  datasetHash: string | null
  totalRows: number
  validRows: number
  invalidRows: number
  status: DatasetStatus
  validationErrors: Array<{ row_number: number; message: string }> | null
  createdBy: number
  createdAt: string | null
}

export interface RagDatasetDetail extends RagDataset {
  rows: RagDatasetRow[]
}

export interface RagRun {
  id: number
  datasetId: number
  datasetName: string | null
  name: string
  description: string | null
  status: RunStatus
  evaluationMode: EvaluationMode
  totalSamples: number
  processedSamples: number
  successfulSamples: number
  failedSamples: number
  progress: number
  faithfulnessAvg: number | null
  answerRelevancyAvg: number | null
  contextPrecisionAvg: number | null
  contextRecallAvg: number | null
  generatorModel: string | null
  embeddingModel: string | null
  evaluatorModel: string | null
  ragasVersion: string | null
  configSnapshot: Record<string, unknown> | null
  celeryTaskId: string | null
  createdBy: number
  startedAt: string | null
  completedAt: string | null
  errorMessage: string | null
  createdAt: string | null
}

export interface RagSample {
  id: number
  runId: number
  datasetRowId: number
  sampleIndex: number
  userInput: string
  reference: string | null
  response: string | null
  retrievedContexts: string[] | null
  referencesMetadata: Array<Record<string, unknown>> | null
  faithfulness: number | null
  answerRelevancy: number | null
  contextPrecision: number | null
  contextRecall: number | null
  ragDurationSeconds: number | null
  evaluationDurationSeconds: number | null
  status: SampleStatus
  errorMessage: string | null
  completedAt: string | null
}

export interface DashboardHistoryPoint {
  id: number
  name: string
  createdAt: string | null
  totalSamples: number
  faithfulness: number | null
  answerRelevancy: number | null
  contextPrecision: number | null
  contextRecall: number | null
}

export interface DashboardSummary {
  activeRun: RagRun | null
  latestCompletedRun: RagRun | null
  previousCompletedRun: RagRun | null
  history: DashboardHistoryPoint[]
}

export interface DashboardDistribution {
  runId: number | null
  buckets: Record<string, Record<string, number>>
}

export interface Paginated<T> {
  total: number
  page: number
  perPage: number
  pages: number
  items: T[]
}
