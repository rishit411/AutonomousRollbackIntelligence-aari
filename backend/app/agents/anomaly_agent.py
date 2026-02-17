import numpy as np

class AnomalyAgent:

    def detect(self, service):

        cpu_z = (np.mean(service.cpu) - 0.55) / 0.05
        latency_z = (np.mean(service.latency) - 120) / 15
        error_z = (np.mean(service.error_rate) - 0.01) / 0.004

        anomaly = (
            abs(cpu_z) > 2 or
            abs(latency_z) > 2 or
            abs(error_z) > 2
        )

        return bool(anomaly)
