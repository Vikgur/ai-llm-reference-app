# Оглавление

- [Архитектура системы](#архитектура-системы)
- [Архитектурный контекст](#архитектурный-контекст)
- [Логическая архитектура](#логическая-архитектура)
- [Компоненты системы](#компоненты-системы)
  - [API слой](#api-слой)
  - [LLM Inference Pipeline](#llm-inference-pipeline)
  - [Policy Enforcement](#policy-enforcement)
  - [Model Artifacts](#model-artifacts)
  - [Observability](#observability)
- [Поток данных (Data Flow)](#поток-данных-data-flow)
- [Trust Boundaries](#trust-boundaries)
  - [Ненадёжная зона (Untrusted)](#ненадёжная-зона-untrusted)
  - [Ограниченно доверенная зона](#ограниченно-доверенная-зона)
  - [Доверенная зона](#доверенная-зона)
- [Runtime архитектура](#runtime-архитектура)
- [Kubernetes-топология](#kubernetes-топология)
- [Точки Security Enforcement](#точки-security-enforcement)
- [Связанные документы](#связанные-документы)
- [Итог](#итог)

---

# Архитектура системы

Этот документ описывает **логическую и runtime-архитектуру** `ai-llm-reference-app`.

Цель — зафиксировать:  
– из каких компонентов состоит система  
– как проходит inference-поток данных  
– где проходят границы доверия  
– где и как применяется security enforcement  

Документ описывает **что и где**, а не детали реализации.

---

# Архитектурный контекст

`ai-llm-reference-app` — это **inference-приложение**, работающее как часть платформы Sovereign AI.

Система:  
– не обучает модель  
– не управляет инфраструктурой  
– не решает governance  

Она:  
– принимает запрос  
– выполняет контролируемый inference  
– возвращает проверенный результат  

---

# Логическая архитектура

Система разделена на явные логические компоненты:

– API слой  
– LLM inference pipeline  
– Policy enforcement  
– Model artifacts  
– Observability  

Каждый компонент имеет:  
– чёткую зону ответственности  
– ограниченные зависимости  
– определённые trust boundaries  

---

# Компоненты системы

## API слой

Назначение:  
– приём запросов  
– базовая валидация  
– контроль формата  

API **не содержит логики модели** и не имеет доступа к весам напрямую.

---

## LLM Inference Pipeline

Inference реализован как **последовательный pipeline**:

1. Tokenization  
2. Embeddings  
3. Transformer decoder  
4. Logits и sampling  
5. Decoding  
6. Post-processing  

Каждый этап:  
– детерминирован  
– изолирован логически  
– подлежит контролю  

Детали этапов см.:  
[`llm-internals.md`](llm-internals.md)

---

## Policy Enforcement

Security-политики применяются:  
– на входе  
– между этапами inference  
– на выходе  

Политики:  
– формализованы  
– проверяемы  
– не зависят от UX  

Связь с моделью угроз:  
[`llm-security.md`](llm-security.md)

---

## Model Artifacts

Модель рассматривается как:  
– immutable артефакт  
– версионируемый объект  
– объект контроля целостности  

Весам запрещены:  
– модификации в runtime  
– динамическая подгрузка  
– side effects  

---

## Observability

Система публикует:  
– метрики inference  
– security-события  
– сигналы нарушения политик  

Наблюдаемость используется:  
– для контроля  
– для аудита  
– для доказательства корректности  

---

# Поток данных (Data Flow)

Полный поток данных выглядит следующим образом:

Client  
↓  
API  
↓  
Tokenization  
↓  
Embeddings  
↓  
Transformer  
↓  
Sampling / Decoding  
↓  
Post-processing  
↓  
Response


Данные **не пересекают границы компонентов произвольно**.  
Каждый переход — контролируемая точка.

---

# Trust Boundaries

Система разделяет зоны доверия:

## Ненадёжная зона (Untrusted)

– внешний пользователь  
– входной prompt  
– сетевое окружение  

## Ограниченно доверенная зона

– API слой  
– preprocessing  

## Доверенная зона

– inference engine  
– model artifacts  
– runtime policies  

Переходы между зонами всегда:  
– валидируются  
– логируются  
– контролируются  

---

# Runtime архитектура

В runtime система развёртывается как:

– контейнеризованное приложение  
– изолированный pod  
– read-only filesystem  
– ограниченные ресурсы  

Взаимодействие с внешним миром:  
– только через API  
– без прямого доступа к storage  
– без внешних вызовов  

---

# Kubernetes-топология

В Kubernetes используются:

– отдельный namespace  
– resource quotas  
– Pod Security Standards  
– seccomp / AppArmor  
– NetworkPolicies  

Приложение не имеет:  
– cluster-wide прав  
– privileged контейнеров  
– динамических volume mounts  

---

# Точки Security Enforcement

Security enforcement происходит:

– на уровне API  
– внутри inference pipeline  
– на уровне артефактов  
– на уровне runtime  
– на уровне CI/CD  

Архитектура предполагает, что **безопасность нельзя “добавить позже”**.

---

# Связанные документы

– Детали LLM pipeline: [`llm-internals.md`](llm-internals.md)  
– Модель угроз и security: [`llm-security.md`](llm-security.md)  
– Supply chain и артефакты: [`supply-chain.md`](supply-chain.md)  

---

# Итог

Архитектура `ai-llm-reference-app`:  
– минимальна  
– формальна  
– контролируема  

Она предназначена для environments, где:
**каждый байт и каждый переход должны быть объяснимы и проверяемы**.
