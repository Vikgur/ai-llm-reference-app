# Threat Model — ai-llm-reference-app

## Assets
- Model weights
- Inference API
- User prompts
- Generated outputs

## Trust boundaries
- External client → API
- API → LLM core
- LLM core → runtime / kernel

## Threats
- Prompt injection
- Denial of service (token explosion)
- Model tampering
- Data exfiltration via output
- Container escape

## Mitigations
- Input limits and decoding guards
- Read-only root filesystem
- Non-root execution
- NetworkPolicy isolation
- Model checksum verification

## Out of scope
- Training-time poisoning
- Side-channel attacks
