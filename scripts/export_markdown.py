"""Export the handbook's small LaTeX vocabulary to GitHub Markdown and prompt files."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
CHAPTERS=[('00_guide','00-overview'),('01_goal','01-define-the-task'),('01_structure','02-project-files'),('02_project','03-research-first'),('02_speckit','04-spec-kit'),('03_build','05-small-steps'),('04_check','06-acceptance-checks'),('05_debug','07-debugging'),('06_parallel','08-multiple-agents'),('07_review','09-independent-review'),('08_resume','10-long-tasks'),('09_reuse','11-rules-and-skills'),('10_batch','12-batch-work'),('12_summary','13-summary')]

def group(s,start):
    assert s[start]=='{',(s[start:start+20],start)
    level=1;i=start+1
    while level:
        if i>=len(s):raise ValueError('Unbalanced TeX group')
        if s[i]=='{' and s[i-1]!='\\':level+=1
        elif s[i]=='}' and s[i-1]!='\\':level-=1
        i+=1
    return s[start+1:i-1],i

def commands(s,cmd,count,fn):
    pattern=re.compile(r'\\'+re.escape(cmd)+r'(?![A-Za-z])\s*')
    pos=0
    while m:=pattern.search(s,pos):
        i=m.end();args=[]
        for _ in range(count):
            while i<len(s) and s[i].isspace():i+=1
            arg,i=group(s,i);args.append(arg)
        value=fn(*args);s=s[:m.start()]+value+s[i:];pos=m.start()+len(value)
    return s

def inline(s):
    s=s.replace('\\newline','<br>').replace('\\allowbreak','').replace('\\par','\n\n').replace('~',' ')
    s=commands(s,'href',2,lambda url,label:f'[{inline(label)}]({url})')
    for c,wrapper in [('texttt','`'),('textbf','**'),('emph','*'),('textsf','')]:s=commands(s,c,1,lambda a,w=wrapper:w+inline(a)+w)
    s=commands(s,'textcolor',2,lambda color,text:inline(text))
    s=s.replace('\\$','$').replace('\\&','&').replace('\\_','_').replace('\\%','%')
    s=s.replace('``','“').replace("''",'”')
    return re.sub(r'\n{3,}', '\n\n', s).strip()

def export(lang):
    out=ROOT/'docs'/lang;out.mkdir(parents=True,exist_ok=True)
    titles=[];allcards=[]
    for source,slug in CHAPTERS:
        s=(ROOT/f'src/{lang}/{source}.tex').read_text()
        # Prompts are literal copyable instructions, protected from prose formatting.
        stored=[]
        def prompt(m):
            title,body=m.groups();body=inline(body)
            stored.append('### '+title+'\n\n```text\n'+body+'\n```\n')
            allcards.append({'number':len(allcards)+1,'chapter':slug,'title':title,'text':body})
            return '\n\nPROMPTTOKEN'+str(len(stored)-1)+'ENDTOKEN\n\n'
        s=re.sub(r'\\begin\{prompt\}\{([^}]+)\}(.*?)\\end\{prompt\}',prompt,s,flags=re.S)
        title_match=re.search(r'\\lesson\{[^}]+\}\{([^}]+)\}|\\section\*\{([^}]+)\}',s)
        assert title_match,source;title=next(x for x in title_match.groups() if x is not None);titles.append((slug,title))
        s=commands(s,'lesson',2,lambda key,t:'# '+t+'\n')
        s=s.replace('\\clearpage','')
        s=re.sub(r'\\section\*\{([^}]+)\}',r'# \1\n',s)
        s=commands(s,'label',1,lambda x:'');s=commands(s,'markboth',2,lambda a,b:'')
        s=commands(s,'lede',1,lambda x:x+'\n')
        s=commands(s,'topic',1,lambda x:'\n\n## '+x+'\n\n')
        s=commands(s,'principle',2,lambda h,b:'\n\n## '+h+'\n\n'+b+'\n')
        s=commands(s,'diagram',1,lambda key:'\n\n!['+title+'](../../assets/diagrams/'+lang+'/'+key+'.svg)\n\n')
        def table(m):
            content=m.group(1);content=content.replace('\\toprule','').replace('\\midrule','').replace('\\bottomrule','')
            rows=[row.strip() for row in re.split(r'\\\\(?:\[[^\]]*\])?',content) if row.strip()]
            parsed=[[inline(c) for c in re.split(r'(?<!\\)&',row)] for row in rows]
            assert parsed and all(len(row)==len(parsed[0]) for row in parsed),(source,parsed)
            lines=['| '+' | '.join(row)+' |' for row in parsed];lines.insert(1,'| '+' | '.join('---' for _ in parsed[0])+' |')
            return '\n\n'+'\n'.join(lines)+'\n\n'
        s=re.sub(r'\\begin\{tabularx\}\{\\linewidth\}\{[^\n]*\}(.*?)\\end\{tabularx\}',table,s,flags=re.S)
        s=s.replace('\\begin{enumerate}','\n').replace('\\end{enumerate}','\n')
        s=re.sub(r'\\item\s*','\n1. ',s)
        s=re.sub(r'\\vspace\{[^}]+\}','',s)
        s=re.sub(r'\\renewcommand\{\\arraystretch\}\{[^}]+\}','',s)
        s=s.replace('\\begingroup','').replace('\\endgroup','').replace('\\smallskip','')
        s=s.replace('{\\footnotesize\\color{muted}','').rstrip()
        if s.endswith('}'):s=s[:-1] if source=='12_summary' else s
        s=inline(s)
        for i,body in enumerate(stored):s=s.replace('PROMPTTOKEN'+str(i)+'ENDTOKEN',body)
        s=re.sub(r'\n{3,}','\n\n',s).strip()+'\n'
        assert not re.search(r'\\[a-zA-Z]',s),(source,'unconverted TeX',re.findall(r'\\[a-zA-Z]+',s))
        # Normalize source line wraps while retaining Markdown blocks.
        lines=s.splitlines();joined=[]
        for line in lines:
            if joined and line and joined[-1] and not re.match(r'[#|!`]|\d+\. ',line) and not re.match(r'[#|!`]|\d+\. ',joined[-1]):
                # Keep original paragraphs as paragraphs, not hard line breaks.
                joined[-1]+=('' if lang=='zh' else ' ')+line
            else:joined.append(line)
        # Prompt fences must retain their original line breaks. Source prompts are already paragraphs.
        body='\n'.join(joined)+'\n'
        alt='en' if lang=='zh' else 'zh'
        nav=f'[English](../en/{slug}.md) · [简体中文](../zh/{slug}.md) · [Home](../../README.md)\n\n'
        (out/(slug+'.md')).write_text(nav+body)
    index='# '+('阅读目录' if lang=='zh' else 'Reading Guide')+'\n\n'+ ('按顺序阅读，或选择当前需要的章节。\n\n' if lang=='zh' else 'Read in order, or jump to the chapter you need.\n\n')
    index+='\n'.join('- ['+title+']('+slug+'.md)' for slug,title in titles)+'\n'
    (out/'README.md').write_text(index)
    text='# '+('可复制提示词' if lang=='zh' else 'Copyable Prompts')+'\n\n'
    text+=('每次选一条，替换方括号后发送给能访问项目的编程智能体。详细用法见[工作框架](../docs/zh/00-overview.md)。\n\n' if lang=='zh' else 'Choose one prompt, fill in the brackets and send it to a coding agent with project access. See [the overview](../docs/en/00-overview.md) for instructions.\n\n')
    for c in allcards:text+='## '+str(c['number']).zfill(2)+' · '+c['title']+'\n\n[Chapter](../docs/'+lang+'/'+c['chapter']+'.md)\n\n```text\n'+c['text']+'\n```\n\n'
    (ROOT/f'prompts/{lang}.md').write_text(text.rstrip()+'\n')
    (ROOT/f'prompts/{lang}.json').write_text(json.dumps(allcards,ensure_ascii=False,indent=2)+'\n')
    assert len(allcards)==13
    return titles

if __name__=='__main__':
    for lang in ['zh','en']:export(lang)
    print('Exported 14 reading pages and 13 prompt cards per language.')
