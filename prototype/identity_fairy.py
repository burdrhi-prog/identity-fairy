"""Identity Fairy: local-only, synthetic snapshot comparison and explainability demo."""
import argparse
import json
from pathlib import Path

KINDS = {"account", "recovery_method", "logical_client", "session", "device_record", "permission"}
STATUSES = {"known", "unrecognized", "disputed", "unresolved"}
def load_snapshot(path):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data,dict) or not isinstance(data.get("records"),list):
        raise ValueError("snapshot must contain a records list")
    records={}
    for row in data["records"]:
        if not isinstance(row,dict) or not all(isinstance(row.get(k),str) and row[k].strip() for k in ("id","kind","provider","account","source_ref","observed_at","status")):
            raise ValueError("record requires id, kind, provider, account, source_ref, observed_at, status")
        if row["kind"] not in KINDS or row["status"] not in STATUSES:
            raise ValueError("invalid kind or status")
        from datetime import datetime
        dt=datetime.fromisoformat(row["observed_at"].replace("Z","+00:00"))
        if dt.tzinfo is None or dt.utcoffset() is None:
            raise ValueError("timestamps require timezone")
        if row["id"] in records:
            raise ValueError("duplicate record id")
        records[row["id"]]=row
    return records

def compare(previous,current):
    findings=[]
    for key,row in sorted(current.items()):
        old=previous.get(key)
        if old is None:
            change="new_record"
        elif any(row.get(field)!=old.get(field) for field in ("status","source_ref","observed_at","value_alias")):
            change="record_updated"
        else:
            continue
        kind=row["kind"].replace("_"," ")
        findings.append({
            "record_id":key,"change":change,"status":row["status"],
            "observed":f'{kind.capitalize()} record {key} was {"added" if old is None else "updated"} in {row["provider"]} account {row["account"]}.',
            "not_established":"This record alone does not establish who acted, unauthorized access, or a separate physical device.",
            "next_step":"Review the original provider record and confirm whether the change is recognized.",
            "source_ref":row["source_ref"],"observed_at":row["observed_at"]})
    for key,row in sorted(previous.items()):
        if key not in current:
            findings.append({"record_id":key,"change":"not_in_latest_snapshot","status":"unresolved",
                "observed":f'Record {key} is absent from the newer snapshot.',
                "not_established":"Absence from an export does not establish deletion or revocation.",
                "next_step":"Check export completeness and provider retention.",
                "source_ref":row["source_ref"],"observed_at":row["observed_at"]})
    return findings

def render(findings):
    lines=["# Identity Fairy — synthetic snapshot review","",
           "Local-only demonstration. No account connections or live monitoring.","",
           f"**Changes to review:** {len(findings)}",""]
    for f in findings:
        lines.extend([f'## {f["record_id"]} — {f["change"]}',"",
                      f'**Observed:** {f["observed"]}',
                      f'**Not established:** {f["not_established"]}',
                      f'**Next step:** {f["next_step"]}',
                      f'**Provenance:** {f["source_ref"]} | {f["observed_at"]}',""])
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("before");p.add_argument("after");p.add_argument("--output")
    a=p.parse_args()
    output=render(compare(load_snapshot(a.before),load_snapshot(a.after)))
    if a.output:
        Path(a.output).write_text(output,encoding="utf-8")
    else:
        print(output)
if __name__=="__main__":
    main()
