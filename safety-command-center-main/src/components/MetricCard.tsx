import { LucideIcon } from "lucide-react";

interface MetricCardProps {
  title: string;
  value: number;
  icon: LucideIcon;
  variant: "primary" | "warning" | "success" | "default";
  delay?: number;
}

const variantStyles = {
  primary: "border-primary/30 glow-primary",
  warning: "border-warning/30 glow-warning",
  success: "border-success/30 glow-success",
  default: "border-border/50",
};

const iconStyles = {
  primary: "text-primary",
  warning: "text-warning",
  success: "text-success",
  default: "text-muted-foreground",
};

export function MetricCard({ title, value, icon: Icon, variant, delay = 0 }: MetricCardProps) {
  return (
    <div
      className={`glass-card-hover p-5 ${variantStyles[variant]} opacity-0 animate-fade-in`}
      style={{ animationDelay: `${delay}ms` }}
    >
      <div className="flex items-center justify-between mb-3">
        <span className="text-xs uppercase tracking-widest text-muted-foreground font-medium">
          {title}
        </span>
        <Icon className={`h-5 w-5 ${iconStyles[variant]}`} />
      </div>
      <div className="flex items-baseline gap-1">
        <span className="text-3xl font-bold font-mono tracking-tight">
          {value.toLocaleString()}
        </span>
      </div>
    </div>
  );
}
