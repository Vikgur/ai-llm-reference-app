# Оглавление

- [Безопасность LLM](#безопасность-llm)
- [Контекст безопасности](#контекст-безопасности)
- [Модель угроз LLM](#модель-угроз-llm)
- [Mapping угроз на LLM pipeline](#mapping-угроз-на-llm-pipeline)
- [Prompt Injection](#prompt-injection)
  - [Описание](#описание)
  - [Контрмеры](#контрмеры)
- [Data Exfiltration](#data-exfiltration)
  - [Описание](#описание-1)
  - [Контрмеры](#контрмеры-1)
- [Policy Bypass](#policy-bypass)
  - [Описание](#описание-2)
  - [Контрмеры](#контрмеры-2)
- [Denial of Service](#denial-of-service)
  - [Описание](#описание-3)
  - [Контрмеры](#контрмеры-3)
- [Model Tampering](#model-tampering)
  - [Описание](#описание-4)
  - [Контрмеры](#контрмеры-4)
- [Input Controls](#input-controls)
- [Inference Controls](#inference-controls)
- [Output Controls](#output-controls)
- [Runtime Isolation Assumptions](#runtime-isolation-assumptions)
- [Связь с формальной моделью угроз](#связь-с-формальной-моделью-угроз)
- [Итог](#итог)

---

# Безопасность LLM

Этот документ описывает **security-модель LLM**, реализованную в `ai-llm-reference-app`.

Цель:  
– зафиксировать угрозы, характерные именно для LLM  
– показать, где и как они контролируются  
– связать модель, код и политики  

Документ фокусируется на **inference**, а не на обучении.

---

# Контекст безопасности

LLM в sovereign-среде рассматривается как:  
– потенциальный источник утечек  
– сложный для интерпретации компонент  
– объект повышенного интереса атакующих  

Безопасность строится вокруг предположения:  
**модель не является доверенной сама по себе**.

Архитектурный контекст:  
[`architecture.md`](architecture.md)

---

# Модель угроз LLM

Ключевые классы угроз:

– Prompt Injection  
– Data Exfiltration  
– Policy Bypass  
– Denial of Service  
– Model Tampering  

Каждая угроза рассматривается **в привязке к этапам inference**.

---

# Mapping угроз на LLM pipeline

| Этап | Потенциальные угрозы |
|-----|----------------------|
| Prompt / Input | Injection, DoS |
| Tokenization | Boundary bypass |
| Embeddings | Side-channel |
| Transformer | Resource exhaustion |
| Sampling | Non-deterministic leakage |
| Decoding | Policy bypass |
| Post-processing | Output leakage |

Pipeline подробно описан в:  
[`llm-internals.md`](llm-internals.md)

---

# Prompt Injection

## Описание

Попытка:  
– изменить поведение модели  
– обойти ограничения  
– заставить модель выдать запрещённый контент  

## Контрмеры

– строгая валидация входа  
– ограничения длины  
– deny-by-default политики  
– отсутствие системных промптов  

---

# Data Exfiltration

## Описание

Риск:  
– утечки данных через output  
– восстановления информации о модели  
– side-channel через генерацию  

## Контрмеры

– output filtering  
– redaction  
– ограничение длины ответа  
– отсутствие доступа к внешним данным  

---

# Policy Bypass

## Описание

Попытка:  
– обойти security-фильтры  
– изменить логику enforcement  
– использовать нестандартные токены  

## Контрмеры

– централизованные политики  
– формализованные правила  
– проверка на нескольких этапах  

Политики реализованы в:  
`ci/policies/*.rego`

---

# Denial of Service

## Описание

Возможные атаки:  
– длинные prompt’ы  
– ресурсоёмкие последовательности  
– повторяющиеся запросы  

## Контрмеры

– лимиты длины  
– caps на ресурсы  
– тайм-ауты  
– Kubernetes quotas  

---

# Model Tampering

## Описание

Попытка:  
– изменить веса  
– подменить артефакт  
– загрузить неподписанную модель  

## Контрмеры

– immutable модель  
– checksum verification  
– read-only filesystem  
– supply chain validation  

Связь с CI/CD:  
[`supply-chain.md`](supply-chain.md)

---

# Input Controls

Контроль входных данных включает:

– форматную валидацию  
– ограничения длины  
– допустимые символы  
– отказ по умолчанию  

Input рассматривается как **полностью недоверенный**.

---

# Inference Controls

Контроль процесса inference:

– детерминированные операции  
– ограниченное sampling  
– фиксированные размеры  
– предсказуемое потребление ресурсов  

Inference должен быть:  
**объяснимым и воспроизводимым**.

---

# Output Controls

Output проходит через:

– фильтры  
– redaction  
– policy evaluation  
– финальную валидацию  

Output — последняя линия защиты.

---

# Runtime Isolation Assumptions

Безопасность предполагает:

– изолированный Kubernetes namespace  
– non-privileged pod  
– seccomp / AppArmor  
– отсутствие внешних вызовов  
– read-only filesystem  

Runtime описан в:  
[`architecture.md`](architecture.md)

---

# Связь с формальной моделью угроз

Этот документ дополняет, но не заменяет:

– `security/threat-model/threat-model.md`  

Здесь описана **прикладная реализация угроз**, а не формальная методология.

---

# Итог

Безопасность LLM в этом проекте:  
– threat-driven  
– policy-enforced  
– pipeline-aware  

Она построена для environments, где:
**LLM обязан быть контролируемым, а не “умным”**.
