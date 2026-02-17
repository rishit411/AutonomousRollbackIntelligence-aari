import numpy as np

class TelemetryAgent:

    def apply_change(self, service, change_type):

        # Deep copy BEFORE metrics
        before = {
            "cpu": service.cpu.copy(),
            "latency": service.latency.copy(),
            "error_rate": service.error_rate.copy()
        }

        # Apply drift
        if change_type == "iam":
            service.error_rate = service.error_rate * 2
            service.latency = service.latency * 1.4

        elif change_type == "network":
            service.latency = service.latency * 1.6

        elif change_type == "autoscale":
            service.cpu = service.cpu * 1.3

        # Clamp values safely using numpy
        service.cpu = np.clip(service.cpu, 0, 100)
        service.error_rate = np.clip(service.error_rate, 0, 1)

        after = {
            "cpu": service.cpu.copy(),
            "latency": service.latency.copy(),
            "error_rate": service.error_rate.copy()
        }

        return service, before, after
