---
language: kazakh
tags:
  - kazakh
  - ner
  - qaznlp
  - token-classification
license: mit
---

# QazNLP NER Model

This model identifies named entities in Kazakh language texts using KazBERT + BiLSTM + CRF architecture. It recognizes `PER`, `LOC`, `ORG`, and `MISC` tags.

## Training Data
The model was trained on custom annotated Kazakh corpora.

## Usage

```python
from qaznlp.models.ner_model import KazBERTNERModel

model = KazBERTNERModel()
result = model.predict("Астана қаласында өткен форумға Нұрсұлтан Назарбаев қатысты.")
print(result)
```

## Author
Aigerim · 2024