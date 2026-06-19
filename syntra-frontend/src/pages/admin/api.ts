import { authService } from "@/lib/auth"

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000").replace(/\/$/, "")

interface ApiErrorPayload {
  detail?: unknown
  message?: unknown
}

const toErrorMessage = (payload: ApiErrorPayload, fallbackMessage: string): string => {
  if (typeof payload.message === "string" && payload.message.trim().length > 0) {
    return payload.message
  }

  if (typeof payload.detail === "string" && payload.detail.trim().length > 0) {
    return payload.detail
  }

  return fallbackMessage
}

const getErrorMessage = async (response: Response, fallbackMessage: string): Promise<string> => {
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

export interface AdminUserApiItem {
  id: number
  username: string
  email: string
  role: "admin" | "user"
  is_active: boolean
  created_at: string
  updated_at: string | null
}

export interface AdminUserListResponse {
  users: AdminUserApiItem[]
  total: number
  page: number
  perPage: number
  pages: number
}

export interface ListAdminUsersParams {
  page?: number
  perPage?: number
  search?: string
  status?: "active" | "inactive"
  signal?: AbortSignal
}

export interface AdminDashboardStats {
  totalUsers: number
  activeUsers: number
  inactiveUsers: number
  newUsersThisMonth: number
  totalDocuments: number
  processedDocuments: number
  processingDocuments: number
  failedDocuments: number
  totalConversations: number
  totalChats: number
}

export interface AdminDashboardChartPoint {
  date: string
  users: number
  documents: number
  chats: number
}

export interface AdminRecentDocument {
  id: number
  title: string
  type: string | null
  processingStatus: string | null
  createdAt: string
}

export interface AdminDashboardResponse {
  stats: AdminDashboardStats
  chart: AdminDashboardChartPoint[]
  recentDocuments: AdminRecentDocument[]
}

interface AdminUserListApiResponse {
  users: AdminUserApiItem[]
  total: number
  page: number
  per_page: number
  pages: number
}

interface AdminDashboardApiResponse {
  stats: {
    total_users: number
    active_users: number
    inactive_users: number
    new_users_this_month: number
    total_documents: number
    processed_documents: number
    processing_documents: number
    failed_documents: number
    total_conversations: number
    total_chats: number
  }
  chart: AdminDashboardChartPoint[]
  recent_documents: Array<{
    id: number
    title: string
    type: string | null
    processing_status: string | null
    created_at: string
  }>
}

export const listAdminUsers = async ({
  page = 1,
  perPage = 100,
  search,
  status,
  signal,
}: ListAdminUsersParams = {}): Promise<AdminUserListResponse> => {
  const params = new URLSearchParams({
    page: String(page),
    per_page: String(perPage),
  })

  const normalizedSearch = search?.trim()
  if (normalizedSearch) {
    params.set("search", normalizedSearch)
  }

  if (status) {
    params.set("status", status)
  }

  const response = await fetch(`${API_BASE_URL}/admin/users?${params.toString()}`, {
    method: "GET",
    headers: getAuthHeaders(),
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengambil data user."))
  }

  const payload = (await response.json()) as AdminUserListApiResponse

  return {
    users: payload.users,
    total: payload.total,
    page: payload.page,
    perPage: payload.per_page,
    pages: payload.pages,
  }
}

export const getAdminDashboard = async (signal?: AbortSignal): Promise<AdminDashboardResponse> => {
  const response = await fetch(`${API_BASE_URL}/admin/dashboard`, {
    method: "GET",
    headers: getAuthHeaders(),
    signal,
  })

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Gagal mengambil data dashboard."))
  }

  const payload = (await response.json()) as AdminDashboardApiResponse

  return {
    stats: {
      totalUsers: payload.stats.total_users,
      activeUsers: payload.stats.active_users,
      inactiveUsers: payload.stats.inactive_users,
      newUsersThisMonth: payload.stats.new_users_this_month,
      totalDocuments: payload.stats.total_documents,
      processedDocuments: payload.stats.processed_documents,
      processingDocuments: payload.stats.processing_documents,
      failedDocuments: payload.stats.failed_documents,
      totalConversations: payload.stats.total_conversations,
      totalChats: payload.stats.total_chats,
    },
    chart: payload.chart,
    recentDocuments: payload.recent_documents.map((document) => ({
      id: document.id,
      title: document.title,
      type: document.type,
      processingStatus: document.processing_status,
      createdAt: document.created_at,
    })),
  }
}
