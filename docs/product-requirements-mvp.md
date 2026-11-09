# Identity Fairy MVP — product requirements and acceptance criteria

## User problem
People lose track of historical accounts, recovery methods, sessions, devices and permission grants across providers. Ordinary security notifications rarely preserve context or explain the difference between provider-recorded facts and actual user control.

## Primary persona
Household account owner who needs calm, understandable explanations and the ability to export source-linked evidence for a qualified support person.

## P0 — local synthetic proof of concept
- [x] Import two fictional snapshots with typed record kinds and source references.
- [x] Validate required identifiers and timezone-aware timestamps.
- [x] Compare snapshots and flag added, changed and absent records.
- [x] Explain observations and uncertainty without claiming compromise.
- [x] Unit tests and CI workflow defined.
- [ ] Confirm latest CI run succeeded.
- [ ] Build an accessible local visual interface.
- [ ] Add export completeness, duplicate and conflicting-source tests.

## P1 — user-driven review and preservation
- [ ] Record user recognition/dispute as a separate annotation with timestamp and evidence.
- [ ] Add immutable historical snapshot archive and correction audit trail.
- [ ] Build account → recovery → session → logical client graph with typed edges.
- [ ] Implement offline-readable state and opt-in emergency evidence pack.
- [ ] Define threat model, encryption/key management, data minimization and retention controls.

## P2 — future optional features
- [ ] Provider integrations only with explicit user authorization, scoped permissions and revocation.
- [ ] Optional ambient household indicator, without credential/evidence storage.
- [ ] Usability and accessibility tests; low-bandwidth/offline testing.
- [ ] Calibrated notification severity after research, not guessed from a single signal.

## Product metrics (proposed, not measured)
- Correct identification of snapshot changes against labeled synthetic truth.
- False-positive rate of claims implying unauthorized access.
- Percentage of findings with traceable source pointers.
- User comprehension of known vs unknown vs disputed.
- Time to prepare a technical handoff.
- Successful offline retrieval of the last-known state.

## Safety constraints
No live account monitoring, scanning outside authorized scope, credential collection, cloud dependency, or automatic operator attribution in this MVP.
