import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

const TelemetryChart = ({ telemetry }) => {
  if (!telemetry) return null;

  const data = [
    {
      stage: "Before",
      cpu: telemetry.before.cpu,
      latency: telemetry.before.latency,
      error: telemetry.before.error_rate,
    },
    {
      stage: "After",
      cpu: telemetry.after.cpu,
      latency: telemetry.after.latency,
      error: telemetry.after.error_rate,
    },
  ];

  return (
    <div style={{
      background: "#1f2a44",
      padding: "20px",
      borderRadius: "10px",
      marginTop: "20px"
    }}>
      <h3 style={{ marginBottom: "20px" }}>Telemetry Drift</h3>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="stage" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="cpu" stroke="#00bfff" />
          <Line type="monotone" dataKey="latency" stroke="#ffa500" />
          <Line type="monotone" dataKey="error" stroke="#ff4d4f" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default TelemetryChart;
