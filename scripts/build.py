"""Build one or both language editions from the repository root with XeLaTeX."""
from pathlib import Path
import argparse,hashlib,json,re,shutil,subprocess
ROOT=Path(__file__).resolve().parents[1]

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def build(lang):
    out=ROOT/'build'/lang;out.mkdir(parents=True,exist_ok=True)
    inputs=[*sorted((ROOT/'src'/lang).glob('*.tex')),*sorted((ROOT/'src/shared').glob('*.tex')),ROOT/'assets/cover.png',*sorted((ROOT/f'assets/diagrams/{lang}').glob('*.pdf'))]
    before={str(p.relative_to(ROOT)):digest(p) for p in inputs}
    for attempt in range(2):
        result=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(out),'src/'+lang+'/main.tex'],cwd=ROOT,capture_output=True,text=True)
        (out/f'pass-{attempt+1}.txt').write_text(result.stdout+result.stderr)
        if result.returncode:
            print('\n'.join(result.stdout.splitlines()[-50:]));raise SystemExit(result.returncode)
    assert before=={str(p.relative_to(ROOT)):digest(p) for p in inputs},'Inputs changed during compilation'
    log=(out/'main.log').read_text()
    warnings=[line for line in log.splitlines() if any(w in line for w in ['Overfull','Missing character','undefined','multiply defined'])]
    if warnings:raise SystemExit('\n'.join(warnings))
    pdf=out/'main.pdf'
    (ROOT/'verification').mkdir(exist_ok=True)
    (ROOT/f'verification/build-{lang}.json').write_text(json.dumps({'language':lang,'inputs':before,'pdf_sha256':digest(pdf),'tex_warnings':warnings},ensure_ascii=False,indent=2)+'\n')
    print(lang+': '+str(pdf.relative_to(ROOT)))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--lang',choices=['zh','en','all'],default='all');args=parser.parse_args()
    if not shutil.which('xelatex'):raise SystemExit('Install XeLaTeX first; see BUILDING.md')
    for lang in ['zh','en'] if args.lang=='all' else [args.lang]:build(lang)
