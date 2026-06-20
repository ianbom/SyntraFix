import { Link, useNavigate, useParams } from "react-router-dom"
import { useMutation, useQuery } from "@tanstack/react-query"
import { toast } from "sonner"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { createRun, getDataset } from "./api"
import { AdminShell } from "./dashboard"

const DatasetDetailPage = () => {
  const params = useParams()
  const navigate = useNavigate()
  const datasetId = Number(params.datasetId)
  const datasetQuery = useQuery({ queryKey: ["rag-evaluation", "dataset", datasetId], queryFn: () => getDataset(datasetId), enabled: Number.isFinite(datasetId) })
  const runMutation = useMutation({
    mutationFn: () => createRun(datasetId, `${datasetQuery.data?.name ?? "Dataset"} - Evaluation`, datasetQuery.data?.evaluationMode),
    onSuccess: (run) => navigate(`/admin/rag-evaluation/runs/${run.id}`),
    onError: (error) => toast.error((error as Error).message),
  })
  const dataset = datasetQuery.data

  return (
    <AdminShell>
      <div className="flex items-center justify-between gap-3">
        <div><h1 className="text-2xl font-semibold">{dataset?.name ?? "Dataset"}</h1><p className="text-sm text-muted-foreground">Preview baris valid/invalid sebelum evaluasi.</p></div>
        <div className="flex gap-2"><Button asChild variant="outline"><Link to="/admin/rag-evaluation/datasets">Kembali</Link></Button><Button disabled={!dataset || dataset.status !== "ready" || runMutation.isPending} onClick={() => runMutation.mutate()}>Start Evaluation</Button></div>
      </div>
      {datasetQuery.isError && <div className="rounded-lg border border-destructive/40 bg-destructive/10 p-3 text-sm text-destructive">{(datasetQuery.error as Error).message}</div>}
      {dataset && <div className="grid gap-4 md:grid-cols-4"><Card><CardHeader><CardTitle>{dataset.totalRows}</CardTitle></CardHeader><CardContent>Total rows</CardContent></Card><Card><CardHeader><CardTitle>{dataset.validRows}</CardTitle></CardHeader><CardContent>Valid</CardContent></Card><Card><CardHeader><CardTitle>{dataset.invalidRows}</CardTitle></CardHeader><CardContent>Invalid</CardContent></Card><Card><CardHeader><CardTitle><Badge>{dataset.status}</Badge></CardTitle></CardHeader><CardContent>{dataset.evaluationMode}</CardContent></Card></div>}
      <Card>
        <CardHeader><CardTitle>Preview Rows</CardTitle></CardHeader>
        <CardContent><Table><TableHeader><TableRow><TableHead>No</TableHead><TableHead>User Input</TableHead><TableHead>Reference</TableHead><TableHead>Status</TableHead><TableHead>Pesan</TableHead></TableRow></TableHeader><TableBody>{(dataset?.rows ?? []).slice(0, 100).map((row) => <TableRow key={row.id}><TableCell>{row.rowNumber}</TableCell><TableCell className="max-w-md truncate">{row.userInput}</TableCell><TableCell className="max-w-md truncate">{row.reference ?? "-"}</TableCell><TableCell><Badge variant={row.validationStatus === "valid" ? "outline" : "destructive"}>{row.validationStatus}</Badge></TableCell><TableCell>{row.validationMessage ?? "-"}</TableCell></TableRow>)}</TableBody></Table></CardContent>
      </Card>
    </AdminShell>
  )
}

export default DatasetDetailPage
