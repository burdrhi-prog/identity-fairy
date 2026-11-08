# Proposed Architecture (not implemented)

```text
User-selected files (synthetic first)
            |
            v
Input validation and safe parsing
            |
            v
Normalized event model + original source references
            |
            v
Correlation and uncertainty rules
            |
            v
Plain-language explanations + review timeline
            |
            v
User-controlled export or deletion
```

## Data model draft
An event should preserve: event_id, source_provider, source_record_reference, original_timestamp, normalized_timestamp_utc, account_alias, event_type, logical_client_id (optional), observation, and interpretation_status.

Do not infer device ownership, operator identity, or unauthorized access from an identifier alone.

## Security assumptions to validate
- Local-first storage as a preferred starting architecture, not an implemented guarantee.
- Avoid collecting passwords, passkeys, tokens, or recovery codes.
- Avoid uploading real investigation exports into a demo repository.
- Treat imported records as untrusted data.
- Define deletion and retention controls before accepting sensitive user records.
