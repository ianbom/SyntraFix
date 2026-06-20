import { useEffect } from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Welcome from "./pages/welcome"
import Dashboard from "./pages/admin/dashboard"
import Login from "./pages/auth/login"
import Register from "./pages/auth/register"
import DocumentListPage from "./pages/admin/document/list"
import UserListPage from "./pages/admin/user/list-user"
import CreateDocumentPage from "./pages/admin/document/create"
import EditDocumentPage from "./pages/admin/document/edit-document"
import ProcessDocumentPage from "./pages/admin/document/process-document"
import RagEvaluationDashboard from "./pages/admin/rag-evaluation/dashboard"
import RagEvaluationDatasetsPage from "./pages/admin/rag-evaluation/datasets"
import RagEvaluationDatasetUploadPage from "./pages/admin/rag-evaluation/dataset-upload"
import RagEvaluationDatasetDetailPage from "./pages/admin/rag-evaluation/dataset-detail"
import RagEvaluationRunDetailPage from "./pages/admin/rag-evaluation/run-detail"
import UnauthorizedPage from "./pages/unauthorized"
import NewChatPage from "./pages/chat/new-chat"
import DetailChatPage from "./pages/chat/detail-chat"
import { AdminRoute } from "./components/auth/AdminRoute"
import { ProtectedRoute } from "./components/auth/ProtectedRoute"
import { authService } from "@/lib/auth"

function AuthTokenRefresher() {
  useEffect(() => {
    const refreshSession = async () => {
      if (!authService.isAuthenticated()) {
        return
      }

      await authService.refreshToken()
    }

    void refreshSession()

    const intervalId = window.setInterval(() => {
      void refreshSession()
    }, authService.getRefreshIntervalMs())

    const handleVisibilityChange = () => {
      if (document.visibilityState === "visible") {
        void refreshSession()
      }
    }

    window.addEventListener("focus", handleVisibilityChange)
    document.addEventListener("visibilitychange", handleVisibilityChange)

    return () => {
      window.clearInterval(intervalId)
      window.removeEventListener("focus", handleVisibilityChange)
      document.removeEventListener("visibilitychange", handleVisibilityChange)
    }
  }, [])

  return null
}

function App() {
  return (
    <BrowserRouter>
      <AuthTokenRefresher />
      <Routes>
        {/* Public routes */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/unauthorized" element={<UnauthorizedPage />} />

        {/* Protected routes (any authenticated user) */}
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Welcome />
            </ProtectedRoute>
          }
        />

        {/* Chat routes (protected) */}
        <Route
          path="/chat/new"
          element={
            <ProtectedRoute>
              <NewChatPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/chat/:id"
          element={
            <ProtectedRoute>
              <DetailChatPage />
            </ProtectedRoute>
          }
        />

        {/* Admin-only routes with /admin prefix */}
        <Route path="/admin">
          <Route
            path="dashboard"
            element={
              <AdminRoute>
                <Dashboard />
              </AdminRoute>
            }
          />
          <Route
            path="document"
            element={
              <AdminRoute>
                <DocumentListPage />
              </AdminRoute>
            }
          />
          <Route
            path="document/create"
            element={
              <AdminRoute>
                <CreateDocumentPage />
              </AdminRoute>
            }
          />
          <Route
            path="document/edit/:id"
            element={
              <AdminRoute>
                <EditDocumentPage />
              </AdminRoute>
            }
          />
          <Route
            path="document/process"
            element={
              <AdminRoute>
                <ProcessDocumentPage />
              </AdminRoute>
            }
          />
          <Route
            path="user"
            element={
              <AdminRoute>
                <UserListPage />
              </AdminRoute>
            }
          />
          <Route
            path="rag-evaluation"
            element={
              <AdminRoute>
                <RagEvaluationDashboard />
              </AdminRoute>
            }
          />
          <Route
            path="rag-evaluation/datasets"
            element={
              <AdminRoute>
                <RagEvaluationDatasetsPage />
              </AdminRoute>
            }
          />
          <Route
            path="rag-evaluation/datasets/upload"
            element={
              <AdminRoute>
                <RagEvaluationDatasetUploadPage />
              </AdminRoute>
            }
          />
          <Route
            path="rag-evaluation/datasets/:datasetId"
            element={
              <AdminRoute>
                <RagEvaluationDatasetDetailPage />
              </AdminRoute>
            }
          />
          <Route
            path="rag-evaluation/runs/:runId"
            element={
              <AdminRoute>
                <RagEvaluationRunDetailPage />
              </AdminRoute>
            }
          />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
