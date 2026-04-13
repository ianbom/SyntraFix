import { useSyncExternalStore } from "react"
import { Navigate } from "react-router-dom"
import { authService } from "@/lib/auth"

interface AdminRouteProps {
  children: React.ReactNode
}

export function AdminRoute({ children }: AdminRouteProps) {
  const currentUser = useSyncExternalStore(
    authService.subscribe,
    authService.getCurrentUser,
    authService.getCurrentUser
  )
  const isAuthenticated = currentUser !== null
  const isAdmin = currentUser?.role === "admin"

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
  }

  if (!isAdmin) {
    return <Navigate to="/unauthorized" replace />
  }

  return <>{children}</>
}
