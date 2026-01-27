class DecodingGuards:
    def __init__(self, max_tokens: int, max_context: int):
        self.max_tokens = max_tokens
        self.max_context = max_context

    def check_context(self, token_ids):
        if len(token_ids) > self.max_context:
            raise ValueError("Context length exceeded")

    def check_generation(self, generated_ids):
        if len(generated_ids) > self.max_tokens:
            raise ValueError("Max generation tokens exceeded")
