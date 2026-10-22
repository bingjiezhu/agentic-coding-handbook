"""Check bilingual source, generated pages, copyable prompts and PDF artifacts."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,unicodedata
import pdfplumber
from pypdf import PdfReader
from export_markdown import CHAPTERS,inline
ROOT=Path(__file__).resolve().parents[1]

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):
    s=unicodedata.normalize('NFKC',s).replace('’',"'").replace('‘',"'").replace('“','\"').replace('”','\"')
    s=re.sub(r'\s+','',s).replace('\u00ad','')
    return re.sub(r'(?<=[A-Za-z])-(?=[A-Za-z])','',s)
def source_cards(lang):
    cards=[]
    for source,slug in CHAPTERS:
        text=(ROOT/f'src/{lang}/{source}.tex').read_text()
        for title,body in re.findall(r'\\begin\{prompt\}\{([^}]+)\}(.*?)\\end\{prompt\}',text,re.S):cards.append((slug,title,inline(body)))
    return cards

def check_links(candidate=False):
    checked=0
    for path in [*ROOT.glob('*.md'),*ROOT.glob('docs/**/*.md'),*ROOT.glob('prompts/*.md')]:
        text=re.sub(r'```.*?```','',path.read_text(),flags=re.S)
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^)]+)\)',text):
            if re.match(r'^(https?://|mailto:|#)',target):continue
            f=(path.parent/target.split('#')[0]).resolve()
            if candidate and f.parent==ROOT/'pdf' and f.suffix=='.pdf':
                lang=f.stem.rsplit('-',1)[-1];assert (ROOT/f'build/{lang}/main.pdf').is_file()
            else:assert f.is_relative_to(ROOT) and f.exists(),(path.relative_to(ROOT),target)
            checked+=1
    return checked

def render(pdf,lang):
    from PIL import Image,ImageDraw
    out=ROOT/f'tmp/qa/{lang}';out.mkdir(parents=True,exist_ok=True)
    for p in out.glob('*.png'):p.unlink()
    subprocess.run(['pdftoppm','-r','110','-png',str(pdf),str(out/'page')],check=True,capture_output=True)
    pages=sorted(out.glob('page-*.png'))
    for start in range(0,len(pages),3):
        sheet=Image.new('RGB',(1500,750),'#d7d1c7');draw=ImageDraw.Draw(sheet)
        for j,path in enumerate(pages[start:start+3]):
            im=Image.open(path).convert('RGB');im.thumbnail((480,700));x=j*500+10;sheet.paste(im,(x,30));draw.text((x,8),f'{lang} / {start+j+1}',fill='black')
        sheet.save(out/f'contact-{start//3+1}.png')
    return len(pages)

def verify(candidate=False,do_render=False):
    reports=[];allcards={};required_paths=[]
    for lang in ['zh','en']:
        cards=source_cards(lang);allcards[lang]=cards;assert len(cards)==13
        exported=json.loads((ROOT/f'prompts/{lang}.json').read_text())
        assert [(c['chapter'],c['title'],c['text']) for c in exported]==cards,(lang,'prompt export drift')
        md=(ROOT/f'prompts/{lang}.md').read_text();blocks=re.findall(r'```text\n(.*?)\n```',md,re.S)
        assert blocks==[c[2] for c in cards],(lang,'copyable Markdown differs')
        lessons=0;diagrams=[];headings=[]
        for source,slug in CHAPTERS:
            tex=(ROOT/f'src/{lang}/{source}.tex').read_text();lessons+=tex.count('\\lesson{')
            m=re.search(r'\\lesson\{[^}]+\}\{([^}]+)\}|\\section\*\{([^}]+)\}',tex)
            headings.append(next(x for x in m.groups() if x))
            diagrams+=re.findall(r'\\diagram\{([^}]+)\}',tex)
            path=ROOT/f'docs/{lang}/{slug}.md';assert path.is_file()
            assert not re.search(r'\\(?:texttt|begin|lesson|topic|href)\b',path.read_text())
            if lang=='en':assert not re.search(r'[\u4e00-\u9fff]',tex),(source,'untranslated English source')
        assert lessons==12 and len(diagrams)==len(set(diagrams))==13
        for key in diagrams:
            for ext in ['svg','png','pdf']:assert (ROOT/f'assets/diagrams/{lang}/{key}.{ext}').is_file()
        bound=json.loads((ROOT/f'verification/build-{lang}.json').read_text())
        for name,h in bound['inputs'].items():assert digest(ROOT/name)==h,(lang,'source changed',name)
        pdf=ROOT/(f'build/{lang}/main.pdf' if candidate else f'pdf/vibe-coding-in-practice-{lang}.pdf')
        assert digest(pdf)==bound['pdf_sha256'],(lang,'PDF not bound to current source')
        reader=PdfReader(pdf);texts=[p.extract_text() or '' for p in reader.pages]
        assert len(reader.pages)==15,(lang,len(reader.pages),'review unexpected page breaks')
        assert all(len(t)>80 for t in texts[1:]),(lang,'near empty page')
        full='\n'.join(texts)
        assert all(norm(h) in norm(full) for h in headings),(lang,'missing heading')
        assert not re.search(r'\ufffd|\?\?',full),(lang,'unresolved text')
        assert not re.search(r'[\u4e00-\u9fff]',full) if lang=='en' else True
        # pdfplumber gives more faithful line order for prompt text and glyph coordinates.
        with pdfplumber.open(pdf) as document:
            complete='\n'.join(p.extract_text(x_tolerance=2) or '' for p in document.pages)
            for i,p in enumerate(document.pages,1):
                assert not [c for c in p.chars if c['x0']<-.5 or c['x1']>p.width+.5 or c['top']<-.5 or c['bottom']>p.height+.5],(lang,i,'text outside page')
            # English line-end hyphenation is typographical, not missing prompt content.
            cleaned=re.sub(r'(?<=[A-Za-z])-\n(?=[A-Za-z])','',complete)
            for _,title,body in cards:
                assert norm(body) in norm(cleaned),(lang,title,'prompt body missing from PDF')
        reports.append({'language':lang,'pages':len(reader.pages),'chapters':lessons,'prompt_cards':len(cards),'diagrams':len(diagrams),'pdf_sha256':digest(pdf),'prompt_bodies_complete':True,'tex_warnings':bound['tex_warnings'],'rendered_pages':render(pdf,lang) if do_render else None})
    for a,b in zip(allcards['zh'],allcards['en']):
        assert a[0]==b[0] and len(re.findall(r'\[[^\]]+\]',a[2]))==len(re.findall(r'\[[^\]]+\]',b[2])),(a[1],'placeholder count mismatch')
    links=check_links(candidate)
    # Public files must not contain the author's private local workspace paths or credentials.
    patterns=[r'/Users/',r'/home/',r'gh[pousr]_[A-Za-z0-9]{20,}',r'sk-[A-Za-z0-9]{24,}',r'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----']
    for folder in ['src','docs','prompts','verification']:
        for p in (ROOT/folder).rglob('*'):
            if p.is_file() and p.suffix in ['.tex','.md','.json']:
                s=p.read_text();assert not any(re.search(pattern,s) for pattern in patterns),(str(p.relative_to(ROOT)),'private material pattern')
    result={'mode':'candidate' if candidate else 'published','editions':reports,'local_links_checked':links,'chapter_alignment':True,'placeholder_alignment':True,'private_path_scan':'passed','issues':[]}
    (ROOT/'verification'/('candidate-checks.json' if candidate else 'publication-checks.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--candidate',action='store_true');p.add_argument('--render',action='store_true');a=p.parse_args();verify(a.candidate,a.render)
