import Cookies from "js-cookie"
import type { AuthToken, LoginCredentials, LoginResponse, User } from "./types"

const AUTH_TOKEN_KEY = "auth_token"
const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000").replace(/\/$/, "")

const parseAuthToken = (rawToken: string): AuthToken | null => {
  try {
    const parsed = JSON.parse(rawToken) as Partial<AuthToken>

    if (
      typeof parsed !== "object" ||
      parsed === null ||
      typeof parsed.access_token !== "string" ||
      typeof parsed.refresh_token !== "string" ||
      typeof parsed.token_type !== "string" ||
      typeof parsed.user !== "object" ||
      parsed.user === null ||
      typeof parsed.user.role !== "string"
    ) {
      Cookies.remove(AUTH_TOKEN_KEY)
      return null
    }

    return parsed as AuthToken
  } catch (error) {
    console.error("Failed to parse auth token from cookie.", error)
    Cookies.remove(AUTH_TOKEN_KEY)
    return null
  }
}

const getErrorMessage = async (response: Response): Promise<string> => {
  const contentType = response.headers.get("content-type") ?? ""

  if (contentType.includes("application/json")) {
    const data = (await response.json()) as { detail?: string; message?: string }
    return data.detail ?? data.message ?? "Login gagal"
  }

  const text = await response.text()
  return text || "Login gagal"
}

export const authService = {
  login: async (credentials: LoginCredentials): Promise<LoginResponse> => {
    const formData = new URLSearchParams({
      username: credentials.email,
      password: credentials.password,
    })

    const response = await fetch(`${API_BASE_URL}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formData.toString(),
    })

    if (!response.ok) {
      return {
        success: false,
        message: await getErrorMessage(response),
      }
    }

    const token = (await response.json()) as AuthToken
    Cookies.set(AUTH_TOKEN_KEY, JSON.stringify(token), { expires: 7, sameSite: "lax" })

    return {
      success: true,
      user: token.user,
    }
  },

  logout: () => {
    Cookies.remove(AUTH_TOKEN_KEY)
  },

  getCurrentUser: (): User | null => {
    const rawToken = Cookies.get(AUTH_TOKEN_KEY)
    if (!rawToken) {
      return null
    }

    const authToken = parseAuthToken(rawToken)
    return authToken?.user ?? null
  },

  isAuthenticated: (): boolean => {
    const rawToken = Cookies.get(AUTH_TOKEN_KEY)
    if (!rawToken) {
      return false
    }

    return parseAuthToken(rawToken) !== null
  },

  getAccessToken: (): string | null => {
    const rawToken = Cookies.get(AUTH_TOKEN_KEY)
    if (!rawToken) {
      return null
    }

    const authToken = parseAuthToken(rawToken)
    return authToken?.access_token ?? null
  },

  isAdmin: (): boolean => {
    const user = authService.getCurrentUser()
    return user?.role === "admin"
  },

  isUser: (): boolean => {
    const user = authService.getCurrentUser()
    return user?.role === "user"
  },
}
