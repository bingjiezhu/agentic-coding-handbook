# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Bingjie Zhu
"""Read-only inventory for the Project Guide. Does not execute project code."""
from pathlib import Path
import argparse,json,os,re,shutil,subprocess

STEPS=('constitution','specify','clarify','plan','checklist','tasks','analyze','implement','converge')

def inside(root,path):
    try:return path.resolve().is_relative_to(root)
    except (OSError,RuntimeError):return False

def exists_inside(root,path):return inside(root,path) and path.is_file()

def inspect(root,feature_override=None):
    root=Path(root).expanduser().resolve()
    if not root.is_dir():raise ValueError('Project directory does not exist; choose the target folder before initialization.')
    result={'project':str(root),'rules_and_records':[p for p in ('AGENTS.md','CLAUDE.md','README.md','PROJECT_BRIEF.md','PROGRESS.md') if exists_inside(root,root/p)],'specify_cli_on_path':bool(shutil.which('specify')),'specify_directory_present':inside(root,root/'.specify') and (root/'.specify').is_dir(),'active_feature':None,'feature_files_present':[],'installed_steps':[],'notes':[]}
    state=root/'.specify/feature.json';selected=feature_override
    if selected is not None:
        result['feature_selection_source']='explicit override'
    elif exists_inside(root,state):
        result['feature_selection_source']='.specify/feature.json'
        try:
            data=json.loads(state.read_text(encoding='utf-8'))
            if not isinstance(data,dict) or not isinstance(data.get('feature_directory'),str) or not data['feature_directory'].strip():raise ValueError('feature_directory must be a nonempty string')
            selected=data['feature_directory']
        except (ValueError,OSError,UnicodeError) as error:result['notes'].append('Invalid active feature state: '+str(error))
    elif state.exists():result['notes'].append('Active feature state is outside the project; not read.')
    else:result['feature_selection_source']='not set'
    if selected:
        path=Path(selected);path=path if path.is_absolute() else root/path
        if not inside(root,path):result['notes'].append('Active feature points outside the project; not inspected. Confirm scope first.')
        else:
            result['active_feature']=path.resolve().relative_to(root).as_posix()
            result['feature_files_present']=[name for name in ('spec.md','research.md','plan.md','tasks.md','quickstart.md','data-model.md') if exists_inside(root,path/name)]
            if not path.is_dir():result['notes'].append('Selected feature directory does not exist.')
    for host,folder in [('codex','.agents/skills'),('claude','.claude/skills')]:
        for step in STEPS:
            path=root/folder/('speckit-'+step)/'SKILL.md'
            if not exists_inside(root,path):continue
            try:
                text=path.read_text(encoding='utf-8');front=text.split('---',2)[1] if text.startswith('---') else ''
                user_only=bool(re.search(r'^disable-model-invocation:\s*true\s*$',front,re.M))
                config=path.parent/'agents/openai.yaml'
                implicit_disabled=exists_inside(root,config) and bool(re.search(r'^\s*allow_implicit_invocation:\s*false\s*$',config.read_text(encoding='utf-8'),re.M))
                result['installed_steps'].append({'host':host,'step':step,'path':path.relative_to(root).as_posix(),'user_invocation_only':user_only,'implicit_invocation_disabled':implicit_disabled,'session_loading':'not observable from files'})
            except (OSError,UnicodeError) as error:result['notes'].append('Cannot read '+str(path.relative_to(root))+': '+str(error))
    result['notes'].append('File presence does not establish artifact quality, completed work or callable skill availability. Inspect content and host capabilities before selecting a stage.')
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('project');parser.add_argument('--feature',help='Explicit active feature override, checked within the project');args=parser.parse_args()
    try:result=inspect(args.project,args.feature if args.feature is not None else os.environ.get('SPECIFY_FEATURE_DIRECTORY'))
    except (ValueError,OSError) as error:parser.exit(2,str(error)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
