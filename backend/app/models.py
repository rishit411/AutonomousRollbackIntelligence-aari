from pydantic import BaseModel
from typing import List

class DeploymentRequest(BaseModel):
    service_name: str
    change_type: str
    impact_scope: str

class DeploymentResponse(BaseModel):
    prior_risk: float
    posterior_risk: float
    impacted_services: List[str]
    strategy: str
    anomaly_detected: bool
    explanation: str
