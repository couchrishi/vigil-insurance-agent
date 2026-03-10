import { useEffect, useRef } from "react";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Activity } from "lucide-react";

interface LogEntry {
  timestamp: string;
  agent: string;
  action: string;
}

interface ActivityFeedProps {
  logs: LogEntry[];
  isLive: boolean;
}

const agentColors: Record<string, string> = {
  MonitorAgent: "text-primary border-l-primary",
  TriageAgent: "text-warning border-l-warning",
  OutreachAgent: "text-success border-l-success",
  DealerAgent: "text-primary border-l-primary",
  "A2A Partner": "text-warning border-l-warning",
  System: "text-muted-foreground border-l-muted-foreground",
};

function getAgentStyle(agent: string) {
  for (const key of Object.keys(agentColors)) {
    if (agent.toLowerCase().includes(key.toLowerCase())) return agentColors[key];
  }
  return "text-primary border-l-primary/50";
}

export function ActivityFeed({ logs, isLive }: ActivityFeedProps) {
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [logs.length]);

  return (
    <div className="glass-card h-[700px] flex flex-col">
      <div className="px-4 py-3 border-b border-border/50 flex items-center gap-2">
        <Activity className="h-4 w-4 text-primary" />
        <h2 className="text-sm font-semibold uppercase tracking-widest text-muted-foreground">
          Autonomous Agent Activity
        </h2>
        {isLive && (
          <span className="ml-auto relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-primary"></span>
          </span>
        )}
      </div>
      <div 
        ref={scrollRef}
        className="flex-1 overflow-y-auto p-3 scrollbar-none"
        style={{ scrollBehavior: 'smooth' }}
      >
        <div className="space-y-2">
          {logs.length === 0 && (
            <p className="text-xs text-muted-foreground text-center py-8">
              Waiting for agent activity...
            </p>
          )}
          {logs.map((log, i) => {
            const style = getAgentStyle(log.agent);
            const textClass = style.split(" ")[0];
            const borderClass = style.split(" ").slice(1).join(" ");
            return (
              <div
                key={i}
                className={`border-l-2 ${borderClass} pl-3 py-2 rounded-r-md bg-muted/20 animate-fade-in`}
              >
                <div className="flex items-center gap-2 mb-0.5">
                  <span className="text-[10px] font-mono text-muted-foreground">{log.timestamp}</span>
                  <span className={`text-[10px] font-semibold uppercase tracking-wider ${textClass}`}>
                    {log.agent}
                  </span>
                </div>
                <p className="text-xs text-foreground/80 leading-relaxed">{log.action}</p>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
