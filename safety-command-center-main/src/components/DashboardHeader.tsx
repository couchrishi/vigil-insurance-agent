import { Rocket, FastForward } from "lucide-react";
import { Button } from "@/components/ui/button";

interface DashboardHeaderProps {
  onRunAudit: () => void;
  isAuditing: boolean;
  onSimulate: () => void;
  isSimulating: boolean;
}

export function DashboardHeader({ onRunAudit, isAuditing, onSimulate, isSimulating }: DashboardHeaderProps) {
  return (
    <header className="flex items-center justify-between px-6 py-6 glass-card rounded-none border-x-0 border-t-0">
      <div className="flex items-center gap-4">
        <div>
          <h1 className="text-4xl font-bold tracking-tight">
            Vigil Insurance
          </h1>
          <p className="text-xl text-muted-foreground font-medium mt-1">
            Proactive Safety Command Center
          </p>
          <div className="flex items-center gap-2 mt-1">
            <span className="relative flex h-2.5 w-2.5">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-success opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-success"></span>
            </span>
            <span className="text-xs text-muted-foreground font-medium">
              Background Agent: <span className="text-success">Active</span>
            </span>
          </div>
        </div>
      </div>

      <div className="flex items-center gap-3">
        <Button
          onClick={onSimulate}
          disabled={isSimulating}
          variant="outline"
          className="border-warning/40 text-warning hover:bg-warning/10 hover:text-warning font-semibold px-5"
          size="lg"
        >
          {isSimulating ? (
            <>
              <div className="h-4 w-4 border-2 border-warning/30 border-t-warning rounded-full animate-spin mr-2" />
              Simulating...
            </>
          ) : (
            <>
              <FastForward className="mr-2 h-4 w-4" />
              Fast Forward 30 Days
            </>
          )}
        </Button>

        <Button
          onClick={onRunAudit}
          disabled={isAuditing}
          className="bg-primary text-primary-foreground hover:bg-primary/90 font-semibold px-6 glow-primary"
          size="lg"
        >
          {isAuditing ? (
            <>
              <div className="h-4 w-4 border-2 border-primary-foreground/30 border-t-primary-foreground rounded-full animate-spin mr-2" />
              Scanning NHTSA API...
            </>
          ) : (
            <>
              <Rocket className="mr-2 h-4 w-4" />
              Run Global Safety Audit
            </>
          )}
        </Button>
      </div>
    </header>
  );
}
