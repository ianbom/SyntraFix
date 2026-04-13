export type UserRole = "admin" | "user"

export interface User {
  id: number
  email: string
  username: string
  role: UserRole
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface AuthToken {
  access_token: string
  refresh_token: string
  token_type: string
  user: User
}

export interface LoginCredentials {
  email: string
  password: string
}

export interface LoginResponse {
  success: boolean
  message?: string
  user?: User
}
