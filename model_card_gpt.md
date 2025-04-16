---
language: kazakh
tags:
  - kazakh
  - text-generation
  - gpt
  - qaznlp
license: mit
---

# QazGPT Mini

This is a Kazakh GPT-2 style model for generating fluent Kazakh text. Trained on a cleaned corpus of Kazakh news, books, and web content.

## Usage

```python
from qaznlp.models.kazgpt_mini import KazGPT
model = KazGPT()
output = model.generate("Қазақ тілі —")
print(output)
```

## Author
Aigerim · 2024