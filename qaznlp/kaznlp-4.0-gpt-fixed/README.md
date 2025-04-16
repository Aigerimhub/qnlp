
<p align="center">
  <img src="https://img.shields.io/pypi/v/kaznlp?color=blue" alt="PyPI">
  <img src="https://img.shields.io/github/license/yourusername/kaznlp" alt="License">
  <img src="https://img.shields.io/badge/made%20for-Kazakh-blue" alt="Kazakh NLP">
</p>

<h1 align="center">🇰🇿 KazNLP</h1>

<p align="center">
  <b>Kazakh Natural Language Processing Toolkit</b><br>
  Morphological analysis, wordform generation, POS tagging, corpus annotation and more.
</p>

---

# KazNLP

KazNLP — это набор инструментов для автоматической обработки казахского языка.  
Включает морфологический анализ, генерацию словоформ, POS-теггинг, визуализацию зависимостей, экспорт в CoNLL-U и HTML-интерфейс аннотации.

## 🚀 Возможности

- 🔤 Морфологический анализ: `root + suffix + ending`
- 🧠 POS-теггинг: модель `KazBERT + BiLSTM + CRF`
- 🧬 Генерация словоформ: `generate_form`, `generate_verb_form`
- 📊 Автоаннотация и экспорт: `JSONL`, `TSV`, `CoNLL-U`
- 🌐 HTML-интерфейс для редактирования разметки
- 📦 Поддержка Flask и Stanza

## 📦 Установка

```bash
pip install kaznlp-3.2.0-py3-none-any.whl
```

или:

```bash
git clone https://github.com/yourusername/kaznlp.git
cd kaznlp
pip install .
```

## 🧪 Тесты

```bash
pytest unit_tests.py
```

## 🖥️ Примеры

```python
from kaznlp import generate_form, generate_verb_form, MorphAnalyzer

print(generate_form("кітап", number="plural", case="genitive"))  # кітаптардың
print(generate_verb_form("бар", tense="past", person="1sg"))     # бардым

analyzer = MorphAnalyzer()
print(analyzer.analyze("кітаптарымның"))
```

## 📁 Лицензия

MIT License