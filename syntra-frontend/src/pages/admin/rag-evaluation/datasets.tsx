import { Link, useNavigate } from "react-router-dom"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { toast } from "sonner"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { createRun, downloadFile, listDatasets } from "./api"
import { AdminShell } from "./dashboard"

const DatasetsPage = () => {
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const datasetsQuery = useQuery({ queryKey: ["rag-evaluation", "datasets"], queryFn: () => listDatasets(1, 50) })
  const runMutation = useMutation({
    mutationFn: ({ id, name }: { id: number; name: string }) => createRun(id, name),
    onSuccess: (run) => { void queryClient.invalidateQueries({ queryKey: ["rag-evaluation"] }); navigate(`/admin/rag-evaluation/runs/${run.id}`) },
    onError: (error) => toast.error((error as Error).message),
  })

  return (
    <AdminShell>
      <div className="flex items-center justify-between gap-3">
        <div><h1 className="text-2xl font-semibold">Dataset Evaluasi</h1><p className="text-sm text-muted-foreground">Upload score-only CSV, preview, template, dan start batch evaluasi.</p></div>
        <div className="flex gap-2"><Button variant="outline" onClick={() => void downloadFile("/rag-evaluation/datasets/template", "rag-evaluation-score-only-template.csv")}>Template Score-Only</Button><Button asChild><Link to="/admin/rag-evaluation/datasets/upload">Upload CSV</Link></Button></div>
      </div>
      {datasetsQuery.isError && <div className="rounded-lg border border-destructive/40 bg-destructive/10 p-3 text-sm text-destructive">{(datasetsQuery.error as Error).message}</div>}
      <Card>
        <CardHeader><CardTitle>Daftar Dataset</CardTitle></CardHeader>
        <CardContent>
          <Table>
            <TableHeader><TableRow><TableHead>Nama</TableHead><TableHead>Mode</TableHead><TableHead>Status</TableHead><TableHead>Rows</TableHead><TableHead>Valid</TableHead><TableHead>Invalid</TableHead><TableHead /></TableRow></TableHeader>
            <TableBody>
              {(datasetsQuery.data?.items ?? []).map((dataset) => (
                <TableRow key={dataset.id}>
                  <TableCell className="font-medium">{dataset.name}</TableCell>
                  <TableCell>{dataset.evaluationMode}</TableCell>
                  <TableCell><Badge variant={dataset.status === "ready" ? "outline" : "destructive"}>{dataset.status}</Badge></TableCell>
                  <TableCell>{dataset.totalRows}</TableCell>
                  <TableCell>{dataset.validRows}</TableCell>
                  <TableCell>{dataset.invalidRows}</TableCell>
                  <TableCell className="text-right">
                    <Button asChild variant="ghost" size="sm"><Link to={`/admin/rag-evaluation/datasets/${dataset.id}`}>Preview</Link></Button>
                    <Button variant="ghost" size="sm" onClick={() => void downloadFile(`/rag-evaluation/datasets/${dataset.id}/download`, dataset.originalFilename ?? `dataset-${dataset.id}.csv`)}>Download</Button>
                    <Button size="sm" disabled={dataset.validRows <= 0 || runMutation.isPending} onClick={() => runMutation.mutate({ id: dataset.id, name: `${dataset.name} - Evaluation` })}>Start</Button>
                  </TableCell>
                </TableRow>
              ))}
              {datasetsQuery.data?.items.length === 0 && <TableRow><TableCell colSpan={7} className="h-24 text-center">Belum ada dataset.</TableCell></TableRow>}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </AdminShell>
  )
}

export default DatasetsPage
