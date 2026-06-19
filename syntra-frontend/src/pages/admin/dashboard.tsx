import { useQuery } from "@tanstack/react-query"
import { AppSidebar } from "@/components/app-sidebar"
import { ChartAreaInteractive } from "@/components/chart-area-interactive"
import { SectionCards } from "@/components/section-cards"
import { SiteHeader } from "@/components/site-header"
import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  SidebarInset,
  SidebarProvider,
} from "@/components/ui/sidebar"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { getAdminDashboard } from "./api"
import type { AdminRecentDocument } from "./api"

const formatDate = (date: string) =>
  new Date(date).toLocaleDateString("id-ID", {
    year: "numeric",
    month: "short",
    day: "numeric",
  })

const getStatusLabel = (status: string | null) => {
  if (status === "completed") return "Selesai"
  if (status === "processing") return "Diproses"
  if (status === "failed") return "Gagal"
  return status ?? "-"
}

function RecentDocumentsTable({ documents }: { documents: AdminRecentDocument[] }) {
  return (
    <Card className="mx-4 lg:mx-6">
      <CardHeader>
        <CardTitle>Dokumen Terbaru</CardTitle>
        <CardDescription>Data dokumen terakhir dari backend</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="overflow-hidden rounded-lg border">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Judul</TableHead>
                <TableHead>Tipe</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Dibuat</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {documents.length > 0 ? (
                documents.map((document) => (
                  <TableRow key={document.id}>
                    <TableCell className="font-medium">{document.title}</TableCell>
                    <TableCell className="capitalize">{document.type ?? "-"}</TableCell>
                    <TableCell>
                      <Badge variant={document.processingStatus === "failed" ? "destructive" : "outline"}>
                        {getStatusLabel(document.processingStatus)}
                      </Badge>
                    </TableCell>
                    <TableCell>{formatDate(document.createdAt)}</TableCell>
                  </TableRow>
                ))
              ) : (
                <TableRow>
                  <TableCell colSpan={4} className="h-24 text-center">
                    Belum ada dokumen.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  )
}

const Dashboard = () => {
  const dashboardQuery = useQuery({
    queryKey: ["admin-dashboard"],
    queryFn: ({ signal }) => getAdminDashboard(signal),
  })

  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "calc(var(--spacing) * 72)",
          "--header-height": "calc(var(--spacing) * 12)",
        } as React.CSSProperties
      }
    >
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
        <div className="flex flex-1 flex-col">
          <div className="@container/main flex flex-1 flex-col gap-2">
            <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
              {dashboardQuery.isError && (
                <div className="mx-4 rounded-lg border border-destructive/40 bg-destructive/10 px-4 py-3 text-sm text-destructive lg:mx-6">
                  {(dashboardQuery.error as Error).message}
                </div>
              )}
              <SectionCards stats={dashboardQuery.data?.stats} />
              <div className="px-4 lg:px-6">
                <ChartAreaInteractive data={dashboardQuery.data?.chart ?? []} />
              </div>
              <RecentDocumentsTable documents={dashboardQuery.data?.recentDocuments ?? []} />
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}

export default Dashboard
