# Research-to-requirements: private workbook methods → Identity Fairy

**Boundary:** This document abstracts design methods from the private investigation workbook dated 2026-11-06 (149 worksheets inspected at sheet-inventory level, with selected method sheets reviewed) and earlier product conversations. It is not a complete audit of every workbook cell or every conversation, and contains no personal records.

## What the workbook teaches the product
| Private research method | Fairy feature requirement | Acceptance criterion |
|---|---|---|
| Evidence Index + Master Timeline | Source-linked event history | Every displayed event links to a source pointer and original time |
| Identifier Crosswalk + Client ID Crosswalk | Typed identity relationships | A logical registration cannot silently become a hardware or person identity |
| Corrections and duplicate review | Append-only corrections, source deduplication | A correction retains prior value and explanation; repeated citations do not count as independent proof |
| Current Authority Matrix + recovery-path audits | Account authority and recovery history | Recovery method, OAuth grant, session and control status are distinct objects |
| Verified Self Baselines | User-recognized context | Exact known baseline only; never generalize nearby IPs or lookalike devices |
| Attribution Workflow + Critical Gaps | Evidence-calibrated explanation | Facts, correlation, user report, hypothesis and missing bridge are separate |
| Multi-provider event overlap | Cross-provider temporal review | Time proximity prompts review; no automatic actor attribution |
| Disputed and unresolved lineages | User confirmation and reversible classification | Recognition/dispute status is explicit, revisable and source-linked |

## Distinctive product behavior
REMEMBER → COMPARE → ASK → PRESERVE → EXPLAIN.

1. **Remember:** inventory accounts, forgotten/legacy identities, recovery channels, device and logical client histories.
2. **Compare:** identify historical changes without treating absence from an export as proof of deletion.
3. **Ask:** invite the account owner to classify a change as known, unrecognized, disputed, or unresolved.
4. **Preserve:** local-first snapshots; proposed offline-readable last-known state and opt-in emergency USB pack.
5. **Explain:** calm household-language observation, what is not established, and a technical evidence handoff.

## Additional concepts from earlier design discussions
- Optional ambient physical Fairy indicator for households; not a database, not a credential store.
- Calm states: All Good / Heads Up / Investigating / Action Needed / Urgent. These are UX proposals, not implemented risk ratings.
- Support travel, family and work/personal identity inventories without assuming a single person owns every related account.
- Provider-neutral architecture: do not make Google or any monitored provider the only custodian of the history.
- Stay within explicitly user-authorized sources and trusted environments. No arbitrary network scans.
- Consider low-bandwidth and offline contexts and accessibility, including communities with limited connectivity.
- Avoid diagnosing compromise from an unfamiliar client ID, shared IP, or repeated logical registration.

## Honest implementation status
The committed standard-library prototype compares two **synthetic JSON snapshots**, validates provenance and timestamps, and generates cautious explanations. It does not ingest the private workbook, connect to providers, detect intrusions, encrypt stored records, or provide live alerts. Production security, threat modeling, encryption, consent, retention, and usability validation remain open.
