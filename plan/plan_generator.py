import json
import re
from core.llm_client import LLMClient
from utils.text_cleaner import clean_text


class PlanGenerator:

    def __init__(self):
        self.llm = LLMClient()

    def generate(self, company: str, data: dict) -> dict:
        """
        Generates a detailed 8-section account plan using reliable regex parsing.
        Includes fallbacks for missing text.
        """

        yahoo = json.dumps(data.get("yahoo"), indent=2)
        news = json.dumps(data.get("news"), indent=2)
        wiki = data.get("wiki")

        prompt = f"""
Generate a detailed, professional Account Plan for the company: {company}.

Use ONLY the verified data provided below.
If some data is missing, say: "Insufficient public data available."

Yahoo Finance Data:
{yahoo}

News Articles:
{news}

Wikipedia Info:
{wiki}

Write EXACTLY the following sections (use these exact headings):

Company Overview
Products and Services
Market Position
Competitors
Recent News
Opportunities
Risks
Final Summary

Each section MUST contain 3–6 meaningful sentences.
Do NOT return JSON.
Do NOT number the sections.
Return clean plain text.
"""

        #  1️ RUN MODEL
        text = self.llm.run(prompt)

        if not text:
            raise ValueError("LLM returned an empty response.")

        #  2️ REGEX HEADINGS 

        patterns = {
            "Company_Overview": r"(Company Overview[:\-]?)",
            "Products_and_Services": r"(Products and Services[:\-]?)",
            "Market_Position": r"(Market Position[:\-]?)",
            "Competitors": r"(Competitors[:\-]?)",
            "Recent_News": r"(Recent News[:\-]?)",
            "Opportunities": r"(Opportunities[:\-]?)",
            "Risks": r"(Risks[:\-]?)",
            "Final_Summary": r"(Final Summary[:\-]?)"
        }

        extracted = {k: "" for k in patterns}

        # A huge combined pattern to split the LLM text safely.
        master_pattern = "|".join(patterns.values())

        parts = re.split(master_pattern, text, flags=re.IGNORECASE)

        current_key = None

        #3️ ASSIGN TEXT TO SECTIONS -
        for raw in parts:
            if not raw or raw.strip() == "":
                continue

            chunk = raw.strip()
            matched = False

            # Detect heading
            for key, pat in patterns.items():
                if re.fullmatch(pat, chunk, flags=re.IGNORECASE):
                    current_key = key
                    matched = True
                    break

            # If actual content chunk
            if not matched and current_key:
                extracted[current_key] += clean_text(chunk) + "\n\n"

        #  4️ FINAL CLEANUP
        for k, v in extracted.items():
            extracted[k] = clean_text(v.strip() or "Insufficient public data available.")

        return extracted
