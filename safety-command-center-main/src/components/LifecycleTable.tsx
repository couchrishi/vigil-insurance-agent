import { PolicyHolder } from "@/lib/mock-data";
import { SeverityBadge } from "./SeverityBadge";
import { ActionStepper } from "./ActionStepper";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

interface LifecycleTableProps {
  data: PolicyHolder[];
}

export function LifecycleTable({ data }: LifecycleTableProps) {
  return (
    <div className="glass-card overflow-hidden opacity-0 animate-fade-in" style={{ animationDelay: "300ms" }}>
      <div className="px-5 py-4 border-b border-border/50">
        <h2 className="text-sm font-semibold uppercase tracking-widest text-muted-foreground">
          Policyholder Lifecycle
        </h2>
      </div>
      <div className="overflow-x-auto">
        <Table>
          <TableHeader>
            <TableRow className="border-border/30 hover:bg-transparent">
              <TableHead className="text-xs uppercase tracking-wider text-muted-foreground">Policyholder</TableHead>
              <TableHead className="text-xs uppercase tracking-wider text-muted-foreground">Vehicle Info</TableHead>
              <TableHead className="text-xs uppercase tracking-wider text-muted-foreground">Severity</TableHead>
              <TableHead className="text-xs uppercase tracking-wider text-muted-foreground">AI Actions</TableHead>
              <TableHead className="text-xs uppercase tracking-wider text-muted-foreground">Current Status</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((row, i) => (
              <TableRow
                key={row.policy_id}
                className="border-border/20 hover:bg-accent/30 transition-colors opacity-0 animate-fade-in"
                style={{ animationDelay: `${400 + i * 60}ms` }}
              >
                <TableCell>
                  <div>
                    <p className="font-medium text-sm">{row.name}</p>
                    <p className="text-xs text-muted-foreground font-mono">{row.policy_id}</p>
                  </div>
                </TableCell>
                <TableCell>
                  <div>
                    <p className="text-sm">{row.vehicle}</p>
                    <p className="text-xs text-muted-foreground font-mono">{row.vin}</p>
                  </div>
                </TableCell>
                <TableCell>
                  <SeverityBadge severity={row.status} />
                </TableCell>
                <TableCell>
                  <ActionStepper
                    notificationSent={row.notification_sent}
                    rideBooked={row.ride_booked}
                    repairScheduled={row.repair_scheduled}
                    fixed={row.fixed}
                  />
                </TableCell>
                <TableCell>
                  <span className={`text-sm font-medium ${
                    row.fixed ? "text-success" : 
                    row.status === "Critical" ? "text-destructive" : "text-foreground"
                  }`}>
                    {row.current_status}
                  </span>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}
