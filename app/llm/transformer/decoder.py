from .attention import scaled_dot_product_attention
from .ffw import feed_forward

class DecoderBlock:
    def __init__(self, hidden_dim: int):
        self.hidden_dim = hidden_dim

    def forward(self, x):
        attn_out = scaled_dot_product_attention(x, x, x)
        ffw_out = feed_forward(attn_out, self.hidden_dim)
        return ffw_out
