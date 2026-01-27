# Embeddings

Таблица embedding-векторов как immutable модельный артефакт.

## Design
- Хранение весов вне кода
- Жёсткая проверка размера при загрузке
- Только read-only доступ

## Security considerations
- Проверка целостности по размеру (дополняется checksum на уровне models/)
- Отказ от pickle / numpy.load
- Исключена динамическая инициализация

## Limitations
- Нет GPU / SIMD оптимизаций
- Предназначено для reference pipeline
