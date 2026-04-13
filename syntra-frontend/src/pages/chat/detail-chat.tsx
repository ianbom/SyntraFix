import { type CSSProperties, useEffect, useMemo, useRef, useState } from "react"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { useLocation, useNavigate, useParams, Link } from "react-router-dom"
import { IconPlus, IconRobot } from "@tabler/icons-react"
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { ChatInput, MessageBubble } from "./components"
import {
  getConversation,
  postChatStream,
  type ConversationDetail,
  type PostChatResult,
} from "./api"
import type { Message } from "./types"

interface PendingChatLocationState {
  initialMessage?: string
}

const PENDING_CHAT_ID = "pending"
const processedPendingLocationKeys = new Set<string>()

const DetailChatPage = () => {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const location = useLocation()
  const queryClient = useQueryClient()
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const [sendErrorMessage, setSendErrorMessage] = useState<string | null>(null)
  const [pendingRouteOptimisticMessage, setPendingRouteOptimisticMessage] = useState<Message | null>(null)
  const [streamingAssistantMessage, setStreamingAssistantMessage] = useState<Message | null>(null)

  const initialMessage = useMemo(() => {
    if (!location.state || typeof location.state !== "object") {
      return ""
    }

    const state = location.state as PendingChatLocationState
    return typeof state.initialMessage === "string"
      ? state.initialMessage.trim()
      : ""
  }, [location.state])

  const buildOptimisticUserMessage = (content: string): Message => ({
    id: `temp-user-${Date.now()}-${Math.random().toString(36).slice(2, 9)}`,
    content,
    role: "user",
    timestamp: new Date(),
  })

  const isCreatingConversationRoute = id === PENDING_CHAT_ID
  const parsedConversationId = Number(id)
  const conversationId =
    Number.isInteger(parsedConversationId) && parsedConversationId > 0
      ? parsedConversationId
      : null
  const isConversationIdValid = conversationId !== null

  useEffect(() => {
    if (!id) {
      navigate("/chat/new", { replace: true })
      return
    }

    if (isCreatingConversationRoute) {
      if (!initialMessage) {
        navigate("/chat/new", { replace: true })
      }

      return
    }

    if (!isConversationIdValid) {
      navigate("/chat/new", { replace: true })
    }
  }, [id, initialMessage, isConversationIdValid, isCreatingConversationRoute, navigate])

  const conversationQuery = useQuery({
    queryKey: ["chats", "conversation", conversationId],
    queryFn: ({ signal }) => {
      if (!conversationId) {
        throw new Error("ID percakapan tidak valid.")
      }

      return getConversation({ conversationId, signal })
    },
    enabled: isConversationIdValid,
  })

  const createConversationMutation = useMutation({
    mutationFn: async (message: string): Promise<PostChatResult> => {
      const assistantMessageId = `temp-assistant-${Date.now()}-${Math.random().toString(36).slice(2, 9)}`
      const assistantTimestamp = new Date()

      setStreamingAssistantMessage({
        id: assistantMessageId,
        content: "",
        role: "assistant",
        timestamp: assistantTimestamp,
      })

      return postChatStream({
        message,
        onChunk: (chunk) => {
          setStreamingAssistantMessage((currentMessage) => {
            if (!currentMessage || currentMessage.id !== assistantMessageId) {
              return {
                id: assistantMessageId,
                content: chunk,
                role: "assistant",
                timestamp: assistantTimestamp,
              }
            }

            return {
              ...currentMessage,
              content: `${currentMessage.content}${chunk}`,
            }
          })
        },
      })
    },
    onMutate: (message: string) => {
      setPendingRouteOptimisticMessage(buildOptimisticUserMessage(message))
    },
    onSuccess: async (response) => {
      setSendErrorMessage(null)
      setPendingRouteOptimisticMessage(null)

      await Promise.all([
        queryClient.invalidateQueries({
          queryKey: ["chats", "conversation", response.conversationId],
        }),
        queryClient.invalidateQueries({
          queryKey: ["chats", "conversations"],
        }),
      ])

      setStreamingAssistantMessage(null)
      navigate(`/chat/${response.conversationId}`, { replace: true })
    },
    onError: (error: unknown) => {
      setStreamingAssistantMessage(null)

      if (error instanceof Error) {
        setSendErrorMessage(error.message)
        return
      }

      setSendErrorMessage("Gagal memulai percakapan.")
    },
  })

  const {
    mutate: createConversation,
    isPending: isCreatingConversation,
    status: createConversationStatus,
  } = createConversationMutation

  useEffect(() => {
    if (!isCreatingConversationRoute || !initialMessage) {
      return
    }

    if (createConversationStatus !== "idle") {
      return
    }

    // Prevent duplicate initial request in StrictMode remount.
    if (processedPendingLocationKeys.has(location.key)) {
      return
    }

    processedPendingLocationKeys.add(location.key)
    createConversation(initialMessage)
  }, [
    createConversation,
    createConversationStatus,
    initialMessage,
    isCreatingConversationRoute,
    location.key,
  ])

  const sendMessageMutation = useMutation({
    mutationFn: async (message: string): Promise<PostChatResult> => {
      if (!conversationId) {
        throw new Error("ID percakapan tidak valid.")
      }

      const assistantMessageId = `temp-assistant-${Date.now()}-${Math.random().toString(36).slice(2, 9)}`
      const assistantTimestamp = new Date()

      setStreamingAssistantMessage({
        id: assistantMessageId,
        content: "",
        role: "assistant",
        timestamp: assistantTimestamp,
      })

      return postChatStream({
        message,
        conversationId,
        onChunk: (chunk) => {
          setStreamingAssistantMessage((currentMessage) => {
            if (!currentMessage || currentMessage.id !== assistantMessageId) {
              return {
                id: assistantMessageId,
                content: chunk,
                role: "assistant",
                timestamp: assistantTimestamp,
              }
            }

            return {
              ...currentMessage,
              content: `${currentMessage.content}${chunk}`,
            }
          })
        },
      })
    },
    onMutate: async (message: string) => {
      if (!conversationId) {
        return { previousConversation: undefined as ConversationDetail | undefined }
      }

      await queryClient.cancelQueries({
        queryKey: ["chats", "conversation", conversationId],
      })

      const previousConversation = queryClient.getQueryData<ConversationDetail>([
        "chats",
        "conversation",
        conversationId,
      ])

      const optimisticMessage = buildOptimisticUserMessage(message)

      queryClient.setQueryData<ConversationDetail>(
        ["chats", "conversation", conversationId],
        (currentConversation) => {
          if (!currentConversation) {
            return currentConversation
          }

          return {
            ...currentConversation,
            chats: [...currentConversation.chats, optimisticMessage],
          }
        }
      )

      return { previousConversation }
    },
    onSuccess: async () => {
      setSendErrorMessage(null)

      await Promise.all([
        queryClient.invalidateQueries({
          queryKey: ["chats", "conversation", conversationId],
        }),
        queryClient.invalidateQueries({
          queryKey: ["chats", "conversations"],
        }),
      ])

      setStreamingAssistantMessage(null)
    },
    onError: (error: unknown, _message, context) => {
      if (conversationId && context?.previousConversation) {
        queryClient.setQueryData(
          ["chats", "conversation", conversationId],
          context.previousConversation
        )
      }

      setStreamingAssistantMessage(null)

      if (error instanceof Error) {
        setSendErrorMessage(error.message)
        return
      }

      setSendErrorMessage("Gagal mengirim pesan.")
    },
  })

  const messages = useMemo<Message[]>(() => {
    const chats = conversationQuery.data?.chats ?? []
    const pendingRouteMessages =
      isCreatingConversationRoute && pendingRouteOptimisticMessage
        ? [pendingRouteOptimisticMessage]
        : []
    const streamingMessages = streamingAssistantMessage
      ? [streamingAssistantMessage]
      : []

    return [...chats, ...pendingRouteMessages, ...streamingMessages].sort(
      (firstMessage, secondMessage) => {
        const timestampDiff = firstMessage.timestamp.getTime() - secondMessage.timestamp.getTime()

        if (timestampDiff !== 0) {
          return timestampDiff
        }

        if (firstMessage.role === secondMessage.role) {
          return 0
        }

        return firstMessage.role === "user" ? -1 : 1
      }
    )
  }, [
    conversationQuery.data?.chats,
    isCreatingConversationRoute,
    pendingRouteOptimisticMessage,
    streamingAssistantMessage,
  ])

  const chatTitle =
    conversationQuery.data?.title ?? (isCreatingConversationRoute ? "Memulai chat..." : "Chat")
  const isBotTyping =
    (isCreatingConversationRoute && isCreatingConversation) || sendMessageMutation.isPending
  const isConversationLoading = isConversationIdValid && conversationQuery.isPending

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages, isBotTyping])

  const handleSendMessage = (content: string) => {
    if (isCreatingConversationRoute) {
      if (isCreatingConversation) {
        return
      }

      setSendErrorMessage(null)
      processedPendingLocationKeys.add(location.key)
      createConversation(content)
      return
    }

    if (!isConversationIdValid || sendMessageMutation.isPending) {
      return
    }

    setSendErrorMessage(null)
    sendMessageMutation.mutate(content)
  }

  const fetchErrorMessage =
    conversationQuery.error instanceof Error
      ? conversationQuery.error.message
      : "Gagal memuat percakapan."

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
        <div className="flex flex-1 flex-col">
          <div className="@container/main flex flex-1 flex-col">
            {/* Chat Header */}
            <div className="flex items-center justify-between border-b px-4 py-3 lg:px-6">
              <div className="flex items-center gap-2">
                <div className="flex size-8 items-center justify-center rounded-full bg-primary/10">
                  <IconRobot className="size-4 text-primary" />
                </div>
                <div>
                  <h1 className="line-clamp-1 max-w-[200px] text-sm font-semibold sm:max-w-md">
                    {chatTitle}
                  </h1>
                  <p className="text-xs text-muted-foreground">Syntra AI</p>
                </div>
              </div>

              <Link to="/chat/new">
                <Button variant="outline" size="sm">
                  <IconPlus className="size-4" />
                  <span className="ml-1 hidden sm:inline">Chat Baru</span>
                </Button>
              </Link>
            </div>

            {isConversationIdValid && conversationQuery.isError && (
              <div className="px-4 pt-4 lg:px-6">
                <div className="rounded-md bg-destructive/10 p-3 text-sm text-destructive">
                  {fetchErrorMessage}
                </div>
              </div>
            )}

            {sendErrorMessage && (
              <div className="px-4 pt-4 lg:px-6">
                <div className="rounded-md bg-destructive/10 p-3 text-sm text-destructive">
                  {sendErrorMessage}
                </div>
              </div>
            )}

            {/* Messages */}
            <div className="flex-1 overflow-y-auto px-4 py-6 lg:px-6">
              <div className="mx-auto max-w-3xl space-y-6">
                {isConversationLoading && (
                  <p className="text-center text-sm text-muted-foreground">
                    Memuat percakapan...
                  </p>
                )}

                {isCreatingConversationRoute && isCreatingConversation && (
                  <p className="text-center text-sm text-muted-foreground">
                    Memulai percakapan...
                  </p>
                )}

                {messages.map((message) => (
                  <MessageBubble key={message.id} message={message} />
                ))}

                {/* {isBotTyping && <TypingIndicator />} */}

                <div ref={messagesEndRef} />
              </div>
            </div>

            {/* Input */}
            <div className="border-t px-4 py-4 lg:px-6">
              <div className="mx-auto max-w-3xl">
                <Card className="p-0">
                  <ChatInput
                    onSend={handleSendMessage}
                    disabled={isConversationLoading || isBotTyping}
                    placeholder={
                      isBotTyping
                        ? "Menunggu respons..."
                        : isCreatingConversationRoute
                          ? "Ketik pesan untuk memulai percakapan..."
                          : "Ketik pesan..."
                    }
                  />
                </Card>
              </div>
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}

export default DetailChatPage
