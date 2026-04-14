import { useMemo, useState } from "react"
import { IconChevronDown, IconChevronUp, IconEdit, IconTrash } from "@tabler/icons-react"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"
import type { ChunkType, DocumentChunk } from "../edit-types"

interface DocumentChunksEditorProps {
  chunks: DocumentChunk[]
  onUpdateChunk: (chunkId: number, data: Partial<DocumentChunk>) => void
  onDeleteChunk: (chunkId: number) => void
}


const formatDateTime = (value: string | null): string => {
  if (!value) {
    return "-"
  }

  const date = new Date(value)
  if (Number.isNaN(date.getTime())) {
    return value
  }

  return date.toLocaleString()
}

const formatJson = (value: unknown): string => {
  if (value == null) {
    return "-"
  }

  try {
    return JSON.stringify(value, null, 2)
  } catch {
    return String(value)
  }
}

const getChunkTypeColor = (type: ChunkType | null) => {
  switch (type) {
    case "title":
      return "bg-blue-500/10 border-blue-200 text-blue-700"
    case "abstract":
      return "bg-purple-500/10 border-purple-200 text-purple-700"
    case "paragraph":
      return "bg-gray-500/10 border-gray-200 text-gray-700"
    case "table":
      return "bg-green-500/10 border-green-200 text-green-700"
    case "image":
      return "bg-pink-500/10 border-pink-200 text-pink-700"
    case "reference":
      return "bg-orange-500/10 border-orange-200 text-orange-700"
    default:
      return "bg-muted border-border text-muted-foreground"
  }
}

const getChunkTypeLabel = (type: ChunkType | null): string => type ?? "unknown"

