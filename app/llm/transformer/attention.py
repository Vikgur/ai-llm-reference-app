from typing import List
import math

def scaled_dot_product_attention(q, k, v):
    scores = []
    for qi in q:
        row = []
        for kj in k:
            dot = sum(a * b for a, b in zip(qi, kj))
            row.append(dot / math.sqrt(len(qi)))
        scores.append(row)

    attn = []
    for row in scores:
        s = sum(row)
        attn.append([x / s for x in row])

    output = []
    for i, row in enumerate(attn):
        out = [0.0] * len(v[0])
        for j, w in enumerate(row):
            for d in range(len(out)):
                out[d] += w * v[j][d]
        output.append(out)

    return output
