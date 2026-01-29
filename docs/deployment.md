# Оглавление

- [Deployment модель](#deployment-модель)
- [Контекст деплоя](#контекст-деплоя)
- [Container Assumptions](#container-assumptions)
- [Kubernetes Deployment Model](#kubernetes-deployment-model)
- [Namespace Isolation](#namespace-isolation)
- [Resource Isolation](#resource-isolation)
- [Security Controls в Kubernetes](#security-controls-в-kubernetes)
- [Network Model](#network-model)
- [Secrets и Configuration](#secrets-и-configuration)
- [Observability Hooks](#observability-hooks)
- [Runtime Controls](#runtime-controls)
- [Ограничения для Prod-like окружений](#ограничения-для-prod-like-окружений)
- [Связь с Helm и K8s манифестами](#связь-с-helm-и-k8s-манифестами)
- [Итог](#итог)

---

# Deployment модель

Этот документ описывает **безопасный путь от артефакта до runtime** для `ai-llm-reference-app`.

Цель:  
– зафиксировать assumptions окружения  
– описать модель деплоя  
– показать, где применяется runtime security  
– обозначить ограничения для prod-like сред  

Документ отвечает на вопрос:  
**как именно этот LLM должен быть запущен безопасно**.

---

# Контекст деплоя

Приложение разворачивается как часть платформы Sovereign AI.

Оно:  
– не управляет кластером  
– не изменяет инфраструктуру  
– не требует привилегий  

Архитектурный контекст:  
[`architecture.md`](architecture.md)

---

# Container Assumptions

Контейнер рассматривается как:

– immutable  
– минимальный  
– non-privileged  

Основные допущения:  
– один процесс  
– отсутствие shell-доступа  
– read-only filesystem  
– отсутствие package manager  

Контейнер не предназначен для интерактивной работы.

---

# Kubernetes Deployment Model

Приложение деплоится как:

– Deployment  
– один или несколько реплик  
– stateless workload  

Каждый pod:  
– изолирован  
– не хранит состояние  
– не делит volume с другими pod’ами  

---

# Namespace Isolation

Для приложения используется:

– отдельный namespace  
– собственные quotas  
– ограниченные права  

Namespace:  
– не имеет cluster-admin  
– не взаимодействует с другими workload’ами напрямую  

---

# Resource Isolation

Ограничения ресурсов обязательны:

– CPU limits  
– memory limits  
– ограничение числа pod’ов  

Цель:  
– защита от DoS  
– предсказуемость inference  
– контроль потребления  

---

# Security Controls в Kubernetes

Применяются следующие меры:

– Pod Security Standards  
– seccomp профили  
– AppArmor профили  
– NetworkPolicies  

Приложение:  
– не использует privileged режим  
– не имеет hostPath  
– не использует hostNetwork  

---

# Network Model

Сетевые допущения:

– вход только через Service  
– исходящий трафик ограничен  
– отсутствие внешних API вызовов  

NetworkPolicies используются как:  
– enforcement механизм  
– часть threat model  

---

# Secrets и Configuration

Secrets:  
– передаются через Kubernetes Secrets  
– не хранятся в образе  
– не логируются  

Configuration:  
– монтируется read-only  
– версионируется  
– проходит validation  

---

# Observability Hooks

Приложение предоставляет:

– metrics endpoint  
– structured logs  
– trace hooks  

Observability используется для:  
– контроля поведения  
– аудита  
– выявления аномалий  

Конфигурации:  
`observability/`

---

# Runtime Controls

Runtime контроль включает:

– ограничение syscalls  
– запрет записи на диск  
– контроль сетевого доступа  
– ограничение ресурсов  

Связь с security моделью:  
[`llm-security.md`](llm-security.md)

---

# Ограничения для Prod-like окружений

Окружения должны обеспечивать:

– защищённый registry  
– проверку подписей  
– enforcement trust policy  
– audit logging  

Без этих условий деплой считается **некорректным**.

---

# Связь с Helm и K8s манифестами

Реализация деплоя:  
– `helm/`  
– `k8s/`  

Этот документ:  
– не дублирует YAML  
– фиксирует архитектурные требования  

---

# Итог

Deployment модель `ai-llm-reference-app`:  
– минимальна  
– изолирована  
– контролируема  

Она предназначена для сред, где:  
**runtime — продолжение security-модели, а не отдельный слой**.
