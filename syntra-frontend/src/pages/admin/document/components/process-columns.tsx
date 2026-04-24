import { type ColumnDef } from "@tanstack/react-table"
import { IconArrowUp, IconArrowDown } from "@tabler/icons-react"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import type { ProcessDocument } from "../types"

interface ProcessColumnsOptions {
  generatingDocumentId?: string | null
  onGenerateQuestions?: (document: ProcessDocument) => void
}

const formatDate = (dateStr: string): string => {
  return new Date(dateStr).toLocaleDateString("id-ID", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  })
}

const getStatusBadge = (status: ProcessDocument["status"]) => {
  switch (status) {
    case "processing":
      return <Badge variant="default">Processing</Badge>
    case "completed":
      return <Badge variant="default" className="bg-green-500">Completed</Badge>
    case "failed":
      return <Badge variant="destructive">Failed</Badge>
  }
}

const ProgressBar = ({ progress }: { progress: number }) => {
  const getProgressColor = () => {
    if (progress >= 100) return "bg-green-500"
    if (progress >= 70) return "bg-blue-500"
    if (progress >= 40) return "bg-yellow-500"
    return "bg-red-500"
  }

  return (
    <div className="flex items-center gap-2 min-w-[150px]">
      <div className="flex-1 h-2 overflow-hidden rounded-full bg-secondary">
        <div
          className={`h-full transition-all duration-300 ${getProgressColor()}`}
          style={{ width: `${progress}%` }}
        />
      </div>
      <span className="text-sm font-medium tabular-nums w-12 text-right">
        {progress}%
      </span>
    </div>
  )
}

const PossiblyQuestionStatus = ({ document }: { document: ProcessDocument }) => {
  const isComplete =
    document.chunkCount === 0 ||
    document.possiblyQuestionCount >= document.chunkCount
  const isEmpty = document.possiblyQuestionCount === 0 && document.chunkCount > 0

  return (
    <div className="flex min-w-[140px] flex-col gap-1">
      <span className="text-sm font-medium tabular-nums">
        {document.possiblyQuestionCount} / {document.chunkCount}
      </span>
      <Badge
        variant={isComplete ? "default" : isEmpty ? "secondary" : "outline"}
        className={
          isComplete
            ? "w-fit bg-green-500"
            : isEmpty
              ? "w-fit"
              : "w-fit border-yellow-500 text-yellow-700"
        }
      >
        {isComplete ? "Complete" : isEmpty ? "Belum Generate" : "Partial"}
      </Badge>
    </div>
  )
}

export const createProcessColumns = ({
  generatingDocumentId = null,
  onGenerateQuestions,
}: ProcessColumnsOptions = {}): ColumnDef<ProcessDocument>[] => [
  {
    accessorKey: "title",
    header: ({ column }) => {
      return (
        <div
          className="flex cursor-pointer select-none items-center gap-1"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Title
          <span className="ml-1">
            {column.getIsSorted() === "asc" ? (
              <IconArrowUp className="size-3" />
            ) : column.getIsSorted() === "desc" ? (
              <IconArrowDown className="size-3" />
            ) : (
              <span className="size-3 opacity-0">↕</span>
            )}
          </span>
        </div>
      )
    },
    cell: ({ row }) => (
      <div className="max-w-[300px]">
        <p className="font-medium truncate">{row.original.title}</p>
      </div>
    ),
  },
  {
    accessorKey: "creator",
    header: ({ column }) => {
      return (
        <div
          className="flex cursor-pointer select-none items-center gap-1"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Creator
          <span className="ml-1">
            {column.getIsSorted() === "asc" ? (
              <IconArrowUp className="size-3" />
            ) : column.getIsSorted() === "desc" ? (
              <IconArrowDown className="size-3" />
            ) : (
              <span className="size-3 opacity-0">↕</span>
            )}
          </span>
        </div>
      )
    },
    cell: ({ row }) => <span className="text-sm">{row.original.creator}</span>,
  },
  {
    accessorKey: "uploadedAt",
    header: ({ column }) => {
      return (
        <div
          className="flex cursor-pointer select-none items-center gap-1"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Diupload Pada
          <span className="ml-1">
            {column.getIsSorted() === "asc" ? (
              <IconArrowUp className="size-3" />
            ) : column.getIsSorted() === "desc" ? (
              <IconArrowDown className="size-3" />
            ) : (
              <span className="size-3 opacity-0">↕</span>
            )}
          </span>
        </div>
      )
    },
    cell: ({ row }) => (
      <span className="text-sm">{formatDate(row.original.uploadedAt)}</span>
    ),
  },
  {
    accessorKey: "progress",
    header: ({ column }) => {
      return (
        <div
          className="flex cursor-pointer select-none items-center gap-1"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Progress
          <span className="ml-1">
            {column.getIsSorted() === "asc" ? (
              <IconArrowUp className="size-3" />
            ) : column.getIsSorted() === "desc" ? (
              <IconArrowDown className="size-3" />
            ) : (
              <span className="size-3 opacity-0">↕</span>
            )}
          </span>
        </div>
      )
    },
    cell: ({ row }) => <ProgressBar progress={row.original.progress} />,
  },
  {
    accessorKey: "status",
    header: "Status",
    cell: ({ row }) => getStatusBadge(row.original.status),
    enableSorting: false,
  },
  {
    accessorKey: "possiblyQuestionCount",
    header: "Possibly Question",
    cell: ({ row }) => <PossiblyQuestionStatus document={row.original} />,
  },
  {
    id: "actions",
    header: "Action",
    cell: ({ row }) => {
      const document = row.original
      const isGenerating = generatingDocumentId === document.id
      const canGenerate =
        document.status === "completed" &&
        document.chunkCount > 0 &&
        document.possiblyQuestionCount < document.chunkCount

      return (
        <Button
          variant="outline"
          size="sm"
          disabled={!canGenerate || isGenerating || !onGenerateQuestions}
          onClick={() => onGenerateQuestions?.(document)}
        >
          {isGenerating ? "Generating..." : "Generate Question"}
        </Button>
      )
    },
    enableSorting: false,
  },
]

export const processColumns = createProcessColumns()
