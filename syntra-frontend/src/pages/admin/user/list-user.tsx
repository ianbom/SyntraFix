import { useCallback, useMemo } from "react"
import { useQuery } from "@tanstack/react-query"
import { IconUserPlus } from "@tabler/icons-react"
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { Button } from "@/components/ui/button"
import { UserStatistics, UserTable } from "./components"
import { listAdminUsers } from "../api"
import type { User } from "./types"

const mapAdminUser = (user: Awaited<ReturnType<typeof listAdminUsers>>["users"][number]): User => ({
  id: String(user.id),
  nama: user.username,
  nrp: String(user.id),
  email: user.email,
  createdAt: user.created_at,
  status: user.is_active ? "active" : "inactive",
})

const UserListPage = () => {
  const usersQuery = useQuery({
    queryKey: ["admin-users"],
    queryFn: ({ signal }) => listAdminUsers({ perPage: 100, signal }),
  })

  const users = useMemo(
    () => usersQuery.data?.users.map(mapAdminUser) ?? [],
    [usersQuery.data?.users]
  )

  const handleView = useCallback((user: User) => {
    console.log("View user:", user.id)
  }, [])

  const handleEdit = useCallback((user: User) => {
    console.log("Edit user:", user.id)
  }, [])

  const handleDelete = useCallback((user: User) => {
    console.log("Delete user:", user.id)
  }, [])

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
            <div className="flex flex-col gap-6 py-4 md:py-6">
              <div className="flex items-center justify-between px-4 lg:px-6">
                <div>
                  <h1 className="text-2xl font-bold tracking-tight">
                    Daftar User
                  </h1>
                  <p className="text-muted-foreground">
                    Kelola semua user yang terdaftar di sistem
                  </p>
                </div>
                <Button>
                  <IconUserPlus className="size-4" />
                  Tambah User
                </Button>
              </div>

              {usersQuery.isError && (
                <div className="mx-4 rounded-lg border border-destructive/40 bg-destructive/10 px-4 py-3 text-sm text-destructive lg:mx-6">
                  {(usersQuery.error as Error).message}
                </div>
              )}

              {usersQuery.isLoading && (
                <div className="mx-4 rounded-lg border px-4 py-3 text-sm text-muted-foreground lg:mx-6">
                  Memuat data user...
                </div>
              )}

              <UserStatistics users={users} />

              <UserTable
                users={users}
                onView={handleView}
                onEdit={handleEdit}
                onDelete={handleDelete}
              />
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}

export default UserListPage
