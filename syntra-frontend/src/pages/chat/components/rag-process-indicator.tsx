import { IconRobot } from "@tabler/icons-react"
import { cn } from "@/lib/utils"
import type { ChatStreamStatusEvent } from "../api"

interface RagProcessIndicatorProps {
  steps: ChatStreamStatusEvent[]
}

const DEFAULT_STEPS: ChatStreamStatusEvent[] = [
  {
    type: "status",
    step: "query_processing",
    label: "Memahami pertanyaan",
    status: "running",
  },
]

export function RagProcessIndicator({ steps }: RagProcessIndicatorProps) {
  const visibleSteps = steps.length > 0 ? steps : DEFAULT_STEPS

  return (
    <div className="mr-auto flex max-w-[95%] gap-3">
      <div className="flex size-8 shrink-0 items-center justify-center rounded-full bg-muted">
        <IconRobot className="size-4" />
      </div>
      <div className="flex min-w-0 flex-1 flex-col gap-2 rounded-2xl rounded-bl-md bg-muted px-4 py-3">
        <p className="text-sm font-medium">Mencari data relevan...</p>
        <div className="space-y-2">
          {visibleSteps.map((step) => {
            const isCompleted = step.status === "completed"

            return (
              <div key={step.step} className="flex items-center gap-2 text-sm">
                <span
                  className={cn(
                    "flex size-4 shrink-0 items-center justify-center rounded-full border",
                    isCompleted
                      ? "border-primary bg-primary text-primary-foreground"
                      : "border-primary/40"
                  )}
                >
                  {isCompleted ? (
                    <span className="text-[10px] leading-none">✓</span>
                  ) : (
                    <span className="size-2 animate-pulse rounded-full bg-primary" />
                  )}
                </span>
                <span
                  className={cn(
                    isCompleted ? "text-muted-foreground" : "text-foreground"
                  )}
                >
                  {step.label}
                </span>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
