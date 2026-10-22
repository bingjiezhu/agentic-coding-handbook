import importlib.util
import tempfile
import unittest
from pathlib import Path

path=Path(__file__).resolve().parents[1]/'scripts/validate_repo.py'
spec=importlib.util.spec_from_file_location('validate_repo',path)
validator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class PromptConsistencyTests(unittest.TestCase):
    def test_collection_drift_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            (root/'docs/en').mkdir(parents=True)
            (root/'prompts').mkdir()
            chapter='```text\nPreserve existing work.\n```\n'
            (root/'docs/en/01-task.md').write_text(chapter)
            collection=root/'prompts/en.md'
            collection.write_text(chapter)
            validator.check_prompt_consistency(root,'en')
            collection.write_text('```text\nReplace existing work.\n```\n')
            with self.assertRaises(AssertionError):
                validator.check_prompt_consistency(root,'en')

    def test_reordered_cards_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            (root/'docs/zh').mkdir(parents=True)
            (root/'prompts').mkdir()
            first='```text\n先明确要求。\n```\n'
            second='```text\n再检查结果。\n```\n'
            (root/'docs/zh/01-task.md').write_text(first)
            (root/'docs/zh/02-check.md').write_text(second)
            (root/'prompts/zh.md').write_text(second+first)
            with self.assertRaises(AssertionError):
                validator.check_prompt_consistency(root,'zh')

if __name__=='__main__':unittest.main()
