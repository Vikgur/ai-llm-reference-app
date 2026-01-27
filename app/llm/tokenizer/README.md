# Tokenizer

Минимальный word-level tokenizer для reference LLM.

## Границы ответственности
- Только детерминированное преобразование text ↔ token ids
- Нет обучения, нет мутаций vocab в runtime
- Vocab считается immutable артефактом

## Security considerations
- Ограничение входной длины enforced на уровне API / guards
- Отсутствие regex / eval — защита от ReDoS
- Unknown tokens маппятся в `<unk>`, без исключений

## Limitations
- Word-level, без BPE / SentencePiece
- Предназначен для демонстрации trust boundary, не для SOTA моделей
