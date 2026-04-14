import { IconFilePencil } from "@tabler/icons-react"
import { keepPreviousData, useQuery } from "@tanstack/react-query"
import { type CSSProperties, useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { Button } from "@/components/ui/button"
import { DocumentStatistics, DocumentTable } from "./components"
import { listDocuments } from "./api"
import type { DocumentListResponse } from "./types"

const DEFAULT_PER_PAGE = 10
const SEARCH_DEBOUNCE_MS = 400
const CREATE_DOCUMENT_ROUTE = "/admin/document/create"


const createEmptyDocumentsResponse = (perPage: number): DocumentListResponse => ({
  documents: [],
  total: 0,
  page: 1,
  perPage,
  pages: 1,
})

const DocumentListPage = () => {
  const [page, setPage] = useState(1)
  const [perPage, setPerPage] = useState(DEFAULT_PER_PAGE)
  const [searchInput, setSearchInput] = useState("")
  const [search, setSearch] = useState("")

  useEffect(() => {
    const timeoutId = window.setTimeout(() => {
      setSearch(searchInput.trim())
    }, SEARCH_DEBOUNCE_MS)

    return () => {
      window.clearTimeout(timeoutId)
    }
  }, [searchInput])

  const documentsQuery = useQuery({
    queryKey: ["documents", "list", page, perPage, search],
    queryFn: ({ signal }) =>
      listDocuments({
        page,
        perPage,
        search,
        signal,
      }),
    placeholderData: keepPreviousData,
  })

  const documentsData = documentsQuery.data ?? createEmptyDocumentsResponse(perPage)
  const pages = Math.max(documentsData.pages, 1)

  const handleSearchChange = (value: string) => {
    setSearchInput(value)
    setPage(1)
  }

  const handlePerPageChange = (value: number) => {
    setPerPage(value)
    setPage(1)
  }

  const handlePageChange = (nextPage: number) => {
    const clampedPage = Math.min(Math.max(nextPage, 1), pages)
    setPage(clampedPage)
  }

  const errorMessage =
    documentsQuery.error instanceof Error
      ? documentsQuery.error.message
      : "Gagal memuat daftar dokumen."

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
                <div>
                  <h1 className="text-2xl font-bold tracking-tight">
                    Daftar Dokumen
                  </h1>
                  <p className="text-muted-foreground">
                    Kelola semua dokumen yang ada di sistem
                  </p>
                </div>
                <Button asChild>
                  <Link to={CREATE_DOCUMENT_ROUTE}>
                    <IconFilePencil className="size-4" />
                    Tambah Dokumen
                  </Link>
                </Button>
              </div>

              {documentsQuery.isError && (
                <div className="px-4 lg:px-6">
                  <div className="rounded-md bg-destructive/10 p-3 text-sm text-destructive">
                    {errorMessage}
                  </div>
                </div>
              )}

              {/* Statistics Cards */}
              <DocumentStatistics
                documents={documentsData.documents}
                totalDocuments={documentsData.total}
              />

              {/* Documents Table */}
              <DocumentTable
                documents={documentsData.documents}
                search={searchInput}
                page={Math.min(documentsData.page, pages)}
                pages={documentsData.pages}
                perPage={documentsData.perPage}
                total={documentsData.total}
                isLoading={documentsQuery.isPending}
                onSearchChange={handleSearchChange}
                onPageChange={handlePageChange}
                onPerPageChange={handlePerPageChange}
              />
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}

export default DocumentListPage
