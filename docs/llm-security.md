Назначение:
– security-модель именно для LLM

Тезисы:
– threat model (prompt injection, exfiltration, DoS, policy bypass)
– mapping угроз на этапы LLM pipeline
– input controls (prompt limits, validation)
– inference controls (determinism, resource caps)
– output controls (filters, redaction, policies)
– runtime isolation assumptions

Связи:
– опирается на llm-internals.md
– конкретизирует architecture.md
– связан с security/threat-model/threat-model.md
– связан с ci/policies/*.rego