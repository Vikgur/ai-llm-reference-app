Назначение:
– логическая и runtime-архитектура системы

Тезисы:
– logical architecture (components + boundaries)
– data flow: prompt → tokenization → embeddings → transformer → decoding → postprocess
– trust boundaries (trusted / untrusted)
– runtime topology (API, model, storage, k8s)
– точки security enforcement (high-level)

Связи:
– дополняет README.md
– ссылается на llm-internals.md для деталей реализации
– ссылается на llm-security.md для threat mapping