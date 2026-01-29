# Оглавление

- [AI LLM Reference App](#ai-llm-reference-app)
  - [Ключевая идея](#ключевая-идея)
- [Цель репозитория в платформе Sovereign AI](#цель-репозитория-в-платформе-sovereign-ai)
- [Scope и границы ответственности](#scope-и-границы-ответственности)
- [Почему именно LLM (и почему минимальный)](#почему-именно-llm-и-почему-минимальный)
- [Архитектурное место в экосистеме Sovereign AI](#архитектурное-место-в-экосистеме-sovereign-ai)
- [Что именно демонстрирует репозиторий](#что-именно-демонстрирует-репозиторий)
  - [LLM internals как контролируемый пайплайн](#llm-internals-как-контролируемый-пайплайн)
  - [Security-by-design для inference](#security-by-design-для-inference)
  - [DevSecOps и supply chain для моделей](#devsecops-и-supply-chain-для-моделей)
- [Архитектура высокого уровня](#архитектура-высокого-уровня)
- [Trust boundaries и модель угроз](#trust-boundaries-и-модель-угроз)
- [Модель безопасности LLM](#модель-безопасности-llm)
- [Supply chain и CI/CD интеграция](#supply-chain-и-cicd-интеграция)
- [Runtime и deployment модель](#runtime-и-deployment-модель)
- [Наблюдаемость и контроль](#наблюдаемость-и-контроль)
- [Состав репозитория](#состав-репозитория)
- [Как читать и изучать репозиторий](#как-читать-и-изучать-репозиторий)
- [Связанные репозитории платформы](#связанные-репозитории-платформы)
- [Не-цели и анти-паттерны](#не-цели-и-анти-паттерны)

---

# AI LLM Reference App

Эталонный **LLM reference-проект уровня Senior DevSecOps** для суверенных и регулируемых AI-платформ.

Данный репозиторий представляет собой **минимальную, но настоящую реализацию LLM**, созданную не для демонстрации «умного чатбота», а для показа **глубокого понимания внутреннего устройства современных LLM и способов их защиты в production-средах**.

Проект ориентирован на контекст **sovereign AI**, где:  
– модель является критическим активом  
– inference — контролируемым процессом  
– безопасность важнее UX  
– воспроизводимость важнее скорости  
– DevSecOps является архитектурным слоем, а не набором тулов  

В репозитории показан **полный LLM-пайплайн**:  
– токенизация и эмбеддинги  
– transformer-декодер  
– формирование logits и sampling  
– декодирование и пост-обработка  
– enforcement security-политик на каждом этапе  

LLM реализован **осознанно минимальным**, чтобы:  
– все внутренние механизмы были прозрачны  
– attack surfaces были явными  
– security-контроли были проверяемыми  
– модель можно было формально threat-model’ить  

Репозиторий является **reference-реализацией**, а не продуктом:  
– без обучения  
– без внешних API  
– без магии  
– без vendor lock-in  

## Ключевая идея

> Современный LLM — это не модель.  
> Это цепочка доверия от токена до ответа.

Этот проект показывает, как выглядит **продовый LLM-inference**, когда:  
– модель — immutable artifact  
– код — проверяемый  
– supply chain — аттестуемый  
– runtime — изолированный  
– output — под контролем  

Именно так выглядят LLM-системы, допустимые в **государственных, defense и sovereign AI-платформах**.

---

# Цель репозитория в платформе Sovereign AI

`ai-llm-reference-app` — это **эталонный прикладной слой** платформы Sovereign AI.

Назначение репозитория:  
– показать, как **LLM выглядит как критический инфраструктурный компонент**, а не как ML-эксперимент  
– связать воедино **model internals, security, supply chain и runtime**  
– дать проверяемую reference-реализацию для regulated и sovereign environments  

Репозиторий отвечает на вопрос:  

> Как должен выглядеть LLM-inference, если его можно запускать в государственном, defense или sovereign-контуре.

Он **не автономен**, а осознанно встроен в экосистему:  
– `ai-secure-ci-cd-platform` — формирование доверенной цепочки поставки  
– `ai-kubernetes-security-platform` — изоляция и enforcement в runtime  
– `ai-governance-security` — политики, контроль и соответствие требованиям  

---

# Scope и границы ответственности

**В scope проекта:**  
– inference-only LLM  
– полный pipeline от токенов до ответа  
– security enforcement на каждом этапе  
– supply chain для кода и модели  
– Kubernetes-first runtime  
– observability и контроль поведения  

**За пределами scope:**  
– обучение и fine-tuning  
– distributed training  
– RLHF  
– performance-оптимизации  
– product UX  
– внешние SaaS/API  

Проект демонстрирует **архитектуру и контроль**, а не масштаб.

---

# Почему именно LLM (и почему минимальный)

LLM — один из самых сложных и уязвимых типов workload’ов:  
– непрозрачная логика  
– высокий риск data leakage  
– сложные attack surfaces  
– слабая типизация входа и выхода  

Минимальная реализация выбрана намеренно:  
– все этапы inference явны  
– нет скрытых оптимизаций  
– проще threat-model’ить  
– проще формально проверять  

Цель — **понять и защитить**, а не впечатлить качеством генерации.

Подробно: [`docs/llm-internals.md`](docs/llm-internals.md)

---

# Архитектурное место в экосистеме Sovereign AI

Репозиторий занимает уровень **application / inference workload**.

Он:  
– потребляет артефакты из CI/CD платформы  
– запускается в защищённом Kubernetes-контуре  
– подчиняется governance-политикам  
– публикует метрики и сигналы  

[ CI/CD & Supply Chain ]  
↓  
[ Immutable Model + Image ]  
↓  
[ Secure K8s Runtime ]  
↓  
[ LLM Inference App ]  
↓  
[ Controlled Output ]  

Детали: [`docs/architecture.md`](docs/architecture.md)

---

# Что именно демонстрирует репозиторий

## LLM internals как контролируемый пайплайн

Inference реализован как **детерминированная цепочка этапов**:  
– tokenization  
– embeddings  
– transformer decoder  
– logits → sampling  
– decoding  
– post-processing  

Каждый этап:  
– изолируем  
– логируем  
– ограничиваем  
– проверяем политиками  

## Security-by-design для inference

Безопасность встроена в дизайн:  
– явные trust boundaries  
– policy-based guards  
– input/output validation  
– runtime isolation  
– read-only model artifacts  

Threat-driven подход описан в:  
[`docs/llm-security.md`](docs/llm-security.md)

## DevSecOps и supply chain для моделей

Модель — это артефакт:  
– версионируемый  
– хешируемый  
– проверяемый  
– аттестуемый  

CI/CD обеспечивает:  
– SBOM  
– integrity checks  
– policy validation  
– provenance  

Подробно: [`docs/supply-chain.md`](docs/supply-chain.md)

---

# Архитектура высокого уровня

На высоком уровне система состоит из:  
– API слоя  
– LLM inference engine  
– policy enforcement  
– observability  
– secure runtime  

Детальная схема и разбор:  
[`docs/architecture.md`](docs/architecture.md)

---

# Trust boundaries и модель угроз

Ключевые границы доверия:  
– внешний пользователь  
– API  
– inference engine  
– модель как артефакт  
– Kubernetes runtime  

Угрозы рассматриваются как:  
– prompt injection  
– data exfiltration  
– model tampering  
– supply chain compromise  
– runtime escape  

Полная модель угроз:  
[`docs/llm-security.md`](docs/llm-security.md)

---

# Модель безопасности LLM

Принципы:  
– deny-by-default  
– explicit policies  
– immutable artifacts  
– minimal attack surface  
– observable behavior  

Безопасность реализуется:  
– в коде  
– в CI  
– в Kubernetes  
– в runtime профилях  

---

# Supply chain и CI/CD интеграция

Репозиторий интегрируется с secure CI/CD платформой:  
– сборка image  
– валидация модели  
– подпись артефактов  
– генерация SBOM  
– policy enforcement  

Это не pipeline, а **часть цепочки доверия**.

Подробно: [`docs/supply-chain.md`](docs/supply-chain.md)

---

# Runtime и deployment модель

Запуск ориентирован на Kubernetes:  
– namespace isolation  
– resource quotas  
– Pod Security Standards  
– seccomp / AppArmor  
– NetworkPolicies  

Deployment описан отдельно:  
[`docs/deployment.md`](docs/deployment.md)

---

# Наблюдаемость и контроль

Система предоставляет:  
– метрики inference  
– security events  
– policy violations  
– audit signals  

Цель — не только наблюдать, но **доказывать корректность поведения**.

---

# Состав репозитория

Репозиторий структурирован по ответственности:  
– app — код LLM  
– models — артефакты моделей  
– ci — политики и supply chain  
– security — threat model и runtime security  
– helm / k8s — deployment и изоляция  
– observability — контроль и аудит  

Навигация: [`docs/repository-structure.md`](docs/repository-structure.md)

---

# Как читать и изучать репозиторий

Рекомендуемый порядок:  
1. README  
2. `docs/architecture.md`  
3. `docs/llm-internals.md`  
4. `docs/llm-security.md`  
5. `docs/supply-chain.md`  
6. `docs/deployment.md`  

---

# Связанные репозитории платформы

– **ai-secure-ci-cd-platform** — secure pipelines и attestations  
– **ai-kubernetes-security-platform** — runtime security  
– **ai-governance-security** — политики и compliance  

---

# Не-цели и анти-паттерны

Здесь намеренно **не**:  
– «умный» чатбот  
– SaaS-продукт  
– ML playground  
– benchmark-гонка  
– vendor-specific решение  

Это **reference**, а не продукт.

Его задача — показать, **как должно быть устроено**, а не как быстро запустить.
