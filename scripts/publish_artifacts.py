"""Promote checked candidates; visual review is an explicit, separate responsibility."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=json.loads((ROOT/'verification/candidate-checks.json').read_text())
assert not checks['issues'] and len(checks['editions'])==2
artifacts=[]
for result in checks['editions']:
    lang=result['language'];pdf=ROOT/f'build/{lang}/main.pdf'
    assert sha(pdf)==result['pdf_sha256'] and result['rendered_pages']==result['pages'],lang
    inputs=json.loads((ROOT/f'verification/build-{lang}.json').read_text())
    for name,h in inputs['inputs'].items():assert sha(ROOT/name)==h,name
    dest=ROOT/f'pdf/vibe-coding-in-practice-{lang}.pdf';shutil.copy2(pdf,dest)
    artifacts.append({'language':lang,'file':str(dest.relative_to(ROOT)),'sha256':sha(dest),'pages':result['pages']})
(ROOT/'verification/artifacts.json').write_text(json.dumps({'release':'v1.0.0','published_date':'2026-10-22','artifacts':artifacts,'sources':{str(p.relative_to(ROOT)):sha(p) for folder in ['src','scripts'] for p in sorted((ROOT/folder).rglob('*')) if p.is_file() and p.suffix in ['.tex','.py','.cjs']}},ensure_ascii=False,indent=2)+'\n')
print('Promoted both checked PDFs; remember to record the visual review.')
