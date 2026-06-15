# Dataset Card: Legal Evidence Selection Corpus

## Dataset Summary

This dataset supports clause-level legal and policy evidence retrieval, compact evidence-set construction, and downstream decision support. It contains policy and regulatory documents, clause-level segments, natural-language queries or case descriptions, linked evidence clauses, and one of three labels: `Eligible`, `Not Eligible`, or `Needs Review`.

## Motivation

Existing legal benchmarks such as LexGLUE and PROVBENCH primarily address legal language understanding, classification, or provision retrieval. They do not directly represent multi-clause evidence assembly for policy-oriented eligibility and compliance decisions. This dedicated corpus was therefore constructed to evaluate both semantic retrieval and controlled-cardinality evidence selection.

## Sources

Documents were collected from publicly accessible official institutional or administrative sources.

**TODO:** List the exact institutions, portals, jurisdictions, and document categories used.

A complete source list must be provided in `source_manifest.csv`.

## Dataset Size

Use only verified counts.

- Documents: `REPLACE_ME`
- Clause-level segments: `REPLACE_ME`
- Queries or case descriptions: `REPLACE_ME`
- Query-evidence links: `REPLACE_ME`

## Annotation Procedure

**TODO:** State who created the queries, who assigned evidence links and labels, how disagreements were resolved, and whether annotators had legal or policy expertise.

## Splits

- Training: `REPLACE_ME`
- Validation: `REPLACE_ME`
- Test: `REPLACE_ME`

## Intended Uses

- Semantic legal retrieval
- Policy information extraction
- Evidence subset selection
- Eligibility assessment
- Compliance-oriented decision support
- Explainable Legal NLP

## Limitations

Potential limitations include domain specificity, source-document coverage, annotation subjectivity, class imbalance, policy changes over time, and jurisdictional transfer limitations.

## Licensing and Redistribution

The original documents remain subject to the reuse conditions of their official sources. Do not redistribute full document texts unless permitted. Where redistribution is restricted, provide source URLs, identifiers, metadata, and reconstruction scripts instead.

**TODO:** Add the documentation/annotation license and any source-specific reuse restrictions.

## Ethical Considerations

The dataset must not contain personal or confidential information. Queries and examples should be anonymized. The system is intended for decision support and research, not autonomous legal decision-making.

## Version

- Version: `1.0.0`
- Release date: `REPLACE_ME`
