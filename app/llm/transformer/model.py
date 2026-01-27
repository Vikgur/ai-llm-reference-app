from typing import List
from .decoder import DecoderBlock

class TransformerModel:
    def __init__(self, layers: int, hidden_dim: int):
        self.layers = [DecoderBlock(hidden_dim) for _ in range(layers)]

    def forward(self, x: List[List[float]]):
        for layer in self.layers:
            x = layer.forward(x)
        return x
