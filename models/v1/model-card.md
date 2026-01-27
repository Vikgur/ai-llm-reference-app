# Model Card — v1

## Model name
ai-llm-reference-app / v1

## Intended use
- Reference LLM for secure inference pipelines
- Demonstration of DevSecOps, supply-chain and runtime controls
- Not for production NLP workloads

## Architecture
- Word-level tokenizer
- Static embeddings
- Decoder-only transformer (minimal)
- Greedy decoding

## Training data
- Not trained
- Weights are placeholders

## Limitations
- No semantic understanding
- Deterministic output
- Extremely small vocabulary

## Risks
- Prompt echoing
- Hallucination by construction
- Not suitable for sensitive data

## Security notes
- Weights treated as immutable artifact
- Integrity enforced via SHA-256
- Loaded read-only at runtime
