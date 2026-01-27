import hashlib
from pathlib import Path

MODEL_VERSION = "v1"

def model_provenance(weights_path: str) -> dict:
    data = Path(weights_path).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    return {
        "model": MODEL_VERSION,
        "sha256": digest,
    }
