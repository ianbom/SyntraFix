import Cookies from "js-cookie"
import type { AuthToken, LoginCredentials, LoginResponse, User } from "./types"

const AUTH_TOKEN_KEY = "auth_token"
const AUTH_COOKIE_EXPIRES_DAYS = 7
const TOKEN_REFRESH_INTERVAL_MS = 5 * 60 * 1000
const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000").replace(/\/$/, "")
type AuthStateListener = () => void

const authStateListeners = new Set<AuthStateListener>()
let refreshPromise: Promise<boolean> | null = null
let cachedAuthToken: AuthToken | null = null

const notifyAuthStateChange = () => {
  authStateListeners.forEach((listener) => {
    listener()
  })
}

const isUser = (value: unknown): value is User => {
  if (typeof value !== "object" || value === null) {
    return false
  }

  const maybeUser = value as Partial<User>
  return (
    typeof maybeUser.id === "number" &&
    typeof maybeUser.email === "string" &&
    typeof maybeUser.username === "string" &&
    typeof maybeUser.role === "string" &&
    typeof maybeUser.is_active === "boolean" &&
    typeof maybeUser.created_at === "string" &&
    typeof maybeUser.updated_at === "string"
  )
}

const parseAuthToken = (rawToken: string): AuthToken | null => {
  try {
    const parsed = JSON.parse(rawToken) as Partial<AuthToken>

    if (
      typeof parsed !== "object" ||
      parsed === null ||
      typeof parsed.access_token !== "string" ||
      typeof parsed.refresh_token !== "string" ||
      typeof parsed.token_type !== "string" ||
      !isUser(parsed.user)
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

const clearStoredAuthToken = () => {
  Cookies.remove(AUTH_TOKEN_KEY)
  cachedAuthToken = null
}

const getStoredAuthToken = (): AuthToken | null => {
  if (cachedAuthToken) {
    return cachedAuthToken
  }

  const rawToken = Cookies.get(AUTH_TOKEN_KEY)
  if (!rawToken) {
    return null
  }

  const parsedToken = parseAuthToken(rawToken)
  if (!parsedToken) {
    return null
  }

  cachedAuthToken = parsedToken
  return cachedAuthToken
}

const setStoredAuthToken = (token: AuthToken) => {
  Cookies.set(AUTH_TOKEN_KEY, JSON.stringify(token), {
    expires: AUTH_COOKIE_EXPIRES_DAYS,
    sameSite: "lax",
  })
  cachedAuthToken = token
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
    setStoredAuthToken(token)
    notifyAuthStateChange()

    return {
      success: true,
      user: token.user,
    }
  },

  logout: () => {
    clearStoredAuthToken()
    notifyAuthStateChange()
  },

  getCurrentUser: (): User | null => {
    const authToken = getStoredAuthToken()
    return authToken?.user ?? null
  },

  isAuthenticated: (): boolean => {
    return getStoredAuthToken() !== null
  },

  getAccessToken: (): string | null => {
    const authToken = getStoredAuthToken()
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

  refreshToken: async (): Promise<boolean> => {
    const currentToken = getStoredAuthToken()
    if (!currentToken) {
      return false
    }

    if (refreshPromise) {
      return refreshPromise
    }

    refreshPromise = (async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/auth/refresh`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ refresh_token: currentToken.refresh_token }),
        })

        if (response.status === 401) {
          clearStoredAuthToken()
          notifyAuthStateChange()
          return false
        }

        if (!response.ok) {
          return false
        }

        const payload = (await response.json()) as Partial<AuthToken>
        if (
          typeof payload.access_token !== "string" ||
          typeof payload.refresh_token !== "string" ||
          typeof payload.token_type !== "string"
        ) {
          return false
        }

        const refreshedToken: AuthToken = {
          access_token: payload.access_token,
          refresh_token: payload.refresh_token,
          token_type: payload.token_type,
          user: isUser(payload.user) ? payload.user : currentToken.user,
        }

        setStoredAuthToken(refreshedToken)
        notifyAuthStateChange()
        return true
      } catch (error) {
        console.error("Failed to refresh token.", error)
        return false
      }
    })()

    try {
      return await refreshPromise
    } finally {
      refreshPromise = null
    }
  },

  getRefreshIntervalMs: () => TOKEN_REFRESH_INTERVAL_MS,

  subscribe: (listener: AuthStateListener) => {
    authStateListeners.add(listener)
    return () => {
      authStateListeners.delete(listener)
    }
  },
}
