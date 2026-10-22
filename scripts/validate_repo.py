"""Validate the lean guide's links, package references and reading-edition structure."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]

def validate():
    required=['README.md','README.zh-CN.md','START.md','AGENTS.md','skills/project-guide/SKILL.md','skills/project-guide/agents/openai.yaml','skills/project-guide/references/spec-kit.md','skills/project-guide/references/project-records.md','skills/project-guide/scripts/inspect_project.py','LICENSE','LICENSE-CODE']
    for name in required:assert (ROOT/name).is_file(),name
    skill=ROOT/'skills/project-guide';text=(skill/'SKILL.md').read_text()
    assert text.startswith('---\n') and re.search(r'^name: project-guide$',text,re.M)
    assert re.search(r'^description: .+',text,re.M) and '[TODO' not in text
    # CFF's root type is software/dataset; manual belongs in preferred-citation.
    citation=(ROOT/'CITATION.cff').read_text()
    root_types=re.findall(r'^type:\s*(\S+)\s*$',citation,re.M)
    assert len(root_types)==1 and root_types[0] in ('software','dataset'),'Invalid CFF root type'
    links=0
    for path in [*ROOT.glob('*.md'),*ROOT.glob('docs/**/*.md'),*ROOT.glob('prompts/*.md'),*skill.rglob('*.md')]:
        content=re.sub(r'```.*?```','',path.read_text(),flags=re.S)
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^)]+)\)',content):
            if re.match(r'^(https?://|mailto:|#)',target):continue
            dest=(path.parent/target.split('#')[0]).resolve()
            assert dest.is_relative_to(ROOT) and dest.exists(),(str(path.relative_to(ROOT)),target)
            if path.is_relative_to(skill):assert dest.is_relative_to(skill),'Installed Skill must be self-contained: '+target
            links+=1
    for lang in ['zh','en']:
        chapters=[p for p in (ROOT/f'docs/{lang}').glob('*.md') if re.match(r'\d{2}-',p.name)]
        assert len(chapters)==14,(lang,len(chapters))
        cards=re.findall(r'```text\n(.*?)\n```',(ROOT/f'prompts/{lang}.md').read_text(),re.S)
        assert len(cards)==13,(lang,len(cards))
        assert all(c.count('[')==c.count(']') for c in cards),lang
    for folder in ['src','verification','pdf']:
        assert not (ROOT/folder).exists(),f'Keep publication files in release assets, not main: {folder}'
    assert not [p for p in (ROOT/'assets').rglob('*') if p.is_file() and p.suffix!='.svg']
    print(json.dumps({'status':'passed','local_links':links,'skill_self_contained':True,'chapters_per_language':12,'prompts_per_language':13,'publication_duplicates_on_main':False},indent=2))
if __name__=='__main__':validate()
