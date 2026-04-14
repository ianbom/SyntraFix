import { useEffect, useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Switch } from "@/components/ui/switch"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import type { DocumentDetail, DocumentType } from "../edit-types"

interface DocumentEditFormProps {
  document: DocumentDetail
  onUpdate: (data: Partial<DocumentDetail>) => void
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

export function DocumentEditForm({ document, onUpdate }: DocumentEditFormProps) {
  const [formData, setFormData] = useState<DocumentDetail>(document)

  useEffect(() => {
    setFormData(document)
  }, [document])

  const handleChange = <K extends keyof DocumentDetail>(
    field: K,
    value: DocumentDetail[K]
  ) => {
    setFormData((prev) => ({ ...prev, [field]: value }))
    onUpdate({ [field]: value } as Partial<DocumentDetail>)
  }

  return (
    <Tabs defaultValue="basic" className="w-full">
      <TabsList className="grid w-full grid-cols-4">
        <TabsTrigger value="basic">Basic Info</TabsTrigger>
        <TabsTrigger value="dublin">Dublin Core</TabsTrigger>
        <TabsTrigger value="extended">Extended</TabsTrigger>
        <TabsTrigger value="status">Status</TabsTrigger>
      </TabsList>

      <TabsContent value="basic" className="space-y-4">
        <Card>
          <CardHeader>
            <CardTitle>Basic Information</CardTitle>
            <CardDescription>Essential document information</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="title">Title *</Label>
              <Input
                id="title"
                value={formData.title}
                onChange={(event: React.ChangeEvent<HTMLInputElement>) =>
                  handleChange("title", event.target.value)
                }
                placeholder="Document title"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="creator">Creator/Authors</Label>
              <Input
                id="creator"
                value={formData.creator ?? ""}
                onChange={(event: React.ChangeEvent<HTMLInputElement>) =>
                  handleChange("creator", event.target.value)
                }
                placeholder="Authors (comma-separated)"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="abstract">Abstract</Label>
              <Textarea
                id="abstract"
                value={formData.abstract ?? ""}
                onChange={(event: React.ChangeEvent<HTMLTextAreaElement>) =>
                  handleChange("abstract", event.target.value)
                }
                placeholder="Document abstract"
                rows={6}
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="type">Document Type</Label>
                <Select
                  value={formData.type}
                  onValueChange={(value) => handleChange("type", value as DocumentType)}
                >
                  <SelectTrigger id="type">
                    <SelectValue placeholder="Select type" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="journal">Journal</SelectItem>
                    <SelectItem value="conference">Conference</SelectItem>
                    <SelectItem value="thesis">Thesis</SelectItem>
                    <SelectItem value="book">Book</SelectItem>
                    <SelectItem value="report">Report</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <Label htmlFor="date">Publication Date</Label>
                <Input
                  id="date"
                  type="date"
                  value={formData.date ?? ""}
                  onChange={(event: React.ChangeEvent<HTMLInputElement>) =>
                    handleChange("date", event.target.value || null)
                  }
                />
              </div>
            </div>
          </CardContent>
        </Card>
      </TabsContent>

      <TabsContent value="dublin" className="space-y-4">
        <Card>
          <CardHeader>
            <CardTitle>Dublin Core Metadata</CardTitle>
            <CardDescription>Standard metadata fields for academic resources</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="keywords">Keywords/Subject</Label>
              <Textarea
                id="keywords"
                value={formData.keywords ?? ""}
                onChange={(event: React.ChangeEvent<HTMLTextAreaElement>) =>
                  handleChange("keywords", event.target.value)
                }
                placeholder="Keywords (comma-separated)"
                rows={2}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="description">Description</Label>
              <Textarea
                id="description"
                value={formData.description ?? ""}
                onChange={(event: React.ChangeEvent<HTMLTextAreaElement>) =>
                  handleChange("description", event.target.value)
                }
                placeholder="Short description"
                rows={3}
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="publisher">Publisher</Label>
                <Input
                  id="publisher"
                  value={formData.publisher ?? ""}
                  onChange={(event) => handleChange("publisher", event.target.value)}
                  placeholder="Publisher name"
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="contributor">Contributor</Label>
                <Input
                  id="contributor"
                  value={formData.contributor ?? ""}
                  onChange={(event) => handleChange("contributor", event.target.value)}
                  placeholder="Contributors"
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="source">Source</Label>
                <Input
                  id="source"
                  value={formData.source ?? ""}
                  onChange={(event) => handleChange("source", event.target.value)}
                  placeholder="Journal/Conference name"
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="language">Language</Label>
                <Input
                  id="language"
                  value={formData.language ?? ""}
                  onChange={(event) => handleChange("language", event.target.value)}
                  placeholder="e.g., en, id"
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="format">Format</Label>
                <Input
                  id="format"
                  value={formData.format ?? ""}
                  onChange={(event) => handleChange("format", event.target.value)}
                  placeholder="MIME type or file format"
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="identifier">Identifier</Label>
                <Input
                  id="identifier"
                  value={formData.identifier ?? ""}
                  onChange={(event) => handleChange("identifier", event.target.value)}
                  placeholder="Unique identifier"
                />
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="relation">Relation</Label>
              <Input
                id="relation"
                value={formData.relation ?? ""}
                onChange={(event) => handleChange("relation", event.target.value)}
                placeholder="Related resources"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="coverage">Coverage</Label>
              <Input
                id="coverage"
                value={formData.coverage ?? ""}
                onChange={(event) => handleChange("coverage", event.target.value)}
                placeholder="Spatial/temporal coverage"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="rights">Rights</Label>
              <Textarea
                id="rights"
                value={formData.rights ?? ""}
                onChange={(event) => handleChange("rights", event.target.value)}
                placeholder="Copyright information"
                rows={2}
              />
            </div>
          </CardContent>
        </Card>
      </TabsContent>

      <TabsContent value="extended" className="space-y-4">
        <Card>
          <CardHeader>
            <CardTitle>Extended Metadata</CardTitle>
            <CardDescription>Additional document information</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="doi">DOI</Label>
                <Input
                  id="doi"
                  value={formData.doi ?? ""}
                  onChange={(event) => handleChange("doi", event.target.value)}
                  placeholder="10.xxxx/xxxxx"
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="citation_count">Citation Count</Label>
                <Input
                  id="citation_count"
                  type="number"
                  value={formData.citation_count}
                  onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                    const nextValue = Number.parseInt(event.target.value, 10)
                    handleChange("citation_count", Number.isNaN(nextValue) ? 0 : nextValue)
                  }}
                  min="0"
                />
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="file_path">File Path</Label>
              <Input
                id="file_path"
                value={formData.file_path ?? ""}
                placeholder="MinIO object name"
                disabled
              />
              <p className="text-xs text-muted-foreground">File path cannot be edited directly</p>
            </div>
          </CardContent>
        </Card>
      </TabsContent>

