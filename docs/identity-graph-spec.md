# Evidence-linked Identity Graph — Draft Specification

## Entities
Person-confirmed identity; account; email/alias; phone/recovery method; provider; device record; logical browser/client registration; session; authentication event; IP/network observation; permission/OAuth grant; source artifact.

Each object receives a **typed namespace**. An identifier from one provider must not be merged with another namespace merely because values or timestamps resemble each other.

## Relationships
Examples: account HAS_RECOVERY_METHOD alias; event OBSERVED_ON logical_client; session ASSOCIATED_WITH account; event REFERENCED_BY source_record; user CONFIRMED_OWNERSHIP_OF device.

Each edge should store: source file reference, worksheet/row or event ID, original and normalized timestamps, relation type, direct-vs-inferred, classification, and missing verification bridge.

## Classification
- Provider-recorded fact
- User-confirmed control
- Technical correlation
- Disputed association
- Unresolved attribution
- Hypothesis requiring verification

A registration is not a physical device; a physical device is not an identified operator. IP proximity is not proof of user control.

## Example explanation
**Observed:** Two distinct client IDs appear in records for the same account.
**Possible interpretations:** Separate browser profiles, re-registration, or different devices.
**Not established:** Who operated either client, or whether access was unauthorized.
**Next verification:** Compare exact device/session bridges and provider records.

All examples must use synthetic identities and identifiers.
