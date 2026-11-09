# Identity Fairy Home — Hardware Feasibility Research

**Record:** HF research register v0.1  
**Date opened:** 2026-11-09  
**Status:** Documentary feasibility only; no Identity Fairy physical prototype built  
**Scope:** Home Edition's optional, removable illuminated monitor companion. Enterprise account-correlation features are out of scope.

## Purpose and evidence standard

Assess whether an original character with controllable light and moving wings can act as a physical, glanceable interface to the local-first Identity Fairy application. Distinguish what a source *says* from what Identity Fairy has independently reproduced. Historical products establish precedent, not current market demand, manufacturing readiness, or legal clearance.

### HF-001 — Historical i-Buddy USB companion

- **Type:** Historical hardware precedent.
- **Sources:** User-supplied images of the MSN-branded i-Buddy; independent developer description at [pbrier/ibuddy](https://github.com/pbrier/ibuddy).
- **Observed/documented:** A small angel-like USB figure with movable wings, movable body and four LEDs, per the developer's README. Historical images show a compact physical figure; a monitor clip is described in the supplied historical material but has not been independently inspected.
- **What this supports:** A physical USB companion with lighting and movement has existed; Identity Fairy's basic interaction concept does not require inventing an entirely new class of mechanism.
- **Not yet verified:** Internal motor/gearing, USB power budget, exact dimensions, clip suitability for modern thin displays, durability, availability, production cost, or any patent/design/trademark clearance.
- **Product implication:** Study the *interaction principle* only. Develop an original Fairy/Desk Dude appearance, mounting method and electronics; do not copy branding or protected designs.
- **Evidence status:** Supported historical precedent; physical teardown/testing pending.

### HF-002 — Independent i-Buddy control program

- **Type:** Software feasibility reference.
- **Primary source:** [pbrier/ibuddy GitHub repository](https://github.com/pbrier/ibuddy), README shown in user-provided screenshot dated 2026-11-09.
- **Developer's documented claims:** Command-line program to control an i-Buddy USB device with movable body, wings and four LEDs; based on Ib uddyLib C# software, PyBuddyLib and LibHID; tested on Windows using MinGW. (Check exact upstream dependency spelling in source before relying on it.)
- **What this supports:** A developer has documented an approach for controlling the historical USB character independently of its original MSN application.
- **Not yet verified:** The exact command bytes, claimed U/D/C/A/R/G/B/H mappings appearing in a Google-generated summary, hardware compatibility, successful reproduction on a current computer, source-code licence and obligations, and suitability for reuse.
- **Product implication:** Investigate the repository as a technical reference. A modern USB-capable microcontroller with our own minimal status protocol may be simpler than reproducing obsolete drivers.
- **Evidence status:** Primary developer documentation inspected via screenshot; code, licence and physical test pending.

## Identity Fairy Home: minimum demonstration

```text
Synthetic or explicitly imported security event
  -> local comparison / review-status rules
  -> explainable application alert
  -> minimal USB status signal
  -> original fairy: light + wing movement
```

The hardware should receive **only a status code, freshness/connection state and optional motion command**, never account identifiers, credentials, IP addresses or raw logs. It must have an unmistakable offline/unavailable state, user-adjustable brightness and motion-off mode. Status colours should follow the existing [ambient hardware design brief](ambient-companion-hardware.md) and [roadmap](roadmap.md), rather than introducing a conflicting palette. A reassuring state never means that all accounts are secure.

**Product hypothesis:** The fairy reduces the need to remember to check a dashboard by signalling *new, supported, actionable changes*. This is a usability hypothesis to test, not a demonstrated outcome.

## Next checks (no purchases authorized)

1. Inspect upstream `pbrier/ibuddy` source and actual licence; document version/commit.
2. Confirm the original hardware control behaviour from source, not a generated search summary.
3. Select a small controller, LED and wing-actuation approach for an **original** prototype; test power, noise and safety.
4. Build a software simulator that displays the same status messages before ordering components.
5. Get approximate component and enclosure quotes; validate usefulness with a small, consent-based demonstration using fictional events.

## Commercial and safety boundaries

- No public upload of the user's personal investigation or survivor account data.
- No claim of live monitoring, intrusion detection, complete provider coverage, or confirmed account security.
- Historical i-Buddy materials are research references, **not** an affiliation, endorsement, or licence to manufacture a copy.
- Business feasibility, willingness to pay, and manufacturing costs require separate validation.
- A discreet software-only mode matters for users whose environments may be unsafe.

**Related:** [Ambient companion design brief](ambient-companion-hardware.md) · [Development roadmap](roadmap.md).
