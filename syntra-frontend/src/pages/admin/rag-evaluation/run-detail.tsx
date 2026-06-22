import { Link, useParams } from "react-router-dom"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { toast } from "sonner"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { cancelRun, downloadFile, getRun, listAllSamples } from "./api"
import { AdminShell } from "./dashboard"

const fmtScore = (value: number | null | undefined) => value == null ? "-" : value.toFixed(3)
const activeStatuses = new Set(["queued", "preparing", "running_rag", "running_ragas", "aggregating"])

const RunDetailPage = () => {
  const params = useParams()
  const queryClient = useQueryClient()
  const runId = Number(params.runId)
  const runQuery = useQuery({ queryKey: ["rag-evaluation", "run", runId], queryFn: () => getRun(runId), enabled: Number.isFinite(runId), refetchInterval: (query) => query.state.data && activeStatuses.has(query.state.data.status) ? 3000 : false })
  const samplesQuery = useQuery({ queryKey: ["rag-evaluation", "run", runId, "samples", "all"], queryFn: () => listAllSamples(runId), enabled: Number.isFinite(runId), refetchInterval: runQuery.data && activeStatuses.has(runQuery.data.status) ? 3000 : false })
  const cancelMutation = useMutation({ mutationFn: () => cancelRun(runId), onSuccess: () => void queryClient.invalidateQueries({ queryKey: ["rag-evaluation", "run", runId] }), onError: (error) => toast.error((error as Error).message) })
  const run = runQuery.data

  return (
    <AdminShell>
      <div className="flex items-center justify-between gap-3">
        <div><h1 className="text-2xl font-semibold">{run?.name ?? "Evaluation Run"}</h1><p className="text-sm text-muted-foreground">Detail batch, konfigurasi, skor agregat, dan sample.</p></div>
        <div className="flex gap-2"><Button asChild variant="outline"><Link to="/admin/rag-evaluation">Dashboard</Link></Button>{run?.status === "completed" && <Button variant="outline" onClick={() => void downloadFile(`/rag-evaluation/runs/${run.id}/export`, `rag-run-${run.id}.csv`)}>Export CSV</Button>}{run && activeStatuses.has(run.status) && <Button variant="destructive" onClick={() => cancelMutation.mutate()}>Cancel</Button>}</div>
      </div>
      {runQuery.isError && <div className="rounded-lg border border-destructive/40 bg-destructive/10 p-3 text-sm text-destructive">{(runQuery.error as Error).message}</div>}
      {run && <>
        <Card><CardHeader className="flex flex-row items-center justify-between"><CardTitle>{run.datasetName ?? `Dataset ${run.datasetId}`}</CardTitle><Badge>{run.status}</Badge></CardHeader><CardContent><div className="h-2 overflow-hidden rounded bg-muted"><div className="h-full bg-primary" style={{ width: `${run.progress}%` }} /></div><p className="mt-2 text-sm text-muted-foreground">{run.processedSamples} / {run.totalSamples} processed. Failed {run.failedSamples}.</p></CardContent></Card>
        <div className="grid gap-4 md:grid-cols-4"><Card><CardHeader><CardTitle>{fmtScore(run.faithfulnessAvg)}</CardTitle></CardHeader><CardContent>Faithfulness</CardContent></Card><Card><CardHeader><CardTitle>{fmtScore(run.answerRelevancyAvg)}</CardTitle></CardHeader><CardContent>Answer Relevancy</CardContent></Card><Card><CardHeader><CardTitle>{fmtScore(run.contextPrecisionAvg)}</CardTitle></CardHeader><CardContent>Context Precision</CardContent></Card><Card><CardHeader><CardTitle>{fmtScore(run.contextRecallAvg)}</CardTitle></CardHeader><CardContent>Context Recall</CardContent></Card></div>
        <Card><CardHeader><CardTitle>Konfigurasi</CardTitle></CardHeader><CardContent className="grid gap-2 text-sm md:grid-cols-3"><div>Generator: {run.generatorModel ?? "-"}</div><div>Embedding: {run.embeddingModel ?? "-"}</div><div>Evaluator: {run.evaluatorModel ?? "-"}</div><div>RAGAS: {run.ragasVersion ?? "-"}</div><div>Mode: {run.evaluationMode}</div><div>Task: {run.celeryTaskId ?? "-"}</div></CardContent></Card>
      </>}
      <Card><CardHeader><CardTitle>Sample Results</CardTitle></CardHeader><CardContent><Table><TableHeader><TableRow><TableHead>No</TableHead><TableHead>Pertanyaan</TableHead><TableHead>Status</TableHead><TableHead>Faithfulness</TableHead><TableHead>Answer</TableHead><TableHead>Precision</TableHead><TableHead>Recall</TableHead></TableRow></TableHeader><TableBody>{(samplesQuery.data?.items ?? []).map((sample) => <TableRow key={sample.id}><TableCell>{sample.sampleIndex}</TableCell><TableCell className="max-w-xl truncate">{sample.userInput}</TableCell><TableCell><Badge variant={sample.status === "failed" ? "destructive" : "outline"}>{sample.status}</Badge></TableCell><TableCell>{fmtScore(sample.faithfulness)}</TableCell><TableCell>{fmtScore(sample.answerRelevancy)}</TableCell><TableCell>{fmtScore(sample.contextPrecision)}</TableCell><TableCell>{fmtScore(sample.contextRecall)}</TableCell></TableRow>)}</TableBody></Table></CardContent></Card>
    </AdminShell>
  )
}

export default RunDetailPage
