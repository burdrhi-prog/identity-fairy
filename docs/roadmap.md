# Identity Fairy — Three Development Milestones

**Product:** a local-first account-awareness application for tablet/computer, with an optional colour-changing physical companion. The September 2026 ambient-companion concept is the design origin; the November 2026 Python snapshot comparator is the initial executable foundation.

## Milestone 1 — Make the Fairy visible (next)
**Goal:** a tablet-friendly, accessible local dashboard using fictional events.

- Five original ambient states: **Teal — All Good; Indigo — Heads Up; Purple — Investigating; Amber — Action Needed; Red — Urgent**.
- Distinct **No recent data / Monitoring unavailable** state: never falsely imply everything is safe.
- State must reflect *review priority and data freshness*, not certainty that a breach occurred.
- Interactive synthetic scenarios and a panel explaining why the Fairy changed colour.
- Keyboard, screen-reader text, and shape/text labels so colour is never the only signal.
- No provider credentials or live monitoring.

**Done when:** the dashboard runs locally on a computer/tablet browser, users can switch between fictional scenarios, status changes match tested rules, and each state has readable context.

## Milestone 2 — Make the Fairy useful
**Goal:** link the interface to evidence-aware account history.

- Integrate existing synthetic snapshot comparator.
- Account, recovery method, permission, session and logical client history.
- User recognition / disputed / unresolved review workflow, separate from provider facts.
- Source references, original timestamps, normalized UTC, correction audit trail and export completeness.
- Import validation, duplicate handling, uncertainty rules and test coverage.
- Local data retention, deletion, privacy and threat model before any real user records.

**Done when:** a fictional account change can be imported, reviewed, explained, acknowledged, and traced back to its synthetic source without actor attribution.

## Milestone 3 — Bring the Fairy into the physical world
**Goal:** optional monitor-mounted ambient companion.

- Revisit the September 14, 2026 L-shaped Fairy concept, translucent RGB illumination, USB-C and proposed ESP32-S3; dimensions/components are **design proposals, not validated specifications**.
- Define a minimal local status-only interface: state, freshness and acknowledgement indication; **never** send account identifiers, credentials, logs or evidence to hardware.
- Prototype simulator first; then investigate electronics, enclosure, power and accessibility.
- Hardware should fail to neutral/offline when disconnected, not continue displaying a reassuring green/teal.
- Hardware remains optional: software must work without it.

**Done when:** a simulator or physical prototype reflects tested app status, including offline state, without receiving private evidence.

## Existing work (already committed, not milestone completion)
- Product and evidence-model documentation.
- Synthetic Python before/after snapshot comparison and unit tests.
- GitHub Actions test workflow configured; successful execution must be verified separately.

## Constraints
No real investigation records in public GitHub. No claim of live provider monitoring, breach detection, verified device ownership or physical hardware. Correlation is not attribution.

## Tracking
See repository Issues labelled by title prefix **[M1]**, **[M2]**, and **[M3]**. GitHub's native Milestones creation is not available through the current connector, so these are project milestone groups, not native GitHub Milestone objects.
