from utils.text_cleaner import clean_text
from core.llm_client import LLMClient

class PlanUpdater:
    """
    Updates and rewrites specific sections of the account plan using LLM.
    """

    VALID_SECTIONS = {
        "Company_Overview",
        "Products_and_Services",
        "Market_Position",
        "Competitors",
        "Recent_News",
        "Opportunities",
        "Risks",
        "Final_Summary"
    }

    def __init__(self):
        self.llm = LLMClient()

    def update_section(self, plan: dict, section: str, user_request: str):
        """
        Rewrites a section using LLM based on user instructions.
        If the section doesn't exist yet, it will be created.
        """

        if section not in self.VALID_SECTIONS:
            raise ValueError(f"Invalid section '{section}'. Allowed: {self.VALID_SECTIONS}")

        old_text = plan.get(section, "")

        # LLM prompt
        prompt = f"""
Rewrite the following section of an Account Plan.

Section: {section}

Current Text:
{old_text}

User Request:
{user_request}

Rewrite the section in a clean, structured, professional way.
Do NOT add new sections, just rewrite this one section.
"""

        new_text = self.llm.run(prompt)
        new_text = clean_text(new_text)

        updated_plan = plan.copy()
        updated_plan[section] = new_text

        return updated_plan
