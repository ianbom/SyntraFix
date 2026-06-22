import { authService } from "@/lib/auth"
import type {
  DashboardDistribution,
  DashboardSummary,
  EvaluationMode,
  Paginated,
  RagDataset,
  RagDatasetDetail,
  RagDatasetRow,
  RagRun,
  RagSample,
} from "./types"

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000").replace(/\/$/, "")

interface ApiErrorPayload {
  detail?: unknown
  message?: unknown
}

const authHeaders = (): HeadersInit => {
  const token = authService.getAccessToken()
  if (!token) throw new Error("Sesi login tidak ditemukan. Silakan login ulang.")
  return { Authorization: `Bearer ${token}` }
}

const errorMessage = async (response: Response, fallback: string) => {
  const contentType = response.headers.get("content-type") ?? ""
  if (contentType.includes("application/json")) {
    const payload = (await response.json()) as ApiErrorPayload
    if (typeof payload.detail === "string") return payload.detail
    if (typeof payload.message === "string") return payload.message
  }
  const text = await response.text()
  return text || fallback
}

const requestJson = async <T>(path: string, init: RequestInit = {}, fallback = "Request gagal."): Promise<T> => {
  const headers = new Headers(init.headers)
  if (!(init.body instanceof FormData)) headers.set("Content-Type", "application/json")
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: { ...Object.fromEntries(headers), ...authHeaders() },
  })
  if (!response.ok) throw new Error(await errorMessage(response, fallback))
  return (await response.json()) as T
}

export const getDashboardSummary = async (): Promise<DashboardSummary> =>
  mapSummary(await requestJson<ApiDashboardSummary>("/rag-evaluation/dashboard/summary"))

export const getDashboardDistribution = async (runId?: number): Promise<DashboardDistribution> => {
  const suffix = runId ? `?run_id=${runId}` : ""
  const payload = await requestJson<ApiDistribution>(`/rag-evaluation/dashboard/distribution${suffix}`)
  return { runId: payload.run_id, buckets: payload.buckets }
}

export const listDatasets = async (page = 1, perPage = 20): Promise<Paginated<RagDataset>> => {
  const payload = await requestJson<ApiDatasetList>(`/rag-evaluation/datasets?page=${page}&per_page=${perPage}`)
  return { items: payload.datasets.map(mapDataset), total: payload.total, page: payload.page, perPage: payload.per_page, pages: payload.pages }
}

export const getDataset = async (id: number): Promise<RagDatasetDetail> => mapDatasetDetail(await requestJson<ApiDatasetDetail>(`/rag-evaluation/datasets/${id}`))

export const deleteDatasetRow = async (datasetId: number, rowId: number): Promise<void> => {
  await requestJson<{ message: string }>(`/rag-evaluation/datasets/${datasetId}/rows/${rowId}`, { method: "DELETE" }, "Gagal menghapus baris dataset.")
}

export const uploadDataset = async (params: { file: File; mode: EvaluationMode; name?: string; description?: string }): Promise<RagDatasetDetail> => {
  const form = new FormData()
  form.set("file", params.file)
  form.set("evaluation_mode", params.mode)
  if (params.name) form.set("name", params.name)
  if (params.description) form.set("description", params.description)
  return mapDatasetDetail(await requestJson<ApiDatasetDetail>("/rag-evaluation/datasets/upload", { method: "POST", body: form }, "Gagal upload dataset."))
}

export const createRun = async (datasetId: number, name: string, mode?: EvaluationMode): Promise<RagRun> =>
  mapRun(await requestJson<ApiRun>("/rag-evaluation/runs", { method: "POST", body: JSON.stringify({ dataset_id: datasetId, name, evaluation_mode: mode }) }, "Gagal membuat evaluasi."))

export const listRuns = async (page = 1, perPage = 20): Promise<Paginated<RagRun>> => {
  const payload = await requestJson<ApiRunList>(`/rag-evaluation/runs?page=${page}&per_page=${perPage}`)
  return { items: payload.runs.map(mapRun), total: payload.total, page: payload.page, perPage: payload.per_page, pages: payload.pages }
}

export const getRun = async (id: number): Promise<RagRun> => mapRun(await requestJson<ApiRun>(`/rag-evaluation/runs/${id}`))

