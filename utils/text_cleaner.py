import re

class TextCleaner:
    """
    Advanced text cleaning utility:
    - Removes excessive whitespace
    - Normalizes newlines
    - Truncates long LLM outputs
    - Safely merges text blocks
    """

    def clean(self, text: str) -> str:
        """Clean whitespace, newlines, markdown fences, etc."""
        if not text:
            return ""

        # Remove code fences like ```json or ```text
        text = re.sub(r"```[\s\S]*?```", "", text)

        # Normalize whitespace
        text = text.replace("\r", "").strip()
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"\s{2,}", " ", text)

        return text

    def truncate(self, text: str, limit: int = 3000) -> str:
        """Safely shorten long responses (Wikipedia, OpenAI, etc.)."""
        if not text:
            return ""
        return text[:limit]

    def safe_merge(self, *parts):
        """Combine multiple optional blocks into clean unified text."""
        blocks = [p.strip() for p in parts if p and isinstance(p, str)]
        return "\n\n".join(blocks)


#
# TOP-LEVEL FUNCTION (required by your ResearchEngine import)


_cleaner = TextCleaner()

def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.replace("\r", "")
    text = re.sub(r"`{3}.*?`{3}", "", text, flags=re.DOTALL)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()
