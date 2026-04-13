import { useMemo } from "react"
import {
  IconFileText,
  IconFileCheck,
  IconFilePencil,
  IconClock,
} from "@tabler/icons-react"
import { Card, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import type { DocumentListItem } from "../types"

interface StatCardProps {
  title: string
  value: number
  icon: typeof IconFileText
  description: string
}

function StatCard({ title, value, icon: Icon, description }: StatCardProps) {
  return (
    <Card className="@container/card">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardDescription>{title}</CardDescription>
          <Icon className="size-5 text-muted-foreground" />
        </div>
        <CardTitle className="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          {value}
        </CardTitle>
        <p className="text-xs text-muted-foreground">{description}</p>
      </CardHeader>
    </Card>
  )
}

interface DocumentStatisticsProps {
  documents: DocumentListItem[]
  totalDocuments: number
}

export function DocumentStatistics({ documents, totalDocuments }: DocumentStatisticsProps) {
  const stats = useMemo(() => {
    const currentPage = documents.length
    const privateDocuments = documents.filter((d) => d.isPrivate).length
    const withDoi = documents.filter((d) => Boolean(d.doi)).length

    return {
      total: totalDocuments,
      currentPage,
      privateDocuments,
      withDoi,
    }
  }, [documents, totalDocuments])

  return (
    <div className="grid grid-cols-1 gap-4 px-4 sm:grid-cols-2 lg:grid-cols-4 lg:px-6">
      <StatCard
        title="Total Dokumen"
        value={stats.total}
        icon={IconFileText}
        description="Jumlah dokumen dari API"
      />
      <StatCard
        title="Halaman Aktif"
        value={stats.currentPage}
        icon={IconFileCheck}
        description="Dokumen yang sedang ditampilkan"
      />
      <StatCard
        title="Dokumen Private"
        value={stats.privateDocuments}
        icon={IconFilePencil}
        description="Dokumen private di halaman aktif"
      />
      <StatCard
        title="Memiliki DOI"
        value={stats.withDoi}
        icon={IconClock}
        description="Dokumen dengan DOI di halaman aktif"
      />
    </div>
  )
}
