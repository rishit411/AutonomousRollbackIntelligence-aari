import ReactFlow, { Background } from "reactflow";
import "reactflow/dist/style.css";

export default function DependencyGraph({ impacted }) {

  const nodes = [
    { id: "orders", position: { x: 100, y: 100 }, data: { label: "Orders" } },
    { id: "payment", position: { x: 300, y: 100 }, data: { label: "Payment" } },
    { id: "inventory", position: { x: 300, y: 250 }, data: { label: "Inventory" } },
    { id: "gateway", position: { x: 100, y: 250 }, data: { label: "Gateway" } },
  ].map(node => ({
    ...node,
    style: {
      background: impacted?.includes(node.id) ? "#ef4444" : "#334155",
      color: "white",
      padding: 10,
      borderRadius: 8
    }
  }));

  const edges = [
    { id: "e1", source: "orders", target: "payment" },
    { id: "e2", source: "orders", target: "inventory" },
    { id: "e3", source: "gateway", target: "orders" },
  ];

  return (
    <div style={{ width: "100%", height: 350 }}>
      <ReactFlow nodes={nodes} edges={edges} fitView>
        <Background />
      </ReactFlow>
    </div>
  );
}
