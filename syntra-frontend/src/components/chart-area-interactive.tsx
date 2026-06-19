"use client"

import * as React from "react"
import { Area, AreaChart, CartesianGrid, XAxis } from "recharts"

import { useIsMobile } from "@/hooks/use-mobile"
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  type ChartConfig,
} from "@/components/ui/chart"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import {
  ToggleGroup,
  ToggleGroupItem,
} from "@/components/ui/toggle-group"
import type { AdminDashboardChartPoint } from "@/pages/admin/api"

export const description = "Admin activity chart"

const chartConfig = {
  activity: {
    label: "Aktivitas",
  },
  users: {
    label: "User",
    color: "var(--primary)",
  },
  documents: {
    label: "Dokumen",
    color: "var(--chart-2)",
  },
  chats: {
    label: "Chat",
    color: "var(--chart-3)",
  },
} satisfies ChartConfig

interface ChartAreaInteractiveProps {
  data?: AdminDashboardChartPoint[]
}

export function ChartAreaInteractive({ data = [] }: ChartAreaInteractiveProps) {
  const isMobile = useIsMobile()
  const [timeRange, setTimeRange] = React.useState("30d")

  React.useEffect(() => {
    if (isMobile) {
      setTimeRange("7d")
    }
  }, [isMobile])

  const filteredData = React.useMemo(() => {
    if (data.length === 0) {
      return []
    }

    const referenceDate = new Date(data[data.length - 1].date)
    let daysToSubtract = 30
    if (timeRange === "14d") {
      daysToSubtract = 14
    } else if (timeRange === "7d") {
      daysToSubtract = 7
    }

    const startDate = new Date(referenceDate)
    startDate.setDate(startDate.getDate() - daysToSubtract)

    return data.filter((item) => new Date(item.date) >= startDate)
  }, [data, timeRange])

  return (
    <Card className="@container/card">
      <CardHeader>
        <CardTitle>Aktivitas Sistem</CardTitle>
        <CardDescription>
          <span className="hidden @[540px]/card:block">
            User, dokumen, dan chat berdasarkan data backend
          </span>
          <span className="@[540px]/card:hidden">Data backend</span>
        </CardDescription>
        <CardAction>
          <ToggleGroup
            type="single"
            value={timeRange}
            onValueChange={(value) => value && setTimeRange(value)}
            variant="outline"
            className="hidden *:data-[slot=toggle-group-item]:!px-4 @[767px]/card:flex"
          >
            <ToggleGroupItem value="30d">30 hari</ToggleGroupItem>
            <ToggleGroupItem value="14d">14 hari</ToggleGroupItem>
            <ToggleGroupItem value="7d">7 hari</ToggleGroupItem>
          </ToggleGroup>
          <Select value={timeRange} onValueChange={setTimeRange}>
            <SelectTrigger
              className="flex w-32 **:data-[slot=select-value]:block **:data-[slot=select-value]:truncate @[767px]/card:hidden"
              size="sm"
              aria-label="Pilih rentang waktu"
            >
              <SelectValue placeholder="30 hari" />
            </SelectTrigger>
            <SelectContent className="rounded-xl">
              <SelectItem value="30d" className="rounded-lg">30 hari</SelectItem>
              <SelectItem value="14d" className="rounded-lg">14 hari</SelectItem>
              <SelectItem value="7d" className="rounded-lg">7 hari</SelectItem>
            </SelectContent>
          </Select>
        </CardAction>
      </CardHeader>
      <CardContent className="px-2 pt-4 sm:px-6 sm:pt-6">
        <ChartContainer
          config={chartConfig}
          className="aspect-auto h-[250px] w-full"
        >
          <AreaChart data={filteredData}>
            <defs>
              <linearGradient id="fillUsers" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="var(--color-users)" stopOpacity={0.9} />
                <stop offset="95%" stopColor="var(--color-users)" stopOpacity={0.1} />
              </linearGradient>
              <linearGradient id="fillDocuments" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="var(--color-documents)" stopOpacity={0.8} />
                <stop offset="95%" stopColor="var(--color-documents)" stopOpacity={0.1} />
              </linearGradient>
              <linearGradient id="fillChats" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="var(--color-chats)" stopOpacity={0.7} />
                <stop offset="95%" stopColor="var(--color-chats)" stopOpacity={0.1} />
              </linearGradient>
            </defs>
            <CartesianGrid vertical={false} />
            <XAxis
              dataKey="date"
              tickLine={false}
              axisLine={false}
              tickMargin={8}
              minTickGap={32}
              tickFormatter={(value) => {
                const date = new Date(value)
                return date.toLocaleDateString("id-ID", {
                  month: "short",
                  day: "numeric",
                })
              }}
            />
            <ChartTooltip
              cursor={false}
              content={
                <ChartTooltipContent
                  labelFormatter={(value) => {
                    return new Date(value).toLocaleDateString("id-ID", {
                      month: "short",
                      day: "numeric",
                    })
                  }}
                  indicator="dot"
                />
              }
            />
            <Area dataKey="users" type="natural" fill="url(#fillUsers)" stroke="var(--color-users)" stackId="a" />
            <Area dataKey="documents" type="natural" fill="url(#fillDocuments)" stroke="var(--color-documents)" stackId="a" />
            <Area dataKey="chats" type="natural" fill="url(#fillChats)" stroke="var(--color-chats)" stackId="a" />
          </AreaChart>
        </ChartContainer>
      </CardContent>
    </Card>
  )
}
