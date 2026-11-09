import unittest
from pathlib import Path
from identity_fairy import load_snapshot, compare, render
BASE=Path(__file__).resolve().parent
class FairyTests(unittest.TestCase):
    def test_two_changes(self):
        self.assertEqual(len(compare(load_snapshot(BASE/"before.json"),load_snapshot(BASE/"after.json"))),2)
    def test_no_operator_attribution(self):
        text=render(compare(load_snapshot(BASE/"before.json"),load_snapshot(BASE/"after.json")))
        self.assertIn("does not establish who acted",text)
        self.assertIn("SYN-B:8",text)
    def test_missing_record_not_deletion(self):
        a=load_snapshot(BASE/"after.json");b=load_snapshot(BASE/"before.json")
        result=compare(a,b)
        self.assertTrue(any(f["change"]=="not_in_latest_snapshot" and "does not establish deletion" in f["not_established"] for f in result))
    def test_rejects_naive_time(self):
        import json,tempfile
        data={"records":[{"id":"a","kind":"session","provider":"p","account":"x","source_ref":"s","observed_at":"2026-01-01T10:00:00","status":"known"}]}
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"bad.json";p.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError,"timezone"):
                load_snapshot(p)
if __name__=="__main__":unittest.main()
