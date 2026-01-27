import hashlib
import struct
from typing import List

class Embedding:
    def __init__(self, weights_path: str, vocab_size: int, dim: int):
        self.vocab_size = vocab_size
        self.dim = dim
        self.weights_path = weights_path
        self._verify_weights()
        self.weights = self._load_weights()

    def _verify_weights(self):
        with open(self.weights_path, "rb") as f:
            data = f.read()
        if len(data) != self.vocab_size * self.dim * 4:
            raise ValueError("Invalid embedding weights size")

    def _load_weights(self):
        weights = []
        with open(self.weights_path, "rb") as f:
            for _ in range(self.vocab_size):
                row = struct.unpack(f"{self.dim}f", f.read(self.dim * 4))
                weights.append(row)
        return weights

    def forward(self, token_ids: List[int]):
        return [self.weights[t] for t in token_ids]
