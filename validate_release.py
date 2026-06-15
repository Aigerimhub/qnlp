from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
problems=[]
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.md','.csv','.json','.jsonl','.cff','.txt','.py'}:
        text=path.read_text(encoding='utf-8',errors='replace')
        if 'REPLACE_ME' in text: problems.append(f"{path.name}: contains REPLACE_ME")
        if 'TODO:' in text: problems.append(f"{path.name}: contains TODO")
sample=ROOT/'sample_data.jsonl'
if sample.exists():
    for i,line in enumerate(sample.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip(): continue
        try: rec=json.loads(line)
        except json.JSONDecodeError as e:
            problems.append(f"sample_data.jsonl line {i}: invalid JSON ({e})"); continue
        if rec.get('is_synthetic') is True:
            problems.append(f"sample_data.jsonl line {i}: synthetic example remains")
manifest=ROOT/'source_manifest.csv'
if manifest.exists() and len(manifest.read_text(encoding='utf-8').splitlines())<=1:
    problems.append('source_manifest.csv: no real source rows')
if problems:
    print('Release validation FAILED:
')
    [print('- '+p) for p in problems]
    sys.exit(1)
print('Release validation PASSED.')
