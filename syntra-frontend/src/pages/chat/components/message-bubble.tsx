import { useState, useMemo } from "react"
import { IconUser, IconRobot, IconFileText, IconChevronDown, IconChevronUp, IconExternalLink } from "@tabler/icons-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { getDocumentDownloadUrl } from "../api"
import type { Message, DocumentReference } from "../types"

interface MessageBubbleProps {
  message: Message
}

const formatTime = (date: Date): string => {
  return date.toLocaleTimeString("id-ID", {
    hour: "2-digit",
    minute: "2-digit",
  })
}

function GroupedReferenceCard({ title, references }: { title: string, references: DocumentReference[] }) {
  const [isOpeningDocument, setIsOpeningDocument] = useState(false)
  const [openDocumentErrorMessage, setOpenDocumentErrorMessage] = useState<string | null>(null)

  const handleOpenDocument = async () => {
    if (isOpeningDocument) {
      return
    }

    setOpenDocumentErrorMessage(null)
    const previewWindow = window.open("about:blank", "_blank")

    if (!previewWindow) {
      setOpenDocumentErrorMessage("Popup diblokir browser. Izinkan pop-up untuk membuka dokumen.")
      return
    }

    setIsOpeningDocument(true)

    try {
      const { downloadUrl } = await getDocumentDownloadUrl({
        documentUrl: references[0].documentUrl,
      })

      previewWindow.location.replace(downloadUrl)
      previewWindow.opener = null
      previewWindow.focus()
    } catch (error: unknown) {
      previewWindow.close()

      if (error instanceof Error) {
        setOpenDocumentErrorMessage(error.message)
        return
      }

      setOpenDocumentErrorMessage("Gagal membuka dokumen.")
    } finally {
      setIsOpeningDocument(false)
    }
  }

  return (
    <div className="flex flex-col gap-2 rounded-lg border bg-card p-3 text-card-foreground shadow-sm">
      <div className="flex items-start gap-2">
        <div className="flex size-8 shrink-0 items-center justify-center rounded-md bg-primary/10">
          <IconFileText className="size-4 text-primary" />
        </div>
        <div className="flex-1 min-w-0">
          <h4 className="font-medium text-sm line-clamp-2">{title}</h4>
          <p className="text-xs text-muted-foreground">{references.length} cuplikan ditemukan</p>
        </div>
      </div>
      
      <div className="flex flex-col gap-2 mt-2">
        {references.map((ref, idx) => (
          <div key={ref.id || idx} className="bg-muted/50 rounded-md p-2">
            <p className="text-xs font-medium text-foreground mb-1">
              Halaman {ref.pageNumber}
            </p>
            <p className="text-xs text-muted-foreground line-clamp-4 italic border-l-2 border-primary/30 pl-2">
              "{ref.excerpt}"
            </p>
          </div>
        ))}
      </div>

      <Button
        variant="outline"
        size="sm"
        className="w-full mt-2"
        onClick={handleOpenDocument}
        disabled={isOpeningDocument}
      >
        <IconExternalLink className="size-3.5 mr-1.5" />
        {isOpeningDocument ? "Membuka dokumen..." : "Lihat Dokumen"}
      </Button>
      {openDocumentErrorMessage && (
        <p className="text-xs text-destructive mt-1" role="alert">
          {openDocumentErrorMessage}
        </p>
      )}
    </div>
  )
}

function DocumentReferences({ references }: { references: DocumentReference[] }) {
  const [isExpanded, setIsExpanded] = useState(false)

  const groupedReferences = useMemo(() => {
    return references.reduce((acc, ref) => {
      const key = ref.title || 'Dokumen Tidak Diketahui';
      if (!acc[key]) {
        acc[key] = [];
      }
      acc[key].push(ref);
      return acc;
    }, {} as Record<string, DocumentReference[]>);
  }, [references]);

  const documentCount = Object.keys(groupedReferences).length;

  return (
    <div className="mt-2">
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground transition-colors mb-2"
      >
        {isExpanded ? (
          <IconChevronUp className="size-3.5" />
        ) : (
          <IconChevronDown className="size-3.5" />
        )}
        <span>Referensi ({documentCount} dokumen, {references.length} cuplikan)</span>
      </button>
      {isExpanded && (
        <div className="grid gap-2">
          {Object.entries(groupedReferences).map(([title, refs]) => (
            <GroupedReferenceCard key={title} title={title} references={refs} />
          ))}
        </div>
      )}
    </div>
  )
}

export function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === "user"
  const hasReferences = !isUser && message.references && message.references.length > 0

  return (
    <div
      className={cn(
        "flex gap-3",
        isUser ? "ml-auto max-w-[85%] flex-row-reverse" : "mr-auto max-w-[95%]"
      )}
    >
      <div
        className={cn(
          "flex size-8 shrink-0 items-center justify-center rounded-full",
          isUser ? "bg-primary text-primary-foreground" : "bg-muted"
        )}
      >
        {isUser ? (
          <IconUser className="size-4" />
        ) : (
          <IconRobot className="size-4" />
        )}
      </div>

      <div className="flex flex-col gap-1 flex-1 min-w-0">
        <div
          className={cn(
            "rounded-2xl px-4 py-2.5",
            isUser
              ? "bg-muted rounded-br-md"
              : "bg-muted rounded-bl-md"
          )}
        >
          <p className="text-sm whitespace-pre-wrap">{message.content}</p>
        </div>

        {hasReferences && (
          <DocumentReferences references={message.references!} />
        )}

        <span
          className={cn(
            "text-xs text-muted-foreground",
            isUser ? "text-right" : "text-left"
          )}
        >
          {formatTime(message.timestamp)}
        </span>
      </div>
    </div>
  )
}
