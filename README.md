# QNLP 4.0 – Full Kazakh NLP Suite

**QNLP 4.0** is a comprehensive and modular library for automatic processing of the Kazakh language. It combines modern transformer-based models (KazBERT, GPT), classic rule-based morphological processing, and production-ready deployment tools (API, CLI, ONNX).

---

## Features

- **KazBERT + BiLSTM + CRF**: High-accuracy POS and NER tagging
- **KazGPT**: Kazakh GPT-based text generation
- **QA Model**: SQuAD-style question answering
- **SRL**: Semantic role labeling using transformer models
- **Coreference Resolution**: Rule-based and model-enhanced
- **Morphology**: Lemmatizer, generator, morpheme analyzer
- **Tokenizer**: BPE, SentencePiece support
- **ONNX**: Export models for production
- **API**: Flask + Swagger + CLI support
- **Augmentation**: NER-specific synthetic data generator
- **Unit Testing**: All modules with test coverage

---

## Models

| Model           | Architecture             | Description                    |
|----------------|---------------------------|--------------------------------|
| `kazner-crf`    | KazBERT + BiLSTM + CRF   | Named Entity Recognition       |
| `kazpos-crf`    | KazBERT + BiLSTM + CRF   | Part-of-Speech Tagging         |
| `kazgpt-mini`   | GPT2 (fine-tuned)        | Kazakh Text Generation         |
| `kazqa`         | KazBERT + QA Head        | Question Answering             |
| `kazsrl`        | KazBERT + Classifier     | Semantic Role Labeling         |
| `kazcoref`      | Rule-based + Span Linking| Coreference Resolution         |

---

## Directory Structure

```
qaznlp/
├── models/
├── morphology/
├── tokenizer/
├── training/
├── augment/
├── server/
├── scripts/
├── data/
├── tests/
└── notebooks/
```

---

## Demo & Testing

- `test_all.py`: Run all tests
- `app.py`: REST API with Swagger UI
- `export_onnx.py`: Export all models to ONNX

---

## Installation

```bash
pip install qaznlp
```

## License

IITU © 2025 by Aigerim Aitim

---

> For academic use, cite as: *QNLP 4.0: An Open-Source Suite for Kazakh Language Processing (2025)*