      <TabsContent value="status" className="space-y-4">
        <Card>
          <CardHeader>
            <CardTitle>Document Status</CardTitle>
            <CardDescription>Processing and visibility settings</CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="flex items-center justify-between">
              <div className="space-y-0.5">
                <Label htmlFor="is_private">Private Document</Label>
                <p className="text-sm text-muted-foreground">
                  Document is only visible to authorized users
                </p>
              </div>
              <Switch
                id="is_private"
                checked={formData.is_private}
                onCheckedChange={(checked) => handleChange("is_private", checked)}
              />
            </div>

            <div className="flex items-center justify-between">
              <div className="space-y-0.5">
                <Label htmlFor="is_metadata_complete">Metadata Complete</Label>
                <p className="text-sm text-muted-foreground">
                  All required metadata fields are filled
                </p>
              </div>
              <Switch
                id="is_metadata_complete"
                checked={formData.is_metadata_complete}
                onCheckedChange={(checked) => handleChange("is_metadata_complete", checked)}
              />
            </div>

            <div className="space-y-2">
              <Label>Processing Status</Label>
              <div className="rounded-md border bg-muted/50 p-3">
                <span className="font-medium capitalize">{formData.processing_status}</span>
              </div>
              <p className="text-xs text-muted-foreground">Processing status is automatically managed</p>
            </div>

            <div className="space-y-2">
              <Label>Processing Progress</Label>
              <div className="rounded-md border bg-muted/50 p-3">
                <span className="font-medium">{formData.processing_progress}%</span>
              </div>
            </div>

            {formData.processing_error && (
              <div className="space-y-2">
                <Label>Processing Error</Label>
                <div className="rounded-md border bg-destructive/10 p-3 text-sm text-destructive">
                  {formData.processing_error}
                </div>
              </div>
            )}

            <div className="grid grid-cols-2 gap-4 border-t pt-4">
              <div className="space-y-2">
                <Label className="text-muted-foreground">Document ID</Label>
                <div className="text-sm">{formData.id}</div>
              </div>
              <div className="space-y-2">
                <Label className="text-muted-foreground">Chunk Count</Label>
                <div className="text-sm">{formData.chunk_count}</div>
              </div>
              <div className="space-y-2">
                <Label className="text-muted-foreground">Created At</Label>
                <div className="text-sm">{formatDateTime(formData.created_at)}</div>
              </div>
              <div className="space-y-2">
                <Label className="text-muted-foreground">Updated At</Label>
                <div className="text-sm">{formatDateTime(formData.updated_at)}</div>
              </div>
            </div>
          </CardContent>
        </Card>
      </TabsContent>
    </Tabs>
  )
}
