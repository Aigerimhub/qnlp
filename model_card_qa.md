---
language: kazakh
tags:
  - kazakh
  - question-answering
  - qaznlp
license: mit
---

# QazNLP QA Model

A Kazakh language Question Answering model fine-tuned on a SQuAD-style QA dataset using KazBERT.

## Usage

```python
from qaznlp.models.qa_model import KazBERTQAModel
model = KazBERTQAModel()
answer = model.predict("Қазақстанның астанасы қай қала?", "Қазақстанның қазіргі астанасы – Астана қаласы.")
print(answer)
```

## Author
Aigerim · 2024