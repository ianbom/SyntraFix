import { Link } from "react-router-dom"
import type React from "react"
import { useState } from "react"
import { useMutation, useQuery } from "@tanstack/react-query"
import { toast } from "sonner"
import { Line, LineChart, CartesianGrid, XAxis, YAxis } from "recharts"
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { getDashboardDistribution, getDashboardSummary, listRuns, downloadFile, exportChatCsv } from "./api"
import type { RagRun } from "./types"

const metrics = [
  ["Faithfulness", "faithfulnessAvg"],
  ["Answer Relevancy", "answerRelevancyAvg"],
  ["Context Precision", "contextPrecisionAvg"],
  ["Context Recall", "contextRecallAvg"],
] as const

const fmtScore = (value: number | null | undefined) => (value == null ? "-" : `${(value * 100).toFixed(1)}%`)
const fmtDate = (value: string | null | undefined) => value ? new Date(value).toLocaleDateString("id-ID", { day: "2-digit", month: "short", year: "numeric" }) : "-"

export function AdminShell({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider style={{ "--sidebar-width": "calc(var(--spacing) * 72)", "--header-height": "calc(var(--spacing) * 12)" } as React.CSSProperties}>
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
        <div className="flex flex-1 flex-col gap-4 p-4 md:p-6">{children}</div>
      </SidebarInset>
    </SidebarProvider>
  )
}

function ActiveRun({ run }: { run: RagRun | null }) {
  if (!run) return null
  return (
    <Card>
      <CardHeader className="flex flex-row items-start justify-between gap-4">
        <div>
          <CardTitle>Active Evaluation</CardTitle>
          <CardDescription>{run.name}</CardDescription>
        </div>
        <Badge>{run.status.replaceAll("_", " ")}</Badge>
      </CardHeader>
      <CardContent className="grid gap-3 md:grid-cols-5">
        <div className="md:col-span-2">
          <div className="h-2 overflow-hidden rounded bg-muted"><div className="h-full bg-primary" style={{ width: `${run.progress}%` }} /></div>
          <p className="mt-2 text-sm text-muted-foreground">{run.processedSamples} / {run.totalSamples} samples</p>
        </div>
        <div className="text-sm">Success<br /><span className="text-lg font-semibold">{run.successfulSamples}</span></div>
        <div className="text-sm">Failed<br /><span className="text-lg font-semibold">{run.failedSamples}</span></div>
        <Button asChild variant="outline"><Link to={`/admin/rag-evaluation/runs/${run.id}`}>Detail</Link></Button>
      </CardContent>
    </Card>
  )
}

