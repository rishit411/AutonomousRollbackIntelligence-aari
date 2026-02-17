class StrategyAgent:

    def recommend(self, posterior):

        if posterior < 0.3:
            return {
                "strategy": "Full Deployment",
                "traffic_split": "100%"
            }

        elif posterior < 0.6:
            return {
                "strategy": "Canary Deployment",
                "traffic_split": "10% initial"
            }

        elif posterior < 0.8:
            return {
                "strategy": "Phased Regional Rollout",
                "traffic_split": "Region by region"
            }

        else:
            return {
                "strategy": "Block Deployment",
                "traffic_split": "Manual approval required"
            }
