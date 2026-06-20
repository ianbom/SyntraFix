import { useState } from "react"
import type { FormEvent } from "react"
import { useNavigate } from "react-router-dom"
import { useMutation } from "@tanstack/react-query"
import { toast } from "sonner"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"
import { uploadDataset } from "./api"
import { AdminShell } from "./dashboard"
import type { EvaluationMode } from "./types"

const DatasetUploadPage = () => {
  const navigate = useNavigate()
  const [file, setFile] = useState<File | null>(null)
  const [mode, setMode] = useState<EvaluationMode>("score_only")
  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const mutation = useMutation({
    mutationFn: () => {
      if (!file) throw new Error("Pilih file CSV terlebih dahulu.")
      return uploadDataset({ file, mode, name: name || undefined, description: description || undefined })
    },
    onSuccess: (dataset) => { toast.success("Dataset tersimpan."); navigate(`/admin/rag-evaluation/datasets/${dataset.id}`) },
    onError: (error) => toast.error((error as Error).message),
  })

  const submit = (event: FormEvent) => {
    event.preventDefault()
    mutation.mutate()
  }

  return (
    <AdminShell>
      <div><h1 className="text-2xl font-semibold">Upload Dataset Evaluasi</h1><p className="text-sm text-muted-foreground">Gunakan score-only CSV: user_input + response + retrieved_contexts + reference.</p></div>
      <Card className="max-w-3xl">
        <CardHeader><CardTitle>CSV Dataset</CardTitle><CardDescription>Validasi dilakukan di backend saat upload.</CardDescription></CardHeader>
        <CardContent>
          <form className="space-y-4" onSubmit={submit}>
            <div className="grid gap-2"><Label htmlFor="name">Nama dataset</Label><Input id="name" value={name} onChange={(event) => setName(event.target.value)} placeholder="Dataset RAG V2" /></div>
            <div className="grid gap-2"><Label htmlFor="description">Deskripsi</Label><Textarea id="description" value={description} onChange={(event) => setDescription(event.target.value)} placeholder="Catatan dataset" /></div>
            <div className="grid gap-2"><Label>Mode evaluasi</Label><Select value={mode} onValueChange={(value) => setMode(value as EvaluationMode)}><SelectTrigger><SelectValue /></SelectTrigger><SelectContent><SelectItem value="score_only">Score-Only Evaluation</SelectItem><SelectItem value="pipeline">Pipeline Evaluation</SelectItem></SelectContent></Select></div>
            <div className="grid gap-2"><Label htmlFor="file">File CSV</Label><Input id="file" type="file" accept=".csv,text/csv" onChange={(event) => setFile(event.target.files?.[0] ?? null)} /></div>
            <div className="flex gap-2"><Button type="submit" disabled={mutation.isPending}>{mutation.isPending ? "Mengunggah..." : "Upload dan Validasi"}</Button><Button type="button" variant="outline" onClick={() => navigate("/admin/rag-evaluation/datasets")}>Batal</Button></div>
          </form>
        </CardContent>
      </Card>
    </AdminShell>
  )
}

export default DatasetUploadPage
