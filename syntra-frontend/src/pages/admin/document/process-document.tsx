import { type CSSProperties } from "react"
import { IconArrowLeft, IconRefresh } from "@tabler/icons-react"
import { useQuery } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { Button } from "@/components/ui/button"
import { ProcessStatistics, ProcessTable } from "./components"
import { listProcessingDocuments } from "./api"
import type { ProcessMonitorResponse } from "./types"

const PROCESS_MONITOR_REFETCH_INTERVAL_MS = 3000

const EMPTY_PROCESS_MONITOR_RESPONSE: ProcessMonitorResponse = {
  documents: [],
  summary: {
    total: 0,
    processing: 0,
    completed: 0,
    failed: 0,
  },
}

const ProcessDocumentPage = () => {
  const navigate = useNavigate()

  const processingDocumentsQuery = useQuery({
    queryKey: ["documents", "processing-monitor"],
    queryFn: ({ signal }) => listProcessingDocuments({ signal }),
    refetchInterval: PROCESS_MONITOR_REFETCH_INTERVAL_MS,
  })

  const processMonitorData =
    processingDocumentsQuery.data ?? EMPTY_PROCESS_MONITOR_RESPONSE
  const documents = processMonitorData.documents
  const isRefreshing =
    processingDocumentsQuery.isFetching && !processingDocumentsQuery.isPending

  const handleRefresh = () => {
    void processingDocumentsQuery.refetch()
  }

  const errorMessage =
    processingDocumentsQuery.error instanceof Error
      ? processingDocumentsQuery.error.message
      : "Gagal memuat data proses dokumen."

  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "calc(var(--spacing) * 72)",
          "--header-height": "calc(var(--spacing) * 12)",
        } as CSSProperties
      }
    >
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
        <div className="flex flex-1 flex-col">
          <div className="@container/main flex flex-1 flex-col gap-2">
            <div className="flex flex-col gap-6 py-4 md:py-6">
              {/* Page Header */}
              <div className="flex items-center justify-between px-4 lg:px-6">
                <div className="flex items-center gap-3">
                  <Button
                    variant="ghost"
                    size="icon"
                    onClick={() => navigate("/admin/document")}
                  >
                    <IconArrowLeft className="size-5" />
                  </Button>
                  <div>
                    <h1 className="text-2xl font-bold tracking-tight">
                      Process Dokumen
                    </h1>
                    <p className="text-muted-foreground">
                      Monitor progress upload dan pemrosesan dokumen
                    </p>
                  </div>
                </div>
                <Button
                  onClick={handleRefresh}
                  disabled={processingDocumentsQuery.isPending || isRefreshing}
                  variant="outline"
                >
                  <IconRefresh
                    className={`size-4 ${isRefreshing ? "animate-spin" : ""}`}
                  />
                  Refresh
                </Button>
              </div>

              {processingDocumentsQuery.isError && (
                <div className="px-4 lg:px-6">
                  <div className="rounded-md bg-destructive/10 p-3 text-sm text-destructive">
                    {errorMessage}
                  </div>
                </div>
              )}

              {/* Statistics Cards */}
              <ProcessStatistics documents={documents} />

              {/* Process Table */}
              <ProcessTable documents={documents} />
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}

export default ProcessDocumentPage
