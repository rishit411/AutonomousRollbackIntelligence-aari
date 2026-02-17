from google import genai
from app.config import GEMINI_API_KEY

class ExplanationAgent:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def explain(self, change_type, posterior, impacted, anomaly):

        prompt = f"""
        Azure Deployment Simulation Analysis:

        Change Type: {change_type}
        Failure Probability: {posterior}
        Impacted Services: {impacted}
        Anomaly Detected: {anomaly}

        Provide:
        1. Technical root cause hypothesis
        2. Dependency cascade explanation
        3. Recommended mitigation strategy
        4. Rollback advisability assessment

        Use structured enterprise-grade language.
        """

        response = self.client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt,
        )

        return response.text
