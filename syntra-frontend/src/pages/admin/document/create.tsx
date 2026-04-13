import {
  type CSSProperties,
  type ChangeEvent,
  type DragEvent,
  useCallback,
  useRef,
  useState,
} from "react"
import { useMutation } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import { IconArrowLeft, IconCheck, IconLoader } from "@tabler/icons-react"
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { Button } from "@/components/ui/button"
import { FileUploadArea, UploadedFilesList } from "./components"
import { uploadDocumentsBulk } from "./api"
import { createUploadedFile } from "./utils"
import type { UploadedFile } from "./types"

const PROCESS_DOCUMENT_ROUTE = "/admin/document/process"

const isPdfFile = (file: File): boolean =>
  file.type === "application/pdf" || file.name.toLowerCase().endsWith(".pdf")

interface UploadDocumentsVariables {
  files: UploadedFile[]
}

const CreateDocumentPage = () => {
  const navigate = useNavigate()
  const fileInputRef = useRef<HTMLInputElement>(null)
  const [uploadedFiles, setUploadedFiles] = useState<UploadedFile[]>([])
  const [isDragging, setIsDragging] = useState(false)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const uploadDocumentsMutation = useMutation({
    mutationFn: async ({ files }: UploadDocumentsVariables) =>
      uploadDocumentsBulk({ files: files.map((uploadedFile) => uploadedFile.file) }),
    onMutate: ({ files }) => {
      const selectedIds = new Set(files.map((uploadedFile) => uploadedFile.id))

      setErrorMessage(null)
      setUploadedFiles((previousFiles) =>
        previousFiles.map((uploadedFile) =>
          selectedIds.has(uploadedFile.id)
            ? {
                ...uploadedFile,
                status: "uploading",
                progress: 50,
                errorMessage: undefined,
              }
            : uploadedFile
        )
      )
    },
    onSuccess: (response, { files }) => {
      const selectedIds = new Set(files.map((uploadedFile) => uploadedFile.id))
      const resultByFileId = new Map(
        files.map((uploadedFile, index) => [uploadedFile.id, response.results[index]])
      )

      setUploadedFiles((previousFiles) =>
        previousFiles.map((uploadedFile) => {
          if (!selectedIds.has(uploadedFile.id)) {
            return uploadedFile
          }

          const result = resultByFileId.get(uploadedFile.id)
          if (!result) {
            return {
              ...uploadedFile,
              status: "error",
              progress: 0,
              errorMessage: "Respon server tidak valid.",
            }
          }

          if (result.status === "processing") {
            return {
              ...uploadedFile,
              status: "success",
              progress: 100,
              errorMessage: undefined,
            }
          }

          return {
            ...uploadedFile,
            status: "error",
            progress: 0,
            errorMessage: result.error ?? "Gagal mengunggah dokumen.",
          }
        })
      )

      if (response.processingCount > 0) {
        navigate(PROCESS_DOCUMENT_ROUTE)
        return
      }

      setErrorMessage("Semua dokumen gagal diunggah. Silakan coba lagi.")
    },
    onError: (error, { files }) => {
      const selectedIds = new Set(files.map((uploadedFile) => uploadedFile.id))
      const fallbackMessage =
        error instanceof Error
          ? error.message
          : "Terjadi kesalahan saat mengunggah dokumen."

      setUploadedFiles((previousFiles) =>
        previousFiles.map((uploadedFile) =>
          selectedIds.has(uploadedFile.id)
            ? {
                ...uploadedFile,
                status: "error",
                progress: 0,
                errorMessage: fallbackMessage,
              }
            : uploadedFile
        )
      )
      setErrorMessage(fallbackMessage)
    },
  })

  const handleFileSelect = useCallback((files: FileList | null) => {
    if (!files) return

    const selectedFiles = Array.from(files)
    const pdfFiles = selectedFiles.filter(isPdfFile)
    const invalidFileCount = selectedFiles.length - pdfFiles.length

    if (pdfFiles.length > 0) {
      setUploadedFiles((previousFiles) => [
        ...previousFiles,
        ...pdfFiles.map(createUploadedFile),
      ])
    }

    if (invalidFileCount > 0) {
      setErrorMessage(
        `${invalidFileCount} file diabaikan karena hanya format PDF yang didukung.`
      )
      return
    }

    setErrorMessage(null)
  }, [])

  const handleFileInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    handleFileSelect(event.target.files)
    event.target.value = ""
  }

  const handleRemoveFile = useCallback((id: string) => {
    setUploadedFiles((previousFiles) =>
      previousFiles.filter((uploadedFile) => uploadedFile.id !== id)
    )
  }, [])

  const handleDragOver = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault()
    setIsDragging(true)
  }

  const handleDragLeave = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault()
    setIsDragging(false)
  }

  const handleDrop = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault()
    setIsDragging(false)
    handleFileSelect(event.dataTransfer.files)
  }

  const handleSubmit = () => {
    if (uploadedFiles.length === 0) {
      setErrorMessage("Harap pilih minimal 1 dokumen.")
      return
    }

    const filesToUpload = uploadedFiles.filter(
      (uploadedFile) => uploadedFile.status !== "success"
    )
    if (filesToUpload.length === 0) {
      navigate(PROCESS_DOCUMENT_ROUTE)
      return
    }

    uploadDocumentsMutation.mutate({ files: filesToUpload })
  }

  const isSubmitting = uploadDocumentsMutation.isPending

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
                      Upload Dokumen
                    </h1>
                    <p className="text-muted-foreground">
                      Upload dokumen baru ke dalam sistem
                    </p>
                  </div>
                </div>
              </div>

              {/* Main Content */}
              <div className="px-4 lg:px-6">
                <div className="mx-auto max-w-3xl space-y-6">
                  {/* Upload Area */}
                  <FileUploadArea
                    fileInputRef={fileInputRef}
                    isDragging={isDragging}
                    onFileInputChange={handleFileInputChange}
                    onDragOver={handleDragOver}
                    onDragLeave={handleDragLeave}
                    onDrop={handleDrop}
                  />

                  {/* Uploaded Files List */}
                  <UploadedFilesList
                    uploadedFiles={uploadedFiles}
                    onRemoveFile={handleRemoveFile}
                  />

                  {errorMessage && (
                    <div className="rounded-md bg-destructive/10 p-3 text-sm text-destructive">
                      {errorMessage}
                    </div>
                  )}

                  {/* Actions */}
                  <div className="flex items-center justify-between gap-4">
                    <Button
                      variant="outline"
                      onClick={() => navigate("/admin/document")}
                      disabled={isSubmitting}
                    >
                      Batal
                    </Button>

                    <div className="flex items-center gap-2">
                      <Button
                        onClick={handleSubmit}
                        disabled={uploadedFiles.length === 0 || isSubmitting}
                      >
                        {isSubmitting ? (
                          <>
                            <IconLoader className="size-4 animate-spin" />
                            Menyimpan Dokumen...
                          </>
                        ) : (
                          <>
                            <IconCheck className="size-4" />
                            Simpan Dokumen
                          </>
                        )}
                      </Button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}

export default CreateDocumentPage