export function DocumentChunksEditor({
  chunks,
  onUpdateChunk,
  onDeleteChunk,
}: DocumentChunksEditorProps) {
  const [editingChunk, setEditingChunk] = useState<DocumentChunk | null>(null)
  const [expandedChunks, setExpandedChunks] = useState<Set<number>>(new Set())

  const sortedChunks = useMemo(
    () => [...chunks].sort((left, right) => left.chunk_index - right.chunk_index),
    [chunks]
  )

  const toggleChunk = (chunkId: number) => {
    setExpandedChunks((prev) => {
      const next = new Set(prev)
      if (next.has(chunkId)) {
        next.delete(chunkId)
      } else {
        next.add(chunkId)
      }
      return next
    })
  }

  const handleSaveChunk = () => {
    if (!editingChunk) {
      return
    }

    onUpdateChunk(editingChunk.id, editingChunk)
    setEditingChunk(null)
  }

  return (
    <>
      <Card>
        <CardHeader>
          <CardTitle>Document Chunks ({chunks.length})</CardTitle>
          <CardDescription>
            Menampilkan seluruh data chunk yang dihasilkan dari proses dokumen
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-3">
          {sortedChunks.length === 0 ? (
            <div className="py-8 text-center text-muted-foreground">
              No chunks available for this document
            </div>
          ) : (
            sortedChunks.map((chunk) => (
              <Collapsible
                key={chunk.id}
                open={expandedChunks.has(chunk.id)}
                onOpenChange={() => toggleChunk(chunk.id)}
              >
                <div className="rounded-lg border">
                  <CollapsibleTrigger className="w-full">
                    <div className="flex items-center justify-between p-4 transition-colors hover:bg-muted/50">
                      <div className="flex items-center gap-3">
                        <div className="flex size-8 items-center justify-center rounded-full bg-primary/10 text-sm font-medium text-primary">
                          {chunk.chunk_index}
                        </div>
                        <div className="text-left">
                          <div className="text-sm font-medium">
                            {chunk.section_title || `Chunk ${chunk.chunk_index}`}
                          </div>
                          <div className="text-xs text-muted-foreground">
                            {chunk.token_count ?? "Unknown"} tokens
                            {chunk.page_number ? ` • Page ${chunk.page_number}` : ""}
                          </div>
                        </div>
                      </div>
                      <div className="flex items-center gap-2">
                        <Badge
                          variant="outline"
                          className={getChunkTypeColor(chunk.chunk_type)}
                        >
                          {getChunkTypeLabel(chunk.chunk_type)}
                        </Badge>
                        {expandedChunks.has(chunk.id) ? (
                          <IconChevronUp className="size-5 text-muted-foreground" />
                        ) : (
                          <IconChevronDown className="size-5 text-muted-foreground" />
                        )}
                      </div>
                    </div>
                  </CollapsibleTrigger>

                  <CollapsibleContent>
                    <div className="space-y-4 border-t bg-muted/20 p-4">
                      <div>
                        <Label className="text-xs text-muted-foreground">Content</Label>
                        <div className="mt-1 max-h-48 overflow-y-auto whitespace-pre-wrap rounded-md border bg-background p-3 text-sm">
                          {chunk.content}
                        </div>
                      </div>

                      <div className="grid gap-3 text-xs sm:grid-cols-2 lg:grid-cols-3">
                        <div>
                          <Label className="text-muted-foreground">Chunk ID</Label>
                          <p className="text-sm">{chunk.id}</p>
                        </div>
                        <div>
                          <Label className="text-muted-foreground">Document ID</Label>
                          <p className="text-sm">{chunk.document_id}</p>
                        </div>
                        <div>
                          <Label className="text-muted-foreground">Chunk Index</Label>
                          <p className="text-sm">{chunk.chunk_index}</p>
                        </div>
                        <div>
                          <Label className="text-muted-foreground">Token Count</Label>
                          <p className="text-sm">{chunk.token_count ?? "-"}</p>
                        </div>
                        <div>
                          <Label className="text-muted-foreground">Page Number</Label>
                          <p className="text-sm">{chunk.page_number ?? "-"}</p>
                        </div>
                        <div>
                          <Label className="text-muted-foreground">Section Title</Label>
                          <p className="text-sm">{chunk.section_title || "-"}</p>
                        </div>
                        <div>
                          <Label className="text-muted-foreground">Chunk Type</Label>
                          <p className="text-sm">{getChunkTypeLabel(chunk.chunk_type)}</p>
                        </div>
                        <div>
                          <Label className="text-muted-foreground">Created At</Label>
                          <p className="text-sm">{formatDateTime(chunk.created_at)}</p>
                        </div>
                        <div>
                          <Label className="text-muted-foreground">Updated At</Label>
                          <p className="text-sm">{formatDateTime(chunk.updated_at)}</p>
                        </div>
                      </div>

                      <div>
                        <Label className="text-xs text-muted-foreground">Possible Questions</Label>
                        {chunk.possibly_questions && chunk.possibly_questions.length > 0 ? (
                          <ul className="mt-1 space-y-1">
                            {chunk.possibly_questions.map((question, index) => (
                              <li
                                key={`${chunk.id}-question-${index}`}
                                className="flex gap-2 text-sm text-muted-foreground"
                              >
                                <span>•</span>
                                <span>{question}</span>
                              </li>
                            ))}
                          </ul>
                        ) : (
                          <p className="text-sm text-muted-foreground">-</p>
                        )}
                      </div>

                      <div className="space-y-2">
                        <Label className="text-xs text-muted-foreground">Chunk Metadata (JSON)</Label>
                        <pre className="max-h-56 overflow-y-auto rounded-md border bg-background p-3 text-xs">
                          {formatJson(chunk.chunk_metadata)}
                        </pre>
                      </div>

                      <div className="space-y-2">
                        <Label className="text-xs text-muted-foreground">Embedding</Label>
                        <pre className="max-h-56 overflow-y-auto rounded-md border bg-background p-3 text-xs">
                          {formatJson(chunk.embedding)}
                        </pre>
                      </div>

                      <div className="space-y-2">
                        <Label className="text-xs text-muted-foreground">Possible Question Embedding</Label>
                        <pre className="max-h-56 overflow-y-auto rounded-md border bg-background p-3 text-xs">
                          {formatJson(chunk.possibly_question_embedding)}
                        </pre>
                      </div>

                      <div className="flex gap-2 pt-2">
                        <Button
                          variant="outline"
                          size="sm"
                          onClick={(event) => {
                            event.stopPropagation()
                            setEditingChunk(chunk)
                          }}
                        >
                          <IconEdit className="mr-1 size-4" />
                          Edit
                        </Button>
                        <Button
                          variant="outline"
                          size="sm"
                          onClick={(event) => {
                            event.stopPropagation()
                            if (confirm("Are you sure you want to delete this chunk?")) {
                              onDeleteChunk(chunk.id)
                            }
                          }}
                        >
                          <IconTrash className="mr-1 size-4" />
                          Delete
                        </Button>
                      </div>
                    </div>
                  </CollapsibleContent>
                </div>
              </Collapsible>
            ))
          )}
        </CardContent>
      </Card>

      <Dialog open={Boolean(editingChunk)} onOpenChange={() => setEditingChunk(null)}>
        <DialogContent className="max-h-[90vh] max-w-3xl overflow-y-auto">
          <DialogHeader>
            <DialogTitle>Edit Chunk {editingChunk?.chunk_index}</DialogTitle>
            <DialogDescription>Modify chunk content and metadata</DialogDescription>
          </DialogHeader>

          {editingChunk && (
            <div className="space-y-4 py-4">
              <div className="space-y-2">
                <Label htmlFor="chunk-content">Content</Label>
                <Textarea
                  id="chunk-content"
                  value={editingChunk.content}
                  onChange={(event: React.ChangeEvent<HTMLTextAreaElement>) =>
                    setEditingChunk({ ...editingChunk, content: event.target.value })
                  }
                  rows={10}
                  className="font-mono text-sm"
                />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="chunk-type">Chunk Type</Label>
                  <Select
                    value={editingChunk.chunk_type ?? "paragraph"}
                    onValueChange={(value) =>
                      setEditingChunk({ ...editingChunk, chunk_type: value as ChunkType })
                    }
                  >
                    <SelectTrigger id="chunk-type">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="title">Title</SelectItem>
                      <SelectItem value="abstract">Abstract</SelectItem>
                      <SelectItem value="paragraph">Paragraph</SelectItem>
                      <SelectItem value="table">Table</SelectItem>
                      <SelectItem value="image">Image</SelectItem>
                      <SelectItem value="reference">Reference</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="page-number">Page Number</Label>
                  <Input
                    id="page-number"
                    type="number"
                    value={editingChunk.page_number ?? ""}
                    onChange={(event) => {
                      const value = event.target.value
                      setEditingChunk({
                        ...editingChunk,
                        page_number: value ? Number.parseInt(value, 10) : null,
                      })
                    }}
                    min="1"
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="section-title">Section Title</Label>
                <Input
                  id="section-title"
                  value={editingChunk.section_title ?? ""}
                  onChange={(event) =>
                    setEditingChunk({
                      ...editingChunk,
                      section_title: event.target.value || null,
                    })
                  }
                  placeholder="Optional section title"
                />
              </div>
            </div>
          )}

          <DialogFooter>
            <Button variant="outline" onClick={() => setEditingChunk(null)}>
              Cancel
            </Button>
            <Button onClick={handleSaveChunk}>Save Changes</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </>
  )
}
