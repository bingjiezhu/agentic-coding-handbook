import importlib.util,json,tempfile,unittest
from pathlib import Path
MODULE=Path(__file__).resolve().parents[1]/'skills/project-guide/scripts/inspect_project.py'
spec=importlib.util.spec_from_file_location('inspect_project',MODULE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class InspectionTests(unittest.TestCase):
 def setUp(self):self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'app';self.root.mkdir()
 def tearDown(self):self.temp.cleanup()
 def write(self,path,text):p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text);return p
 def snapshot(self):return {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file() and not p.is_symlink()}
 def test_new_project_is_not_called_initialized(self):
  before=self.snapshot();r=m.inspect(self.root);self.assertFalse(r['specify_directory_present']);self.assertIsNone(r['active_feature']);self.assertEqual(before,self.snapshot())
 def test_uses_active_state_and_reports_user_only_skill(self):
  self.write('.specify/feature.json',json.dumps({'feature_directory':'specs/chosen'}));self.write('specs/chosen/spec.md','# Requirements');self.write('specs/other/plan.md','# Not active')
  self.write('.claude/skills/speckit-plan/SKILL.md','---\nname: speckit-plan\ndescription: Plan\ndisable-model-invocation: true\n---\n# Plan')
  before=self.snapshot();r=m.inspect(self.root);self.assertEqual(r['active_feature'],'specs/chosen');self.assertEqual(r['feature_files_present'],['spec.md']);self.assertTrue(r['installed_steps'][0]['user_invocation_only']);self.assertEqual(before,self.snapshot())
 def test_malformed_state_is_visible(self):
  self.write('.specify/feature.json','{wrong');r=m.inspect(self.root);self.assertIsNone(r['active_feature']);self.assertTrue(any('Invalid active feature' in n for n in r['notes']))
 def test_outside_feature_and_symlink_are_not_read(self):
  outside=self.root.parent/'private';outside.mkdir();(outside/'spec.md').write_text('private')
  self.write('.specify/feature.json',json.dumps({'feature_directory':'../private'}));r=m.inspect(self.root);self.assertIsNone(r['active_feature']);self.assertEqual(r['feature_files_present'],[])
  (self.root/'escape').symlink_to(outside,target_is_directory=True);r=m.inspect(self.root,'escape');self.assertIsNone(r['active_feature'])
 def test_explicit_override_and_implicit_policy(self):
  self.write('.specify/feature.json',json.dumps({'feature_directory':'specs/old'}));self.write('specs/new/plan.md','# Plan')
  self.write('.agents/skills/speckit-plan/SKILL.md','---\nname: speckit-plan\ndescription: Plan\n---\n# Plan');self.write('.agents/skills/speckit-plan/agents/openai.yaml','policy:\n  allow_implicit_invocation: false\n')
  r=m.inspect(self.root,'specs/new');self.assertEqual(r['active_feature'],'specs/new');self.assertEqual(r['feature_files_present'],['plan.md']);self.assertTrue(r['installed_steps'][0]['implicit_invocation_disabled'])
 def test_yaml_comments_do_not_hide_invocation_restrictions(self):
  self.write('.claude/skills/speckit-plan/SKILL.md','---\nname: speckit-plan\ndescription: Plan\ndisable-model-invocation: true # user only\n---\n')
  self.write('.agents/skills/speckit-plan/SKILL.md','---\nname: speckit-plan\ndescription: Plan\n---\n')
  self.write('.agents/skills/speckit-plan/agents/openai.yaml','interface:\n  display_name: Plan\npolicy:\n  allow_implicit_invocation: false # explicit only\n')
  steps={x['host']:x for x in m.inspect(self.root)['installed_steps']}
  self.assertTrue(steps['claude']['user_invocation_only']);self.assertTrue(steps['codex']['implicit_invocation_disabled'])
 def test_ambiguous_or_unsupported_flags_are_unknown(self):
  self.write('.claude/skills/speckit-plan/SKILL.md','---\nname: speckit-plan\ndescription: Plan\ndisable-model-invocation: true\ndisable-model-invocation: false\n---\n')
  self.write('.agents/skills/speckit-plan/SKILL.md','---\nname: speckit-plan\ndescription: Plan\n---\n')
  self.write('.agents/skills/speckit-plan/agents/openai.yaml','policy: {allow_implicit_invocation: false}\n')
  r=m.inspect(self.root);steps={x['host']:x for x in r['installed_steps']}
  self.assertIsNone(steps['claude']['user_invocation_only']);self.assertIsNone(steps['codex']['implicit_invocation_disabled']);self.assertTrue(any('Unknown' in n for n in r['notes']))
 def test_unclosed_frontmatter_is_unknown_instead_of_enabled(self):
  self.write('.claude/skills/speckit-plan/SKILL.md','---\nname: speckit-plan\ndescription: Plan\n')
  r=m.inspect(self.root);self.assertIsNone(r['installed_steps'][0]['user_invocation_only']);self.assertTrue(any('frontmatter' in n for n in r['notes']))
 def test_indented_separator_in_description_does_not_end_frontmatter(self):
  self.write('.claude/skills/speckit-plan/SKILL.md','---\nname: speckit-plan\ndescription: |\n  Plan a feature.\n  ---\n  Additional description.\ndisable-model-invocation: true\n---\n')
  self.assertTrue(m.inspect(self.root)['installed_steps'][0]['user_invocation_only'])
if __name__=='__main__':unittest.main()
