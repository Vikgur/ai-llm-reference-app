from typing import List
from .sampler import greedy

def decode_step(logits: List[float]) -> int:
    return greedy(logits)

def decode_sequence(logits_seq: List[List[float]], max_tokens: int) -> List[int]:
    tokens = []
    for step_logits in logits_seq:
        if len(tokens) >= max_tokens:
            break
        token = decode_step(step_logits)
        tokens.append(token)
    return tokens
