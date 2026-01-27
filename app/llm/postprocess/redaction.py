import re

REDACTION_PATTERNS = [
    re.compile(r"\b\d{16}\b"),        # credit card–like
    re.compile(r"\b[A-Za-z0-9]{32,}\b"),  # tokens / hashes
]

def redact(text: str) -> str:
    out = text
    for pattern in REDACTION_PATTERNS:
        out = pattern.sub("[REDACTED]", out)
    return out
