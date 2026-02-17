import { useState } from "react";
import axios from "axios";

import RiskGauge from "./components/RiskGauge";
import DependencyGraph from "./components/DependencyGraph";
import TelemetryChart from "./components/TelemetryChart";

export default function App() {

  const [service, setService] = useState("orders");
  const [changeType, setChangeType] = useState("iam");
  const [impactScope, setImpactScope] = useState("cross");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const deploy = async () => {
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:8000/deploy", {
        service_name: service,
        change_type: changeType,
        impact_scope: impactScope
      });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Backend error. Check console.");
    }
    setLoading(false);
  };

  return (
    <div style={{
      background: "#0f172a",
      minHeight: "100vh",
      padding: "40px",
      color: "white",
      fontFamily: "Segoe UI, sans-serif"
    }}>

      <h1 style={{
        fontSize: "28px",
        color: "#3b82f6",
        marginBottom: "30px"
      }}>
        Azure Autonomous Rollback Intelligence
      </h1>

      {/* CONTROL PANEL */}
      <div style={{
        background: "#1e293b",
        padding: "20px",
        borderRadius: "8px",
        marginBottom: "30px"
      }}>

        <h2 style={{ marginBottom: "15px" }}>Deployment Configuration</h2>

        <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>

          <div>
            <label>Service</label><br />
            <select value={service} onChange={e => setService(e.target.value)}>
              <option value="auth">auth</option>
              <option value="orders">orders</option>
              <option value="gateway">gateway</option>
              <option value="billing">billing</option>
              <option value="payment">payment</option>
              <option value="inventory">inventory</option>
              <option value="search">search</option>
              <option value="analytics">analytics</option>
            </select>
          </div>

          <div>
            <label>Change Type</label><br />
            <select value={changeType} onChange={e => setChangeType(e.target.value)}>
              <option value="iam">iam</option>
              <option value="network">network</option>
              <option value="autoscale">autoscale</option>
            </select>
          </div>

          <div>
            <label>Impact Scope</label><br />
            <select value={impactScope} onChange={e => setImpactScope(e.target.value)}>
              <option value="single">single</option>
              <option value="cross">cross</option>
            </select>
          </div>

          <div style={{ alignSelf: "end" }}>
            <button
              onClick={deploy}
              style={{
                background: "#2563eb",
                padding: "10px 20px",
                borderRadius: "6px",
                border: "none",
                cursor: "pointer"
              }}
            >
              {loading ? "Simulating..." : "Simulate Deployment"}
            </button>
          </div>

        </div>
      </div>

      {/* RESULTS */}
      {result && (
        <div style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "20px"
        }}>

          {/* RISK PANEL */}
          <div style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "8px"
          }}>
            <h2>Risk Assessment</h2>
            <RiskGauge risk={result.posterior_risk} />
            <p style={{ marginTop: "10px" }}>
              <strong>Strategy:</strong> {result.strategy.strategy}
            </p>
          </div>

          {/* DEPENDENCY GRAPH */}
          <div style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "8px"
          }}>
            <h2>Dependency Cascade</h2>
            <DependencyGraph impacted={result.impacted_services} />
          </div>

          {/* TELEMETRY PANEL */}
          <div style={{
            gridColumn: "span 2"
          }}>
            {result.telemetry && (
              <TelemetryChart telemetry={result.telemetry} />
            )}
          </div>

          {/* AI EXPLANATION */}
          <div style={{
            gridColumn: "span 2",
            background: "#1e293b",
            padding: "20px",
            borderRadius: "8px"
          }}>
            <h2>AI Root Cause Analysis</h2>
            <div style={{
              whiteSpace: "pre-wrap",
              fontSize: "14px",
              lineHeight: "1.5"
            }}>
              {result.explanation}
            </div>
          </div>

        </div>
      )}

    </div>
  );
}
