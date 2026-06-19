import Cookies from "js-cookie"
import type { AuthToken, LoginCredentials, LoginResponse, User } from "./types"

const AUTH_TOKEN_KEY = "auth_token"
const AUTH_TOKEN_STORAGE_KEY = "syntra_auth_token"
const AUTH_COOKIE_EXPIRES_DAYS = 7
const AUTH_COOKIE_OPTIONS = {
  expires: AUTH_COOKIE_EXPIRES_DAYS,
  sameSite: "lax" as const,
  path: "/",
}
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

const removeAuthTokenCookie = () => {
  Cookies.remove(AUTH_TOKEN_KEY)
  Cookies.remove(AUTH_TOKEN_KEY, { path: "/" })
  Cookies.remove(AUTH_TOKEN_KEY, { path: "/login" })
  Cookies.remove(AUTH_TOKEN_KEY, { path: "/admin" })
  Cookies.remove(AUTH_TOKEN_KEY, { path: "/chat" })
}

const getStoredAuthTokenFromLocalStorage = (): string | null => {
  try {
    return window.localStorage.getItem(AUTH_TOKEN_STORAGE_KEY)
  } catch (error) {
    console.error("Failed to read auth token from local storage.", error)
    return null
  }
}

const setStoredAuthTokenInLocalStorage = (rawToken: string) => {
  try {
    window.localStorage.setItem(AUTH_TOKEN_STORAGE_KEY, rawToken)
  } catch (error) {
    console.error("Failed to store auth token in local storage.", error)
  }
}

const removeStoredAuthTokenFromLocalStorage = () => {
  try {
    window.localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
  } catch (error) {
    console.error("Failed to remove auth token from local storage.", error)
  }
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
      return null
    }

    return parsed as AuthToken
  } catch (error) {
    console.error("Failed to parse auth token from cookie.", error)
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
  removeAuthTokenCookie()
  removeStoredAuthTokenFromLocalStorage()
  cachedAuthToken = null
}

const getStoredAuthToken = (): AuthToken | null => {
  if (cachedAuthToken) {
    return cachedAuthToken
  }

  const rawCookieToken = Cookies.get(AUTH_TOKEN_KEY)
  if (rawCookieToken) {
    const parsedCookieToken = parseAuthToken(rawCookieToken)
    if (parsedCookieToken) {
      cachedAuthToken = parsedCookieToken
      return cachedAuthToken
    }
  }

  const rawLocalStorageToken = getStoredAuthTokenFromLocalStorage()
  if (rawLocalStorageToken) {
    const parsedLocalStorageToken = parseAuthToken(rawLocalStorageToken)
    if (parsedLocalStorageToken) {
      removeAuthTokenCookie()
      Cookies.set(AUTH_TOKEN_KEY, rawLocalStorageToken, AUTH_COOKIE_OPTIONS)
      cachedAuthToken = parsedLocalStorageToken
      return cachedAuthToken
    }
  }

  if (rawCookieToken || rawLocalStorageToken) {
    clearStoredAuthToken()
  }

  return null
}

const setStoredAuthToken = (token: AuthToken) => {
  const rawToken = JSON.stringify(token)
  removeAuthTokenCookie()
  Cookies.set(AUTH_TOKEN_KEY, rawToken, AUTH_COOKIE_OPTIONS)
  setStoredAuthTokenInLocalStorage(rawToken)
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
