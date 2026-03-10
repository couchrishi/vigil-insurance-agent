interface SeverityBadgeProps {
  severity: "Critical" | "High Risk" | "Urgent" | "Standard";
}

const badgeStyles: Record<string, string> = {
  Critical: "bg-destructive/15 text-destructive border-destructive/30",
  "High Risk": "bg-warning/15 text-warning border-warning/30",
  Urgent: "bg-primary/15 text-primary border-primary/30",
  Standard: "bg-success/15 text-success border-success/30",
};

export function SeverityBadge({ severity }: SeverityBadgeProps) {
  return (
    <span className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold border ${badgeStyles[severity]}`}>
      <span className={`h-1.5 w-1.5 rounded-full ${
        severity === "Critical" ? "bg-destructive" :
        severity === "High Risk" ? "bg-warning" :
        severity === "Urgent" ? "bg-primary" : "bg-success"
      }`} />
      {severity}
    </span>
  );
}
