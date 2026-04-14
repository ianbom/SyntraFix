import { IconArrowLeft, IconDeviceFloppy, IconLoader } from "@tabler/icons-react"
import { useQuery } from "@tanstack/react-query"
import { type CSSProperties, type ReactNode, useEffect, useMemo, useState } from "react"
import { Link, useParams } from "react-router-dom"
import { toast } from "sonner"
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { getDocumentDetail } from "./api"
import { DocumentChunksEditor } from "./components/document-chunks-editor"
import { DocumentEditForm } from "./components/document-edit-form"
import type { DocumentChunk, DocumentDetail } from "./edit-types"

const DOCUMENT_LIST_ROUTE = "/admin/document"

const pageLayoutStyle = {
  "--sidebar-width": "calc(var(--spacing) * 72)",
  "--header-height": "calc(var(--spacing) * 12)",
} as CSSProperties

function DocumentPageShell({ children }: { children: ReactNode }) {
  return (
    <SidebarProvider style={pageLayoutStyle}>
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
        {children}
      </SidebarInset>
    </SidebarProvider>
  )
}

interface DocumentStateCardProps {
  title: string
  description: string
  actionLabel: string
}

function DocumentStateCard({
  title,
  description,
  actionLabel,
}: DocumentStateCardProps) {
  return (
    <div className="flex flex-1 items-center justify-center p-4">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle>{title}</CardTitle>
          <CardDescription>{description}</CardDescription>
        </CardHeader>
        <CardContent>
          <Link to={DOCUMENT_LIST_ROUTE}>
            <Button>
              <IconArrowLeft className="mr-2 size-4" />
              {actionLabel}
            </Button>
          </Link>
        </CardContent>
      </Card>
    </div>
  )
}

const EditDocumentPage = () => {
  const { id } = useParams<{ id: string }>()
  const [document, setDocument] = useState<DocumentDetail | null>(null)
  const [isSaving, setIsSaving] = useState(false)

  const documentId = useMemo(() => Number(id), [id])
  const hasValidDocumentId = Number.isInteger(documentId) && documentId > 0

  const documentQuery = useQuery({
    queryKey: ["documents", "detail", documentId],
    queryFn: ({ signal }) => getDocumentDetail({ documentId, signal }),
    enabled: hasValidDocumentId,
    refetchOnWindowFocus: false,
  })

  useEffect(() => {
    if (documentQuery.data) {
      setDocument(documentQuery.data)
    }
  }, [documentQuery.data])

  useEffect(() => {
    if (!hasValidDocumentId) {
      setDocument(null)
    }
  }, [hasValidDocumentId])

  const handleUpdateDocument = (updates: Partial<DocumentDetail>) => {
    setDocument((prevDocument) => {
      if (!prevDocument) {
        return prevDocument
      }

      return {
        ...prevDocument,
        ...updates,
      }
    })
  }

  const handleUpdateChunk = (
    chunkId: number,
    updates: Partial<DocumentChunk>
  ) => {
    setDocument((prevDocument) => {
      if (!prevDocument) {
        return prevDocument
      }

      const updatedChunks = prevDocument.chunks.map((chunk) =>
        chunk.id === chunkId ? { ...chunk, ...updates } : chunk
      )

      return {
        ...prevDocument,
        chunks: updatedChunks,
        chunk_count: updatedChunks.length,
      }
    })
  }

  const handleDeleteChunk = (chunkId: number) => {
    setDocument((prevDocument) => {
      if (!prevDocument) {
        return prevDocument
      }

      const updatedChunks = prevDocument.chunks.filter(
        (chunk) => chunk.id !== chunkId
      )

      return {
        ...prevDocument,
        chunks: updatedChunks,
        chunk_count: updatedChunks.length,
      }
    })

    toast.success("Chunk deleted successfully")
  }

  const handleSave = async () => {
    if (!document) {
      return
    }

    setIsSaving(true)
    try {
      await new Promise((resolve) => setTimeout(resolve, 600))
      toast.success("Perubahan lokal berhasil disimpan")
    } catch {
      toast.error("Gagal menyimpan perubahan")
    } finally {
      setIsSaving(false)
    }
  }

  const isInitialLoading = hasValidDocumentId && documentQuery.isPending && !document
  const errorMessage =
    documentQuery.error instanceof Error
      ? documentQuery.error.message
      : "Dokumen gagal dimuat."

  if (isInitialLoading) {
    return (
      <DocumentPageShell>
        <div className="flex flex-1 items-center justify-center">
          <div className="flex items-center gap-2 text-muted-foreground">
            <IconLoader className="size-5 animate-spin" />
            <span>Loading document...</span>
          </div>
        </div>
      </DocumentPageShell>
    )
  }

  if (!hasValidDocumentId) {
    return (
      <DocumentPageShell>
        <DocumentStateCard
          title="Document Not Found"
          description="ID dokumen tidak valid."
          actionLabel="Back to Documents"
        />
      </DocumentPageShell>
    )
  }

  if (documentQuery.isError && !document) {
    return (
      <DocumentPageShell>
        <DocumentStateCard
          title="Failed to Load Document"
          description={errorMessage}
          actionLabel="Back to Documents"
        />
      </DocumentPageShell>
    )
  }

  if (!document) {
    return (
      <DocumentPageShell>
        <DocumentStateCard
          title="Document Not Found"
          description="The document you're looking for doesn't exist or has been deleted."
          actionLabel="Back to Documents"
        />
      </DocumentPageShell>
    )
  }

  return (
    <DocumentPageShell>
      <div className="flex flex-1 flex-col">
        <div className="@container/main flex flex-1 flex-col gap-2">
          <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
            <div className="flex items-center justify-between px-4 lg:px-6">
              <div className="flex items-center gap-4">
                <Link to={DOCUMENT_LIST_ROUTE}>
                  <Button variant="ghost" size="icon">
                    <IconArrowLeft className="size-5" />
                  </Button>
                </Link>
                <div>
                  <h1 className="text-2xl font-bold tracking-tight">
                    Edit Document #{document.id}
                  </h1>
                  <p className="text-muted-foreground">
                    Modify document metadata and chunks
                  </p>
                  {documentQuery.isFetching && (
                    <p className="mt-1 text-xs text-muted-foreground">
                      Memperbarui data dari server...
                    </p>
                  )}
                </div>
              </div>
              <Button onClick={handleSave} disabled={isSaving}>
                {isSaving ? (
                  <>
                    <IconLoader className="mr-2 size-4 animate-spin" />
                    Saving...
                  </>
                ) : (
                  <>
                    <IconDeviceFloppy className="mr-2 size-4" />
                    Save Changes
                  </>
                )}
              </Button>
            </div>

            <div className="space-y-6 px-4 lg:px-6">
              <DocumentEditForm document={document} onUpdate={handleUpdateDocument} />

              <DocumentChunksEditor
                chunks={document.chunks}
                onUpdateChunk={handleUpdateChunk}
                onDeleteChunk={handleDeleteChunk}
              />
            </div>
          </div>
        </div>
      </div>
    </DocumentPageShell>
  )
}

export default EditDocumentPage
