import random
from typing import List

def greedy(logits: List[float]) -> int:
    return int(max(range(len(logits)), key=lambda i: logits[i]))

def top_k(logits: List[float], k: int) -> int:
    if k <= 0 or k > len(logits):
        raise ValueError("Invalid k")
    indices = sorted(range(len(logits)), key=lambda i: logits[i], reverse=True)[:k]
    return random.choice(indices)
