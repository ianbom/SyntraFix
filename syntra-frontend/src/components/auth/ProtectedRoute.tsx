import { useSyncExternalStore } from "react"
import { Navigate } from "react-router-dom"
import { authService } from "@/lib/auth"

interface ProtectedRouteProps {
  children: React.ReactNode
}

export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const currentUser = useSyncExternalStore(
    authService.subscribe,
    authService.getCurrentUser,
    authService.getCurrentUser
  )
  const isAuthenticated = currentUser !== null

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
  }

  return <>{children}</>
}
