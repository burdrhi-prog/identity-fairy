# Employer-facing demonstration and honest claims

## What can be inspected today
- Product discovery grounded in a long-running multi-provider evidence-management problem.
- Requirements mapping from evidence index, identity crosswalk, authority/recovery history, corrections and provenance to testable product behaviors.
- Working synthetic snapshot comparator written in Python standard library, with tests and GitHub Actions configuration.
- Clear uncertainty language: observation ≠ compromise; logical registration ≠ physical device; provider trust ≠ user control.
- Privacy-first design decisions: no real personal records committed; local demo requires no external account access.

## How to reproduce
```bash
python -m unittest discover -s prototype -v
python prototype/identity_fairy.py prototype/before.json prototype/after.json
```
Expected: two changes (recovery-method update and newly observed session), each with provenance and an explanation of what is not established.

## Interview discussion prompts
1. Why preserve both raw provider timestamps and UTC normalized values?
2. Why is a missing record in a later export not proof of deletion?
3. What evidence would be needed to link a logical client to a physical handset?
4. Why keep user recognition separate from provider-recorded facts?
5. What would you test before handling real personal account data?

## Claims boundary
Project owner brings independent investigation and product-requirements experience; the Python implementation is AI-assisted and remains a developing skill. This is a synthetic prototype, not a deployed security product or a validated breach detector.
