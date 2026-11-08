# Feasibility and MVP — November 2026

## What is already established
The concept has a defined problem, user experience principles, a proposed event/evidence model, and a manual research foundation: a multi-provider investigation workbook. A previous local graph prototype was described in project history (99 entities and 194 same-row relationships in one source snapshot); **that historical prototype has not been imported, reproduced, or independently verified in this repository**.

## Product loop: REMEMBER → COMPARE → ASK → PRESERVE → EXPLAIN
- **Remember:** User-managed inventory of accounts, aliases, devices, recovery methods, and history—including incomplete identities (“I found another piece of me”).
- **Compare:** Detect changes between user-provided provider-export snapshots.
- **Ask:** Request human confirmation of known/disputed/unresolved relationships.
- **Preserve:** Retain source reference, original timestamp, previous classification, and reason for reclassification.
- **Explain:** Provide concise, compassionate language with expandable technical provenance.

## Feasible first release (proposed)
1. Offline, single-user prototype with **synthetic data only**.
2. CSV import and deterministic validation; preserve source fields and UTC conversion.
3. Identity graph with typed nodes (account, alias, recovery method, logical client, event) and source-linked edges.
4. Snapshot diff statuses: NEW, CHANGED, MISSING, KNOWN, UNRECOGNIZED, UNRESOLVED, RECLASSIFIED.
5. Timeline and explanation cards: observed / correlated / unresolved / next verification.
6. Export of a reviewable, portable evidence summary.

## Defer until proven safe and useful
- Direct provider API connections or background monitoring: provider permissions and ongoing integration burden.
- Financial account integrations: heightened privacy, authorization, and regulatory implications.
- Ambient physical fairy notifier: optional hardware concept, not required for MVP; no credentials or full evidence store on hardware.
- Household display / Guardian remote capabilities: strict authorization boundaries and additional threat modeling needed.
- AI-generated conclusions: optional explanation assistance only after deterministic evidence rules and human review.

## Product feasibility questions
Can users import provider data successfully? Does the graph reduce confusion? Can the interface avoid false alarms? How will encryption, retention, deletion, backups, and consent be implemented and tested? What integrations are actually available and permitted?

**No live monitoring, consumer release, validated market demand, or tested security controls are claimed.**
