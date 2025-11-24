import os
import requests
import json

class LLMClient:
    """
    Uses Gemini 2.0 Flash REST API safely with fallback parsing.
    """

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing")

        self.url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"gemini-2.0-flash:generateContent?key={self.api_key}"
        )

    def run(self, prompt: str) -> str:
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(self.url, json=payload)

        if response.status_code != 200:
            raise RuntimeError(f"Gemini API Error: {response.text}")

        data = response.json()

        
        # SAFE EXTRACTION (ALL CASES)
    

        try:
            # Standard Gemini format
            return data["candidates"][0]["content"]["parts"][0]["text"]

        except KeyError:
            pass

        try:
            # Fallback format
            return data["candidates"][0]["message"]["content"][0]["text"]

        except Exception:
            pass

        raise RuntimeError(f"Gemini response format unknown: {data}")

    def fallback_company_search(self, company: str):
        prompt = f"""
The user is researching the company: {company}.
If this is NOT a valid company return ONLY: INVALID_COMPANY.
Otherwise provide a short factual description.
"""

        result = self.run(prompt).strip()

        if "INVALID_COMPANY" in result.upper():
            return None

        return {"summary": result}
