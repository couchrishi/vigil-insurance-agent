import { Mail, Car, Wrench, CheckCircle2 } from "lucide-react";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";

interface ActionStepperProps {
  notificationSent: boolean;
  rideBooked: boolean;
  repairScheduled: boolean;
  fixed: boolean;
}

export function ActionStepper({ notificationSent, rideBooked, repairScheduled, fixed }: ActionStepperProps) {
  const steps = [
    { icon: Mail, active: notificationSent, label: "Notification Sent", color: "primary" as const },
    { icon: Car, active: rideBooked, label: "Waymo Dispatched", color: "warning" as const },
    { icon: Wrench, active: repairScheduled, label: "Dealer Booked", color: "primary" as const },
    { icon: CheckCircle2, active: fixed, label: "Resolved", color: "success" as const },
  ];

  const colorMap = {
    primary: { bg: "bg-primary/15", text: "text-primary", line: "bg-primary/40", glow: "shadow-[0_0_8px_rgba(56,189,248,0.4)]" },
    warning: { bg: "bg-warning/15", text: "text-warning", line: "bg-warning/40", glow: "shadow-[0_0_8px_rgba(251,191,36,0.4)]" },
    success: { bg: "bg-success/15", text: "text-success", line: "bg-success/40", glow: "shadow-[0_0_8px_rgba(16,185,129,0.4)]" },
  };

  // Determine which step is "currently active" (last true before first false)
  const activeIndex = steps.reduce((acc, step, i) => (step.active ? i : acc), -1);
  const isInProgress = (i: number) => i === activeIndex && !fixed;

  return (
    <div className="flex items-center gap-1">
      {steps.map((step, i) => {
        const c = colorMap[step.color];
        const pulsing = isInProgress(i);
        return (
          <div key={i} className="flex items-center">
            <Tooltip>
              <TooltipTrigger>
                <div className={`p-1.5 rounded-md transition-all duration-300 ${
                  step.active
                    ? `${c.bg} ${c.text} ${pulsing ? `animate-pulse ${c.glow}` : ""}`
                    : "bg-muted/50 text-muted-foreground/30"
                }`}>
                  <step.icon className="h-4 w-4" />
                </div>
              </TooltipTrigger>
              <TooltipContent side="top" className="text-xs">
                {step.label}: {step.active ? (pulsing ? "⚡ In Progress" : "✓ Complete") : "Pending"}
              </TooltipContent>
            </Tooltip>
            {i < steps.length - 1 && (
              <div className={`w-4 h-0.5 mx-0.5 rounded-full transition-colors ${
                step.active ? c.line : "bg-muted-foreground/15"
              }`} />
            )}
          </div>
        );
      })}
    </div>
  );
}
