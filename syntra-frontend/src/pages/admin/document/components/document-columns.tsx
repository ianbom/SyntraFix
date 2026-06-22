import { type ColumnDef } from "@tanstack/react-table"
import {
  IconEye,
  IconEdit,
  IconTrash,
  IconDotsVertical,
} from "@tabler/icons-react"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import type { DocumentListItem } from "../types"
import { Link } from "react-router-dom"
import { getDocumentDownloadUrl } from "../api"

interface DocumentColumnsOptions {
  deletingDocumentId?: number | null
  onDeleteDocument?: (document: DocumentListItem) => void
}

const formatDate = (dateStr: string | null): string => {
  if (!dateStr) return "-"
  return new Date(dateStr).toLocaleDateString("id-ID", {
    year: "numeric",
    month: "short",
    day: "numeric",
  })
}

const typeLabels: Record<DocumentListItem["type"], string> = {
  journal: "Journal",
  conference: "Conference",
  thesis: "Thesis",
  report: "Report",
  book: "Book",
}

const getTypeBadge = (type: DocumentListItem["type"]) => (
  <Badge variant="secondary">{typeLabels[type]}</Badge>
)

const getVisibilityBadge = (isPrivate: boolean) => (
  <Badge variant={isPrivate ? "outline" : "default"}>
    {isPrivate ? "Private" : "Public"}
  </Badge>
)

const openDocumentPreview = async (documentId: number) => {
  const previewWindow = window.open("about:blank", "_blank")

  if (!previewWindow) {
    window.alert("Popup diblokir browser. Izinkan pop-up untuk membuka dokumen.")
    return
  }

  try {
    const { downloadUrl } = await getDocumentDownloadUrl({ documentId })

    previewWindow.location.replace(downloadUrl)
    previewWindow.opener = null
    previewWindow.focus()
  } catch (error: unknown) {
    previewWindow.close()

    window.alert(
      error instanceof Error ? error.message : "Gagal membuka dokumen."
    )
  }
}

export const createDocumentColumns = ({
  deletingDocumentId = null,
  onDeleteDocument,
}: DocumentColumnsOptions = {}): ColumnDef<DocumentListItem>[] => [
  {
    accessorKey: "title",
    header: "Title",
    cell: ({ row }) => (
      <div className="max-w-[300px]">
        <p className="font-medium truncate">{row.original.title}</p>
      </div>
    ),
  },
  {
    accessorKey: "creator",
    header: "Creator",
    cell: ({ row }) => (
      <span className="text-sm">{row.original.creator?.trim() || "-"}</span>
    ),
  },
  {
    accessorKey: "type",
    header: "Tipe",
    cell: ({ row }) => getTypeBadge(row.original.type),
  },
  {
    accessorKey: "doi",
    header: "DOI",
    cell: ({ row }) => (
      <span className="text-sm text-muted-foreground">
        {row.original.doi || "-"}
      </span>
    ),
  },
  {
    accessorKey: "isPrivate",
    header: "Visibilitas",
    cell: ({ row }) => getVisibilityBadge(row.original.isPrivate),
  },
  {
    accessorKey: "publishedAt",
    header: "Dipublish Pada",
    cell: ({ row }) => (
      <span className="text-sm">{formatDate(row.original.publishedAt)}</span>
    ),
  },
  {
    accessorKey: "createdAt",
    header: "Dibuat Pada",
    cell: ({ row }) => (
      <span className="text-sm">{formatDate(row.original.createdAt)}</span>
    ),
  },
  {
    id: "actions",
    header: "Action",
    cell: ({ row }) => {
      const document = row.original
      const isDeleting = deletingDocumentId === document.id

      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" size="icon-sm" disabled={isDeleting}>
              <IconDotsVertical className="size-4" />
              <span className="sr-only">Buka menu</span>
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuItem
              disabled={isDeleting}
              onClick={() => void openDocumentPreview(document.id)}
            >
              <IconEye className="size-4" />
              Lihat
            </DropdownMenuItem>
            <DropdownMenuItem asChild disabled={isDeleting}>
              <Link to={`/admin/document/edit/${document.id}`}>
                <IconEdit className="size-4 mr-2" />
                <span>Edit</span>
              </Link>
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem
              variant="destructive"
              disabled={isDeleting || !onDeleteDocument}
              onClick={() => onDeleteDocument?.(document)}
            >
              <IconTrash className="size-4" />
              {isDeleting ? "Menghapus..." : "Hapus"}
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      )
    },
    enableSorting: false,
  },
]

export const columns = createDocumentColumns()
