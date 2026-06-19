import {
  IconFileDescription,
  IconMessageCircle,
  IconProgressCheck,
  IconUsers,
} from "@tabler/icons-react"

import {
  Card,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import type { AdminDashboardStats } from "@/pages/admin/api"

interface SectionCardsProps {
  stats?: AdminDashboardStats
}

interface StatCardProps {
  title: string
  value: number
  description: string
  detail: string
  icon: typeof IconUsers
}

function StatCard({ title, value, description, detail, icon: Icon }: StatCardProps) {
  return (
    <Card className="@container/card">
      <CardHeader>
        <div className="flex items-center justify-between gap-3">
          <CardDescription>{title}</CardDescription>
          <Icon className="size-5 text-muted-foreground" />
        </div>
        <CardTitle className="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          {value.toLocaleString("id-ID")}
        </CardTitle>
      </CardHeader>
      <CardFooter className="flex-col items-start gap-1.5 text-sm">
        <div className="line-clamp-1 font-medium">{description}</div>
        <div className="text-muted-foreground">{detail}</div>
      </CardFooter>
    </Card>
  )
}

export function SectionCards({ stats }: SectionCardsProps) {
  const safeStats: AdminDashboardStats = stats ?? {
    totalUsers: 0,
    activeUsers: 0,
    inactiveUsers: 0,
    newUsersThisMonth: 0,
    totalDocuments: 0,
    processedDocuments: 0,
    processingDocuments: 0,
    failedDocuments: 0,
    totalConversations: 0,
    totalChats: 0,
  }

  return (
    <div className="*:data-[slot=card]:from-primary/5 *:data-[slot=card]:to-card dark:*:data-[slot=card]:bg-card grid grid-cols-1 gap-4 px-4 *:data-[slot=card]:bg-gradient-to-t *:data-[slot=card]:shadow-xs lg:px-6 @xl/main:grid-cols-2 @5xl/main:grid-cols-4">
      <StatCard
        title="Total User"
        value={safeStats.totalUsers}
        description={`${safeStats.activeUsers.toLocaleString("id-ID")} user aktif`}
        detail={`${safeStats.newUsersThisMonth.toLocaleString("id-ID")} user baru bulan ini`}
        icon={IconUsers}
      />
      <StatCard
        title="Total Dokumen"
        value={safeStats.totalDocuments}
        description={`${safeStats.processedDocuments.toLocaleString("id-ID")} dokumen selesai diproses`}
        detail={`${safeStats.processingDocuments.toLocaleString("id-ID")} proses, ${safeStats.failedDocuments.toLocaleString("id-ID")} gagal`}
        icon={IconFileDescription}
      />
      <StatCard
        title="Percakapan"
        value={safeStats.totalConversations}
        description="Conversation tersimpan"
        detail={`${safeStats.totalChats.toLocaleString("id-ID")} total pesan chat`}
        icon={IconMessageCircle}
      />
      <StatCard
        title="Status Proses"
        value={safeStats.processingDocuments}
        description="Dokumen sedang diproses"
        detail={`${safeStats.inactiveUsers.toLocaleString("id-ID")} user tidak aktif`}
        icon={IconProgressCheck}
      />
    </div>
  )
}
