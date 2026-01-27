class OutputPolicy:
    def __init__(self, allow_empty: bool = False):
        self.allow_empty = allow_empty

    def enforce(self, text: str) -> str:
        if not text and not self.allow_empty:
            raise ValueError("Empty output blocked by policy")
        return text
