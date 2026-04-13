import { type CSSProperties } from "react"
import { useNavigate } from "react-router-dom"
import {
  IconBulb,
  IconFileText,
  IconMessagePlus,
  IconSparkles,
} from "@tabler/icons-react"
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { ChatInput } from "./components"

const PENDING_CHAT_PATH = "/chat/pending"

const guideCards = [
  {
    title: "Jelaskan Konsep",
    description: "Minta penjelasan topik dengan bahasa yang mudah dipahami.",
    icon: IconBulb,
  },
  {
    title: "Analisis Dokumen",
    description: "Tanyakan isi dokumen atau minta ringkasan poin penting.",
    icon: IconFileText,
  },
  {
    title: "Bantuan Cepat",
    description: "Dapatkan jawaban praktis untuk kebutuhan kerja harian.",
    icon: IconMessagePlus,
  },
]

const NewChatPage = () => {
  const navigate = useNavigate()

  const handleSendMessage = (message: string) => {
    navigate(PENDING_CHAT_PATH, {
      state: {
        initialMessage: message,
      },
    })
  }

  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "calc(var(--spacing) * 72)",
          "--header-height": "calc(var(--spacing) * 12)",
        } as CSSProperties
      }
    >
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
        <div className="flex flex-1 flex-col px-4 py-6 md:px-6 md:py-8">
          <div className="mx-auto flex w-full max-w-4xl flex-1 flex-col justify-center gap-6">
            <Card className="border-border/60 bg-card/90">
              <CardHeader className="space-y-4 text-center">
                <div className="mx-auto flex size-14 items-center justify-center rounded-full bg-primary/10">
                  <IconSparkles className="size-7 text-primary" />
                </div>
                <CardTitle className="text-2xl md:text-3xl">Mulai Percakapan Baru</CardTitle>
                <CardDescription className="mx-auto max-w-2xl text-sm md:text-base">
                  Tulis pertanyaan atau kebutuhanmu, lalu asisten akan langsung membantu dari
                  percakapan pertama.
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-3">
                <ChatInput
                  onSend={handleSendMessage}
                  placeholder="Ketik pesan untuk memulai percakapan..."
                  autoFocus
                />
                <p className="text-center text-xs text-muted-foreground">
                  Tekan Enter untuk kirim, Shift + Enter untuk menambah baris.
                </p>
              </CardContent>
            </Card>

            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {guideCards.map((item) => {
                const Icon = item.icon

                return (
                  <Card key={item.title} className="border-border/60 bg-card/70">
                    <CardContent className="flex items-start gap-3 p-4">
                      <div className="mt-0.5 rounded-md bg-primary/10 p-2">
                        <Icon className="size-4 text-primary" />
                      </div>
                      <div className="space-y-1">
                        <p className="text-sm font-medium">{item.title}</p>
                        <p className="text-xs text-muted-foreground">{item.description}</p>
                      </div>
                    </CardContent>
                  </Card>
                )
              })}
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}

export default NewChatPage