const RagEvaluationDashboard = () => {
  const [chatExportDateFrom, setChatExportDateFrom] = useState("")
  const [chatExportDateTo, setChatExportDateTo] = useState("")
  const summaryQuery = useQuery({ queryKey: ["rag-evaluation", "summary"], queryFn: getDashboardSummary, refetchInterval: (query) => query.state.data?.activeRun ? 3000 : false })
  const distributionQuery = useQuery({ queryKey: ["rag-evaluation", "distribution", summaryQuery.data?.latestCompletedRun?.id], queryFn: () => getDashboardDistribution(summaryQuery.data?.latestCompletedRun?.id), enabled: Boolean(summaryQuery.data?.latestCompletedRun) })
  const runsQuery = useQuery({ queryKey: ["rag-evaluation", "runs"], queryFn: () => listRuns(1, 10) })
  const chatExportMutation = useMutation({
    mutationFn: exportChatCsv,
    onError: (error) => toast.error((error as Error).message),
  })
  const latest = summaryQuery.data?.latestCompletedRun ?? null
  const canExportChat = chatExportDateFrom.length > 0 && chatExportDateTo.length > 0 && !chatExportMutation.isPending

  const handleExportChat = () => {
    if (!chatExportDateFrom || !chatExportDateTo) {
      toast.error("Pilih rentang tanggal export chat.")
      return
    }
    if (chatExportDateFrom > chatExportDateTo) {
      toast.error("Tanggal mulai tidak boleh lebih besar dari tanggal akhir.")
      return
    }
    chatExportMutation.mutate({ dateFrom: chatExportDateFrom, dateTo: chatExportDateTo })
  }

  return (
    <AdminShell>
      <div className="flex items-center justify-between gap-3">
        <div><h1 className="text-2xl font-semibold">Skor Evaluasi RAG</h1><p className="text-sm text-muted-foreground">Batch terbaru, progress aktif, history evaluasi.</p></div>
        <div className="flex flex-wrap items-end gap-2">
          <div className="grid gap-1">
            <Label htmlFor="chat-export-date-from" className="text-xs">Dari</Label>
            <Input id="chat-export-date-from" type="date" value={chatExportDateFrom} onChange={(event) => setChatExportDateFrom(event.target.value)} className="h-9 w-[150px]" />
          </div>
          <div className="grid gap-1">
            <Label htmlFor="chat-export-date-to" className="text-xs">Sampai</Label>
            <Input id="chat-export-date-to" type="date" value={chatExportDateTo} onChange={(event) => setChatExportDateTo(event.target.value)} className="h-9 w-[150px]" />
          </div>
          <Button variant="outline" disabled={!canExportChat} onClick={handleExportChat}>{chatExportMutation.isPending ? "Exporting..." : "Export Chat CSV"}</Button>
          <Button asChild variant="outline"><Link to="/admin/rag-evaluation/datasets">Dataset</Link></Button>
          <Button asChild><Link to="/admin/rag-evaluation/datasets/upload">Upload CSV</Link></Button>
        </div>
      </div>
      {summaryQuery.isError && <div className="rounded-lg border border-destructive/40 bg-destructive/10 p-3 text-sm text-destructive">{(summaryQuery.error as Error).message}</div>}
      <ActiveRun run={summaryQuery.data?.activeRun ?? null} />
      <div className="grid gap-4 md:grid-cols-4">
        {metrics.map(([label, key]) => <Card key={key}><CardHeader><CardDescription>{label}</CardDescription><CardTitle className="text-3xl">{fmtScore(latest?.[key])}</CardTitle></CardHeader><CardContent className="text-sm text-muted-foreground">{latest ? `${latest.successfulSamples} sampel valid` : "Belum ada evaluasi selesai"}</CardContent></Card>)}
      </div>
      <div className="grid gap-4 xl:grid-cols-3">
        <Card className="xl:col-span-2">
          <CardHeader><CardTitle>Tren Riwayat</CardTitle><CardDescription>Empat metrik RAGAS per batch selesai.</CardDescription></CardHeader>
          <CardContent>
            <ChartContainer config={{ faithfulness: { label: "Faithfulness", color: "#2563eb" }, answerRelevancy: { label: "Answer", color: "#16a34a" }, contextPrecision: { label: "Precision", color: "#f59e0b" }, contextRecall: { label: "Recall", color: "#dc2626" } }} className="h-[280px] w-full">
              <LineChart data={summaryQuery.data?.history ?? []}><CartesianGrid vertical={false} /><XAxis dataKey="name" tickLine={false} axisLine={false} /><YAxis domain={[0, 1]} /><ChartTooltip content={<ChartTooltipContent />} /><Line dataKey="faithfulness" stroke="var(--color-faithfulness)" dot={false} /><Line dataKey="answerRelevancy" stroke="var(--color-answerRelevancy)" dot={false} /><Line dataKey="contextPrecision" stroke="var(--color-contextPrecision)" dot={false} /><Line dataKey="contextRecall" stroke="var(--color-contextRecall)" dot={false} /></LineChart>
            </ChartContainer>
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Distribusi Terbaru</CardTitle><CardDescription>Jumlah sampel per rentang skor.</CardDescription></CardHeader>
          <CardContent className="space-y-3 text-sm">
            {Object.entries(distributionQuery.data?.buckets ?? {}).map(([bucket, values]) => <div key={bucket} className="rounded border p-3"><div className="mb-2 font-medium">{bucket.replaceAll("_", " ")}</div><div className="grid grid-cols-2 gap-1 text-muted-foreground">{Object.entries(values).map(([key, value]) => <span key={key}>{key}: {value}</span>)}</div></div>)}
          </CardContent>
        </Card>
      </div>
      <Card>
        <CardHeader><CardTitle>Riwayat Evaluasi</CardTitle></CardHeader>
        <CardContent><Table><TableHeader><TableRow><TableHead>Batch</TableHead><TableHead>Dataset</TableHead><TableHead>Status</TableHead><TableHead>Sampel</TableHead><TableHead>Faithfulness</TableHead><TableHead>Tanggal</TableHead><TableHead /></TableRow></TableHeader><TableBody>{(runsQuery.data?.items ?? []).map((run) => <TableRow key={run.id}><TableCell className="font-medium">{run.name}</TableCell><TableCell>{run.datasetName ?? run.datasetId}</TableCell><TableCell><Badge variant={run.status === "failed" ? "destructive" : "outline"}>{run.status}</Badge></TableCell><TableCell>{run.successfulSamples}/{run.totalSamples}</TableCell><TableCell>{fmtScore(run.faithfulnessAvg)}</TableCell><TableCell>{fmtDate(run.createdAt)}</TableCell><TableCell className="text-right"><Button asChild variant="ghost" size="sm"><Link to={`/admin/rag-evaluation/runs/${run.id}`}>Detail</Link></Button>{run.status === "completed" && <Button variant="ghost" size="sm" onClick={() => void downloadFile(`/rag-evaluation/runs/${run.id}/export`, `rag-run-${run.id}.csv`)}>Export</Button>}</TableCell></TableRow>)}</TableBody></Table></CardContent>
      </Card>
    </AdminShell>
  )
}

export default RagEvaluationDashboard
