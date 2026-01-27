from typing import List

def feed_forward(x: List[List[float]], hidden_dim: int):
    out = []
    for vec in x:
        h = [v * 0.5 for v in vec[:hidden_dim]]
        out.append(h)
    return out
