# AutonomousRollbackIntelligence-aari
# 🚀 AARI — Autonomous Azure Rollback Intelligence

> Predict deployment failures **before they reach production**

---

## 🧠 Overview

AARI (Autonomous Azure Rollback Intelligence) is an AI-powered decision engine that predicts the **probability of deployment failure before a release goes live**.

Modern cloud systems (Azure, AWS, GCP) are highly distributed and interdependent.
Most failures today are detected **after deployment**, when users are already impacted.

AARI flips that paradigm.

It simulates runtime behavior, models service dependencies, and recommends whether to:

* ✅ Proceed with deployment
* ⚠️ Roll out in phases
* ❌ Roll back immediately

---

## 🎯 Problem Statement

Cloud platforms provide powerful tools:

* Infrastructure previews (e.g., ARM What-If)
* Observability (metrics, logs, traces)
* Anomaly detection
* Rollback mechanisms

However, they are **reactive systems**.

They answer:

> “What changed?”
> “What broke?”

But not:

> **“Will this break before I deploy it?”**

AARI addresses this gap.

---

## ⚙️ How It Works

AARI follows a multi-agent decision pipeline:

```
Deployment Input
      ↓
Telemetry Simulation
      ↓
Anomaly Detection
      ↓
Risk Modeling (Prior → Posterior)
      ↓
Dependency Cascade Simulation
      ↓
Strategy Recommendation
      ↓
AI Root Cause Explanation
```

---

## 🧩 System Architecture

### 1️⃣ Telemetry Agent

Simulates how key runtime metrics change post-deployment:

* CPU usage
* Latency
* Error rate

---

### 2️⃣ Anomaly Agent

Detects whether simulated telemetry deviates from baseline behavior.

---

### 3️⃣ Risk Agent

Computes:

* **Prior Risk** → based on change type & scope
* **Posterior Risk** → updated using anomaly signals

Outputs a probabilistic failure score.

---

### 4️⃣ Cascade Agent

Models service dependencies and predicts **blast radius**.

Example:

> Payment fails → Orders → Billing → Notifications

---

### 5️⃣ Strategy Agent

Recommends action:

* Low Risk → Deploy
* Medium Risk → Phased Rollout
* High Risk → Rollback

---

### 6️⃣ Explanation Agent (LLM)

Uses Gemini API to generate:

* Root cause hypothesis
* Dependency impact
* Mitigation strategy

---

## ⚖️ How AARI Is Different

| Capability                    | Cloud Platforms  | AARI                        |
| ----------------------------- | ---------------- | --------------------------- |
| Infra Change Preview          | ✅                | ✅                           |
| Runtime Telemetry             | ✅ (after deploy) | ✅ (simulated before deploy) |
| Anomaly Detection             | ✅                | ✅                           |
| Dependency Visualization      | Partial          | Simulated cascade           |
| Probabilistic Risk Scoring    | ❌                | ✅                           |
| Pre-deploy Failure Prediction | ❌                | ✅                           |
| Automated Decision Engine     | ❌                | ✅                           |

> Cloud providers offer tools.
> AARI acts as the decision layer.

---

## 🧪 Example Output

```json
{
  "prior_risk": 0.62,
  "posterior_risk": 0.81,
  "strategy": "Rollback",
  "impacted_services": ["orders", "payment", "billing"],
  "anomaly_detected": true,
  "explanation": "IAM misconfiguration likely causing cross-service access failure..."
}
```

---

## 🏗️ Tech Stack

### Backend

* Python
* FastAPI
* Multi-agent architecture
* Probabilistic risk modeling

### Frontend

* React (Vite)
* Axios
* Data visualization (charts)

### AI Layer

* Gemini API (LLM-based reasoning)

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/rishit411/AutonomousRollbackIntelligence-aari.git
cd AutonomousRollbackIntelligence-aari
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env`:

```
GEMINI_API_KEY=your_api_key_here
```

Run:

```bash
uvicorn app.main:app --reload
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open:

```
http://localhost:5173
```

---

## 🧠 Key Learnings

* Modeling real-world systems requires probabilistic thinking, not rule-based logic
* Observability alone is not enough — systems need **predictive intelligence**
* Multi-agent architectures help break complex decisions into composable steps
* Explainability is critical for trust in AI-driven systems

---

## 🔮 Future Improvements

* Integration with real telemetry (Azure Monitor / CloudWatch)
* Continuous learning from deployment outcomes
* More accurate simulation models
* CI/CD pipeline integration
* Confidence scoring for decision-making

---

## 📌 Use Cases

* High-risk deployments (IAM, networking)
* Financial systems (payments, billing)
* Microservice-heavy architectures
* Multi-region rollouts
* Regulated environments

---

## 🤝 Contributing

Open to ideas, improvements, and collaborations.

---

## ⭐ If you found this interesting

Give it a star ⭐ and let’s build smarter deployment systems.

---

## 👨‍💻 Author

**Rishit Bansal**

---
