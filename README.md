# Legal Evidence Dataset Documentation Package

This folder is a publication-ready **template** for documenting the dataset used in the article:

**MPNet-Based Semantic Retrieval for Legal Evidence Selection: A Set Cover and Subset Selection Perspective**

## Important

Before uploading this folder publicly:

1. Replace every `REPLACE_ME` and `TODO`.
2. Replace the synthetic examples in `sample_data.jsonl` with real anonymized representative records.
3. Enter verified corpus counts in `corpus_statistics.csv` and `split_statistics.csv`.
4. Add only real source URLs to `source_manifest.csv`.
5. Confirm that document reuse and redistribution conditions permit publication.
6. Run `python validate_release.py`.

## Included files

- `DATASET_CARD.md` — dataset scope, motivation, provenance, annotation, limitations, and licensing.
- `source_manifest.csv` — source-document metadata.
- `corpus_statistics.csv` — verified corpus-level counts.
- `split_statistics.csv` — train, validation, and test split statistics.
- `sample_data.jsonl` — representative records; current entries are synthetic placeholders.
- `annotation_guidelines.md` — label definitions and evidence annotation procedure.
- `schema.json` — machine-readable record schema.
- `CITATION.cff` — repository citation metadata.
- `REVIEWER_RESPONSE.md` — draft response to Reviewer C.
- `MANUSCRIPT_TEXT.md` — replacement text for the manuscript.
- `validate_release.py` — checks unresolved placeholders.

## Public resources

- Model and code artifacts: https://huggingface.co/irinaqqq/lexir
- Supporting software repository: https://github.com/Aigerimhub/qnlp
