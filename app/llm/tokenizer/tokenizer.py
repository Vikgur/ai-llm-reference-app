import json
from typing import List

class Tokenizer:
    def __init__(self, vocab_path: str):
        with open(vocab_path, "r") as f:
            self.vocab = json.load(f)
        self.inv_vocab = {v: k for k, v in self.vocab.items()}
        self.unk_id = self.vocab.get("<unk>")
        self.bos_id = self.vocab.get("<bos>")
        self.eos_id = self.vocab.get("<eos>")

    def encode(self, text: str, add_special_tokens: bool = True) -> List[int]:
        tokens = text.strip().split()
        ids = [self.vocab.get(t, self.unk_id) for t in tokens]
        if add_special_tokens:
            ids = [self.bos_id] + ids + [self.eos_id]
        return ids

    def decode(self, ids: List[int], skip_special_tokens: bool = True) -> str:
        tokens = []
        for i in ids:
            tok = self.inv_vocab.get(i, "<unk>")
            if skip_special_tokens and tok.startswith("<") and tok.endswith(">"):
                continue
            tokens.append(tok)
        return " ".join(tokens)

    def vocab_size(self) -> int:
        return len(self.vocab)