export const listSamples = async (runId: number, page = 1, perPage = 50): Promise<Paginated<RagSample>> => {
  const payload = await requestJson<ApiSampleList>(`/rag-evaluation/runs/${runId}/samples?page=${page}&per_page=${perPage}`)
  return { items: payload.samples.map(mapSample), total: payload.total, page: payload.page, perPage: payload.per_page, pages: payload.pages }
}

export const listAllSamples = async (runId: number): Promise<Paginated<RagSample>> => {
  const payload = await requestJson<ApiSampleList>(`/rag-evaluation/runs/${runId}/samples?all=true`)
  return { items: payload.samples.map(mapSample), total: payload.total, page: payload.page, perPage: payload.per_page, pages: payload.pages }
}

export const cancelRun = async (runId: number): Promise<RagRun> =>
  mapRun(await requestJson<ApiRun>(`/rag-evaluation/runs/${runId}/cancel`, { method: "POST" }))

export const downloadUrl = (path: string) => `${API_BASE_URL}${path}`

export const authDownloadHeaders = authHeaders

export const downloadFile = async (path: string, filename: string) => {
  const response = await fetch(downloadUrl(path), { headers: authHeaders() })
  if (!response.ok) throw new Error(await errorMessage(response, "Download gagal."))
  const blob = await response.blob()
  saveBlob(blob, filename)
}

export interface ExportChatCsvParams {
  dateFrom: string
  dateTo: string
}

export const exportChatCsv = async ({ dateFrom, dateTo }: ExportChatCsvParams) => {
  const response = await fetch(`${API_BASE_URL}/rag-evaluation/chat-export`, {
    method: "POST",
    headers: {
      ...authHeaders(),
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      date_from: toStartOfDayIso(dateFrom),
      date_to: toEndOfDayIso(dateTo),
      user_ids: [],
      conversation_ids: [],
      only_with_references: false,
      create_dataset: false,
    }),
  })

  if (!response.ok) throw new Error(await errorMessage(response, "Gagal export chat CSV."))
  saveBlob(await response.blob(), "chat-export-ragas.csv")
}

const toStartOfDayIso = (date: string) => new Date(`${date}T00:00:00`).toISOString()
const toEndOfDayIso = (date: string) => new Date(`${date}T23:59:59`).toISOString()

const saveBlob = (blob: Blob, filename: string) => {
  const url = window.URL.createObjectURL(blob)
  const link = document.createElement("a")
  link.href = url
  link.download = filename
  document.body.appendChild(link)
  link.click()
  link.remove()
  window.URL.revokeObjectURL(url)
}

interface ApiDataset {
  id: number; name: string; description: string | null; source_type: string; evaluation_mode: EvaluationMode; original_filename: string | null; file_path: string | null; dataset_hash: string | null; total_rows: number; valid_rows: number; invalid_rows: number; status: RagDataset["status"]; validation_errors: Array<{ row_number: number; message: string }> | null; created_by: number; created_at: string | null
}
interface ApiDatasetRow { id: number; row_number: number; test_case_id: string | null; user_input: string; reference: string | null; response: string | null; retrieved_contexts: string[] | null; category: string | null; source_document_ids: unknown[] | null; notes: string | null; validation_status: string; validation_message: string | null }
interface ApiDatasetDetail extends ApiDataset { rows: ApiDatasetRow[] }
interface ApiDatasetList { datasets: ApiDataset[]; total: number; page: number; per_page: number; pages: number }
interface ApiRun { id: number; dataset_id: number; dataset_name: string | null; name: string; description: string | null; status: RagRun["status"]; evaluation_mode: EvaluationMode; total_samples: number; processed_samples: number; successful_samples: number; failed_samples: number; progress: number; faithfulness_avg: number | null; answer_relevancy_avg: number | null; context_precision_avg: number | null; context_recall_avg: number | null; generator_model: string | null; embedding_model: string | null; evaluator_model: string | null; ragas_version: string | null; config_snapshot: Record<string, unknown> | null; celery_task_id: string | null; created_by: number; started_at: string | null; completed_at: string | null; error_message: string | null; created_at: string | null }
interface ApiRunList { runs: ApiRun[]; total: number; page: number; per_page: number; pages: number }
interface ApiSample { id: number; run_id: number; dataset_row_id: number; sample_index: number; user_input: string; reference: string | null; response: string | null; retrieved_contexts: string[] | null; references_metadata: Array<Record<string, unknown>> | null; faithfulness: number | null; answer_relevancy: number | null; context_precision: number | null; context_recall: number | null; rag_duration_seconds: number | null; evaluation_duration_seconds: number | null; status: RagSample["status"]; error_message: string | null; completed_at: string | null }
interface ApiSampleList { samples: ApiSample[]; total: number; page: number; per_page: number; pages: number }
interface ApiHistory { id: number; name: string; created_at: string | null; total_samples: number; faithfulness: number | null; answer_relevancy: number | null; context_precision: number | null; context_recall: number | null }
interface ApiDashboardSummary { active_run: ApiRun | null; latest_completed_run: ApiRun | null; previous_completed_run: ApiRun | null; history: ApiHistory[] }
interface ApiDistribution { run_id: number | null; buckets: Record<string, Record<string, number>> }

