import numpy as np

class RiskAgent:

    def compute_prior(self, service, change_type, impact_scope):
        risk = 0.0

        # IAM risk
        if change_type == "iam":
            risk += service.iam_complexity * 0.5

        # Network exposure risk
        if change_type == "network":
            risk += service.network_surface * 0.4

        # Autoscale sensitivity
        if change_type == "autoscale":
            if np.mean(service.cpu) > service.autoscale_limit - 0.1:
                risk += 0.5

        # Cross-service blast amplification
        if impact_scope == "cross":
            risk += 0.3

        return min(risk, 0.95)

    def compute_posterior(self, prior, anomaly_detected):
        posterior = prior

        if anomaly_detected:
            posterior += 0.25

        return min(posterior, 0.99)
