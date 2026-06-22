import { useMemo, useState } from "react"
import {
  IconSearch,
  IconArrowUp,
  IconArrowDown,
  IconX,
} from "@tabler/icons-react"
import {
  useReactTable,
  getCoreRowModel,
  getSortedRowModel,
  flexRender,
  type SortingState,
} from "@tanstack/react-table"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import {
  Pagination,
  PaginationContent,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
import { createDocumentColumns } from "./document-columns"
import type { DocumentListItem } from "../types"

interface DocumentTableProps {
  documents: DocumentListItem[]
  search: string
  page: number
  pages: number
  perPage: number
  total: number
  isLoading: boolean
  deletingDocumentId?: number | null
  onSearchChange: (value: string) => void
  onPageChange: (page: number) => void
  onPerPageChange: (perPage: number) => void
  onDeleteDocument?: (document: DocumentListItem) => void
}

export function DocumentTable({
  documents,
  search,
  page,
  pages,
  perPage,
  total,
  isLoading,
  deletingDocumentId = null,
  onSearchChange,
  onPageChange,
  onPerPageChange,
  onDeleteDocument,
}: DocumentTableProps) {
  const [sorting, setSorting] = useState<SortingState>([])
  const columns = useMemo(
    () =>
      createDocumentColumns({
        deletingDocumentId,
        onDeleteDocument,
      }),
    [deletingDocumentId, onDeleteDocument]
  )

  const table = useReactTable({
    data: documents,
    columns,
    state: {
      sorting,
    },
    onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  })

  const pageCount = Math.max(pages, 1)
  const pageNumbers = useMemo(
    () => Array.from({ length: pageCount }, (_, index) => index + 1),
    [pageCount]
  )

  const showingText = useMemo(() => {
    if (total === 0) {
      return "Menampilkan 0 dari 0 dokumen"
    }

    const start = (page - 1) * perPage + 1
    const end = Math.min(page * perPage, total)

    return `Menampilkan ${start} - ${end} dari ${total} dokumen`
  }, [page, perPage, total])

  return (
    <div className="space-y-4 px-4 lg:px-6">
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex flex-1 items-center gap-2">
          <div className="relative flex-1 max-w-sm">
            <IconSearch className="absolute left-3 top-1/2 size-4 -translate-y-1/2 text-muted-foreground" />
            <Input
              placeholder="Cari dokumen..."
              value={search}
              onChange={(event) => onSearchChange(event.target.value)}
              className="pl-9"
            />
            {search && (
              <Button
                variant="ghost"
                size="icon-xs"
                className="absolute right-1 top-1/2 -translate-y-1/2"
                onClick={() => onSearchChange("")}
              >
                <IconX className="size-3" />
              </Button>
            )}
          </div>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-sm text-muted-foreground">Rows per page:</span>
          <Select
            value={String(perPage)}
            onValueChange={(value) => onPerPageChange(Number(value))}
          >
            <SelectTrigger className="w-[70px]" size="sm">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {[5, 10, 20, 50].map((size) => (
                <SelectItem key={size} value={String(size)}>
                  {size}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
      </div>

      <div className="rounded-lg border">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map((headerGroup) => (
              <TableRow key={headerGroup.id}>
                {headerGroup.headers.map((header) => (
                  <TableHead key={header.id}>
                    {header.isPlaceholder ? null : (
                      <div
                        className={
                          header.column.getCanSort()
                            ? "flex cursor-pointer select-none items-center gap-1"
                            : ""
                        }
                        onClick={header.column.getToggleSortingHandler()}
                      >
                        {flexRender(
                          header.column.columnDef.header,
                          header.getContext()
                        )}
                        {header.column.getCanSort() && (
                          <span className="ml-1">
                            {{
                              asc: <IconArrowUp className="size-3" />,
                              desc: <IconArrowDown className="size-3" />,
                            }[header.column.getIsSorted() as string] ?? (
                              <span className="size-3 opacity-0 group-hover:opacity-50">
                                ↕
                              </span>
                            )}
                          </span>
                        )}
                      </div>
                    )}
                  </TableHead>
                ))}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {isLoading ? (
              <TableRow>
                <TableCell colSpan={columns.length} className="h-24 text-center">
                  Memuat dokumen...
                </TableCell>
              </TableRow>
            ) : table.getRowModel().rows.length ? (
              table.getRowModel().rows.map((row) => (
                <TableRow key={row.id}>
                  {row.getVisibleCells().map((cell) => (
                    <TableCell key={cell.id}>
                      {flexRender(
                        cell.column.columnDef.cell,
                        cell.getContext()
                      )}
                    </TableCell>
                  ))}
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell
                  colSpan={columns.length}
                  className="h-24 text-center"
                >
                  Tidak ada dokumen ditemukan.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>

      <div className="flex items-center justify-between">
        <p className="text-sm text-muted-foreground">{showingText}</p>

        <Pagination>
          <PaginationContent>
            <PaginationItem>
              <PaginationPrevious
                onClick={() => onPageChange(page - 1)}
                className={
                  page <= 1
                    ? "pointer-events-none opacity-50"
                    : "cursor-pointer"
                }
              />
            </PaginationItem>

            {pageNumbers.map((pageNumber) => (
              <PaginationItem key={pageNumber}>
                <PaginationLink
                  onClick={() => onPageChange(pageNumber)}
                  isActive={pageNumber === page}
                  className="cursor-pointer"
                >
                  {pageNumber}
                </PaginationLink>
              </PaginationItem>
            ))}

            <PaginationItem>
              <PaginationNext
                onClick={() => onPageChange(page + 1)}
                className={
                  page >= pageCount
                    ? "pointer-events-none opacity-50"
                    : "cursor-pointer"
                }
              />
            </PaginationItem>
          </PaginationContent>
        </Pagination>
      </div>
    </div>
  )
}