const mapDataset = (item: ApiDataset): RagDataset => ({ id: item.id, name: item.name, description: item.description, sourceType: item.source_type, evaluationMode: item.evaluation_mode, originalFilename: item.original_filename, filePath: item.file_path, datasetHash: item.dataset_hash, totalRows: item.total_rows, validRows: item.valid_rows, invalidRows: item.invalid_rows, status: item.status, validationErrors: item.validation_errors, createdBy: item.created_by, createdAt: item.created_at })
const mapRow = (item: ApiDatasetRow): RagDatasetRow => ({ id: item.id, rowNumber: item.row_number, testCaseId: item.test_case_id, userInput: item.user_input, reference: item.reference, response: item.response, retrievedContexts: item.retrieved_contexts, category: item.category, sourceDocumentIds: item.source_document_ids, notes: item.notes, validationStatus: item.validation_status, validationMessage: item.validation_message })
const mapDatasetDetail = (item: ApiDatasetDetail): RagDatasetDetail => ({ ...mapDataset(item), rows: item.rows.map(mapRow) })
const mapRun = (item: ApiRun): RagRun => ({ id: item.id, datasetId: item.dataset_id, datasetName: item.dataset_name, name: item.name, description: item.description, status: item.status, evaluationMode: item.evaluation_mode, totalSamples: item.total_samples, processedSamples: item.processed_samples, successfulSamples: item.successful_samples, failedSamples: item.failed_samples, progress: item.progress, faithfulnessAvg: item.faithfulness_avg, answerRelevancyAvg: item.answer_relevancy_avg, contextPrecisionAvg: item.context_precision_avg, contextRecallAvg: item.context_recall_avg, generatorModel: item.generator_model, embeddingModel: item.embedding_model, evaluatorModel: item.evaluator_model, ragasVersion: item.ragas_version, configSnapshot: item.config_snapshot, celeryTaskId: item.celery_task_id, createdBy: item.created_by, startedAt: item.started_at, completedAt: item.completed_at, errorMessage: item.error_message, createdAt: item.created_at })
const mapSample = (item: ApiSample): RagSample => ({ id: item.id, runId: item.run_id, datasetRowId: item.dataset_row_id, sampleIndex: item.sample_index, userInput: item.user_input, reference: item.reference, response: item.response, retrievedContexts: item.retrieved_contexts, referencesMetadata: item.references_metadata, faithfulness: item.faithfulness, answerRelevancy: item.answer_relevancy, contextPrecision: item.context_precision, contextRecall: item.context_recall, ragDurationSeconds: item.rag_duration_seconds, evaluationDurationSeconds: item.evaluation_duration_seconds, status: item.status, errorMessage: item.error_message, completedAt: item.completed_at })
const mapSummary = (payload: ApiDashboardSummary): DashboardSummary => ({ activeRun: payload.active_run ? mapRun(payload.active_run) : null, latestCompletedRun: payload.latest_completed_run ? mapRun(payload.latest_completed_run) : null, previousCompletedRun: payload.previous_completed_run ? mapRun(payload.previous_completed_run) : null, history: payload.history.map((item) => ({ id: item.id, name: item.name, createdAt: item.created_at, totalSamples: item.total_samples, faithfulness: item.faithfulness, answerRelevancy: item.answer_relevancy, contextPrecision: item.context_precision, contextRecall: item.context_recall })) })
