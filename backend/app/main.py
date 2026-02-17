from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.environment import create_environment
from app.models import DeploymentRequest
from app.agents.telemetry_agent import TelemetryAgent
from app.agents.anomaly_agent import AnomalyAgent
from app.agents.risk_agent import RiskAgent
from app.agents.cascade_agent import CascadeAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.explanation_agent import ExplanationAgent


# -------------------------
# Initialize App
# -------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Environment + Agents
# -------------------------

graph, services = create_environment()

telemetry_agent = TelemetryAgent()
anomaly_agent = AnomalyAgent()
risk_agent = RiskAgent()
cascade_agent = CascadeAgent()
strategy_agent = StrategyAgent()
explanation_agent = ExplanationAgent()


# =========================
# Deployment Endpoint
# =========================

@app.post("/deploy")
def deploy(request: DeploymentRequest):

    if request.service_name not in services:
        return {"error": "Service not found"}

    service = services[request.service_name]

    # 1️⃣ Prior Risk
    prior = risk_agent.compute_prior(
        service,
        request.change_type,
        request.impact_scope
    )

    # 2️⃣ Apply Telemetry Drift (returns arrays)
    service, before_metrics, after_metrics = telemetry_agent.apply_change(
        service,
        request.change_type
    )

    # 3️⃣ Detect Anomaly
    anomaly_detected = anomaly_agent.detect(service)

    # 4️⃣ Posterior Risk
    posterior = risk_agent.compute_posterior(
        prior,
        anomaly_detected
    )

    # 5️⃣ Cascade Simulation
    impacted = cascade_agent.simulate(
        graph,
        request.service_name
    )

    # 6️⃣ Strategy Recommendation
    strategy = strategy_agent.recommend(posterior)

    # 7️⃣ AI Explanation
    explanation = explanation_agent.explain(
        request.change_type,
        posterior,
        impacted,
        anomaly_detected
    )

    # =========================
    # Return Safe JSON
    # =========================

    return {
        "prior_risk": float(round(prior, 3)),
        "posterior_risk": float(round(posterior, 3)),
        "impacted_services": impacted,
        "strategy": strategy,
        "anomaly_detected": bool(anomaly_detected),
        "telemetry": {
            "before": {
                "cpu": before_metrics["cpu"].tolist(),
                "latency": before_metrics["latency"].tolist(),
                "error_rate": before_metrics["error_rate"].tolist()
            },
            "after": {
                "cpu": after_metrics["cpu"].tolist(),
                "latency": after_metrics["latency"].tolist(),
                "error_rate": after_metrics["error_rate"].tolist()
            }
        },
        "explanation": explanation
    }
