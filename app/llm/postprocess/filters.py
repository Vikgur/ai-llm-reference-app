from typing import List

BLOCKLIST = {
    "password",
    "secret",
    "token",
    "key",
}

def filter_tokens(tokens: List[str]) -> List[str]:
    out = []
    for t in tokens:
        if t.lower() in BLOCKLIST:
            out.append("[REDACTED]")
        else:
            out.append(t)
    return out
