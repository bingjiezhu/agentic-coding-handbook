"""Translate existing diagram labels without changing their relationships or geometry."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
translations={
'从目标到可用结果':'From a goal to a usable result',
'说清目标':'Define the goal','范围·完成标准':'Scope / criteria','读懂项目':'Read the code','文件·已有能力':'Files / reuse','小步实现':'Build a step','接通真实操作':'Real workflow','实际检查':'Verify behavior','操作·记录·错误':'Actions / data','交接与复用':'Save / reuse','进度·规则·技能':'Progress / skills',
'独立工作可并行；发现问题后回到对应步骤修正':'Parallelize independent work; return to the relevant step when problems appear.',
'目标':'Goal','为谁解决什么':'User and problem','边界':'Scope','本版做与不做':'Include / exclude','完成标准':'Acceptance','怎样判断做对':'Observable results','最小方案':'Minimal solution','可检查的小任务':'Verifiable tasks','先明确重要选择，再安排实现':'Settle important choices before implementation.',
'确认位置':'Locate the project','目录·已有改动':'Path / existing edits','读取相关材料':'Read the inputs','代码·资料·参考':'Code / docs / sources','查已有能力':'Find reusable work','运行·复用位置':'Run / reuse locations','限定改动':'Bound the change','范围·检查方法':'Scope / checks','简短目录指向当前文件，需要时再读取细节':'Use a short index to current files; read details as needed.',
'保留旧版':'Keep a baseline','恢复位置':'Recovery point','完成一段':'Build an increment','操作到真实结果':'Action to real result','运行与对照':'Run and compare','画面·功能·记录':'UI / behavior / data','具体反馈':'Give clear feedback','位置·目标·保留项':'Where / goal / preserve','每轮聚焦一组相关改动，检查后再继续':'Focus each round on related changes; check before continuing.',
'按要求操作':'Follow the workflow','正常路径':'Normal use','核对真实记录':'Check saved data','显示与保存相符':'Display = saved data','检查异常恢复':'Check recovery','失败·重复·重开':'Failure / retry / reopen','记录结论':'Record the verdict','通过·失败·未验证':'Pass / fail / unverified','运行没有报错，仍需核对是否完成原来的目标':'No runtime error is not proof that the original goal was met.',
'保留现象':'Capture the failure','步骤·错误·截图':'Steps / errors / images','区分原因':'Test hypotheses','用检查排除猜测':'Check each hypothesis','小范围修复':'Make a small repair','依据实际观察':'Use observed evidence','原路重查':'Recheck the path','问题与相关功能':'Issue / related features','每次尝试都应增加证据，避免无依据地重写':'Each attempt should add evidence; avoid unsupported rewrites.',
'主智能体':'Lead agent','统一要求·分配范围':'Goals / scope','助手 A：查项目':'Agent A: project','可复用位置·限制':'Reuse locations / limits','助手 B：查资料':'Agent B: research','方案依据·风险':'Sources / risks','主智能体汇总':'Lead synthesizes','核对结果·安排实现':'Verify / plan edits',
'固定审查对象':'Set review scope','原要求·当前版本':'Requirements / version','独立检查':'Independent review','直接读取与运行':'Read / execute directly','逐项核对修复':'Validate and fix','明确问题和证据':'Issues / evidence','再次验证':'Recheck','修复与相关影响':'Fixes / related effects','审查意见也要核实，多个 AI 同意不能代替证据':'Verify review findings; agreement among agents is not proof.',
'保存进度':'Save progress','决定·结果·未完成':'Decisions / progress','重新开始':'Start again','打开同一项目':'Open the same project','核对实际状态':'Check current state','当前文件·关键检查':'Current files / checks','接着完成':'Continue the work','更新记录与证据':'Records / evidence','历史记录帮助恢复，当前结果仍需核对':'History supports resuming; verify what is true now.',
'认可的结果':'Accepted results','实际完成与修正':'Completed work / fixes','提取标准':'Extract guidance','规则·模板·步骤':'Rules / methods','按任务调用':'Use as needed','确认被找到与读取':'Confirm actual loading','实际复用':'Test reuse','检查质量与省时':'Quality / time saved','长期规则保持简短，专项方法按需使用':'Keep persistent rules brief; load specialized methods as needed.',
'明确清单':'Define the list','模板·完成条件':'Template / acceptance','小批试跑':'Run a small pilot','常见项·困难项':'Common / edge cases','核对结果':'Check the results','内容·格式·失败':'Content / format','通过后扩量':'Scale after passing','逐项状态·可续做':'Item status / resuming','未通过：修正规则后重试':'Failed: revise the rules and retry',
'项目文件的管理架构':'Project files and responsibilities','项目根目录':'Project root','项目入口':'Project entry points','功能文档':'Feature documents','specs/功能目录/':'specs/feature/','实现与结果':'Code and results','src/ 代码 · tests/ 检查':'src/ code / tests/ checks','.specify/（原则与流程）':'.specify/ principles','需求检查 · 验证步骤':'Requirement checks / validation','生成结果与检查记录':'Outputs / verification records','技能与可复用脚本':'Skills / reusable scripts','沿用实际项目目录':'Follow the actual project layout','文件名为常见组织方式；Spec Kit 沿用当前选定的功能目录':'Typical filenames; Spec Kit uses the currently selected feature directory.',
'需求':'Requirements','调研与方案':'Research, plan','任务拆解':'Plan tasks','实现与检查':'Build and verify','代码 · 运行结果':'Code / results','核对遗漏':'Find omissions','补齐剩余工作':'Remaining work','新证据改变方案时，先更新对应文件，再调整受影响的任务':'When evidence changes the plan, update its files and affected tasks first.'
}
data=json.loads((ROOT/'assets/diagrams/zh/data.json').read_text())
ET.register_namespace('', 'http://www.w3.org/2000/svg')
for g in data:
 key=g['key'];tree=ET.parse(ROOT/f'assets/diagrams/zh/{key}.svg');root=tree.getroot()
 # Titles and descriptions explain each workflow; text nodes retain every original concept.
 labels=[]
 for t in root.findall('.//{http://www.w3.org/2000/svg}text'):
  old=t.text or ''
  if re.search(r'[\u4e00-\u9fff]',old):assert old in translations,(key,old);t.text=translations[old]
  labels.append(t.text)
 root.find('{http://www.w3.org/2000/svg}title').text='Workflow: '+key.removeprefix('p_')
 root.find('{http://www.w3.org/2000/svg}desc').text='; '.join(x for x in labels if x and not x.isdigit())+'.'
 root.find('{http://www.w3.org/2000/svg}style').text='text{font-family:"Noto Sans","DejaVu Sans",Arial,sans-serif}.number{font-family:"DejaVu Sans Mono",monospace}'
 (ROOT/f'assets/diagrams/en/{key}.svg').write_text(ET.tostring(root,encoding='unicode'))
 (ROOT/f'assets/diagrams/en/{key}.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>'+key+'</title><style>html,body{margin:0;background:#F3EDE3}svg{display:block}</style>'+ET.tostring(root,encoding='unicode')+'</html>')
print('Translated all 13 diagrams; relationships and geometry preserved.')
