import { useState, useCallback, useEffect, useRef } from "react";
import { Shield, Car, Wrench, CheckCircle2 } from "lucide-react";
import { DashboardHeader } from "@/components/DashboardHeader";
import { MetricCard } from "@/components/MetricCard";
import { LifecycleTable } from "@/components/LifecycleTable";
import { ActivityFeed } from "@/components/ActivityFeed";
import { mockPolicyholders, metrics as mockMetrics } from "@/lib/mock-data";
import { useToast } from "@/hooks/use-toast";

const API_BASE = "http://localhost:8081";

interface LogEntry {
  timestamp: string;
  agent: string;
  action: string;
}

const Index = () => {
  const [isAuditing, setIsAuditing] = useState(false);
  const [isSimulating, setIsSimulating] = useState(false);
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [policyholders, setPolicyholders] = useState(mockPolicyholders);
  const [isLive, setIsLive] = useState(false);
  const { toast } = useToast();
  const pollRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Poll /api/logs and /api/data every 3 seconds
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch Logs
        const logRes = await fetch(`${API_BASE}/api/logs`);
        if (logRes.ok) {
          const logData = await logRes.json();
          if (Array.isArray(logData) && logData.length > 0) {
            setLogs(logData);
            setIsLive(true);
          }
        }

        // Fetch Policyholders
        const dataRes = await fetch(`${API_BASE}/api/data`);
        if (dataRes.ok) {
          const data = await dataRes.json();
          if (Array.isArray(data) && data.length > 0) {
            setPolicyholders(data);
          }
        }
      } catch {
        // Backend not available — silently use current state
      }
    };

    fetchData();
    pollRef.current = setInterval(fetchData, 3000);
    return () => {
      if (pollRef.current) clearInterval(pollRef.current);
    };
  }, []);

  const handleRunAudit = useCallback(async () => {
    setIsAuditing(true);
    try {
      await fetch(`${API_BASE}/api/trigger`, { method: "POST" });
      toast({
        title: "Safety Audit Triggered",
        description: "Scanning NHTSA API for new recalls...",
      });
    } catch {
      toast({
        title: "Audit Running (Demo)",
        description: "Backend not connected — running in demo mode.",
      });
    }
    setTimeout(() => setIsAuditing(false), 4000);
  }, [toast]);

  const handleSimulate = useCallback(async () => {
    setIsSimulating(true);
    toast({
      title: "⏳ Time Simulation Active",
      description: "Checking for uncompleted repairs over 30 days...",
    });
    try {
      await fetch(`${API_BASE}/api/simulate/30days`, { method: "POST" });
    } catch {
      // Demo mode
    }
    setTimeout(() => setIsSimulating(false), 5000);
  }, [toast]);

  // Derive metrics from live data
  const metrics = {
    currentExposure: policyholders.length, 
    activeDispatches: policyholders.filter(p => p.ride_booked && !p.fixed).length,
    negotiatedRepairs: policyholders.filter(p => p.repair_scheduled && !p.fixed).length,
    resolvedRisks: policyholders.filter(p => p.fixed).length + 142, // Start from base 142
  };

  return (
    <div className="min-h-screen bg-background">
      <DashboardHeader
        onRunAudit={handleRunAudit}
        isAuditing={isAuditing}
        onSimulate={handleSimulate}
        isSimulating={isSimulating}
      />

      <div className="p-6 space-y-6">
        {/* Hero Metrics */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <MetricCard title="Current Exposure" value={metrics.currentExposure} icon={Shield} variant="warning" delay={0} />
          <MetricCard title="Active Dispatches" value={metrics.activeDispatches} icon={Car} variant="primary" delay={80} />
          <MetricCard title="Negotiated Repairs" value={metrics.negotiatedRepairs} icon={Wrench} variant="default" delay={160} />
          <MetricCard title="Resolved Risks" value={metrics.resolvedRisks} icon={CheckCircle2} variant="success" delay={240} />
        </div>

        {/* Main Content: Table + Activity Feed */}
        <div className="grid grid-cols-1 xl:grid-cols-[1fr_380px] gap-6">
          <LifecycleTable data={policyholders} />
          <ActivityFeed logs={logs} isLive={isLive} />
        </div>
      </div>
    </div>
  );
};

export default Index;
