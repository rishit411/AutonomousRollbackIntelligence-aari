import { RadialBarChart, RadialBar, PolarAngleAxis } from "recharts";

export default function RiskGauge({ risk }) {

  const percentage = Math.round(risk * 100);

  let color = "#22c55e"; // green
  if (risk >= 0.8) color = "#ef4444";
  else if (risk >= 0.6) color = "#f97316";
  else if (risk >= 0.3) color = "#eab308";

  const data = [{ name: "risk", value: percentage }];

  return (
    <div style={{ width: 300, height: 250 }}>
      <RadialBarChart
        width={300}
        height={250}
        innerRadius="80%"
        outerRadius="100%"
        data={data}
        startAngle={180}
        endAngle={0}
      >
        <PolarAngleAxis
          type="number"
          domain={[0, 100]}
          tick={false}
        />
        <RadialBar
          dataKey="value"
          cornerRadius={10}
          fill={color}
        />
      </RadialBarChart>

      <div style={{
        textAlign: "center",
        marginTop: "-150px",
        fontSize: "24px",
        fontWeight: "bold"
      }}>
        {percentage}%
      </div>
    </div>
  );
}
