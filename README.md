# Identity Fairy 🧚‍♀️
### Digital identity, explained with care.

**Identity Continuity · Local-First Prototype · Explainable Account Security · Privacy-First Product Design**

> **Status: Working synthetic snapshot-comparison prototype; not a live monitoring service.** The prototype runs locally, uses fictional records and does not connect to provider accounts.

## The idea
Account and device records can be confusing, fragmented, and frightening. **Identity Fairy** aims to help people organize what records actually show, understand what remains uncertain, and decide what to review next—without false reassurance or unnecessary alarm.

**Professional-grade evidence. Human-readable explanations.**

## Example experience (illustrative, not a live alert)
> **New client registration recorded**
>
> A provider record includes a client identifier that differs from one seen earlier. That alone does not prove another physical device or person accessed your account.
>
> **What we know:** Two logical identifiers appear in the available records.
>
> **What we don't know:** Whether they represent separate physical devices or operators.
>
> **Next step:** Review the original provider record and nearby authentication events.

## Product pillars
- **Understand:** Translate technical account events into clear language.
- **Organize:** Maintain source-linked timelines and identity relationships.
- **Evaluate:** Separate observed facts from hypotheses and unresolved questions.
- **Control:** Design for consent, privacy, and user-managed data.
- **Act:** Offer proportionate, evidence-aware next steps.

## Try the working synthetic prototype

```bash
python -m unittest discover -s prototype -v
python prototype/identity_fairy.py prototype/before.json prototype/after.json
```

The local demonstration compares two fictional snapshots and explains a changed recovery method and a newly observed session, with source references and explicit uncertainty. It does **not** detect account compromise or identify an operator.

- [Research-to-requirements mapping](docs/research-to-requirements.md)
- [MVP requirements and acceptance criteria](docs/product-requirements-mvp.md)
- [Employer-facing skills demonstration](docs/employer-skills.md)

## What is feasible now?
The first working demonstration is a **local-first, synthetic-data snapshot comparator**, not live monitoring. It will model identity relationships, compare historical snapshots, preserve provenance, and show accessible explanations. Provider integrations, optional hardware, and production security require separate validation.

- [MVP feasibility and scope](docs/feasibility-and-mvp.md)
- [Evidence-linked identity graph specification](docs/identity-graph-spec.md)
- [Employer-facing case study](docs/employer-case-study.md)
- [Hardware feasibility research — i-Buddy precedents and verification gaps](docs/hardware-feasibility.md)

## Explore
- [Product vision](docs/product-vision.md)
- [Development roadmap](docs/roadmap.md)
- [Proposed architecture](docs/architecture.md)
- [Privacy and evidence principles](docs/privacy-and-evidence.md)

## Three development milestones

1. **Make the Fairy visible** — tablet/desktop dashboard, original five-colour ambient status, explicit offline state, and fictional interactive scenarios. [Issues #1–3](https://github.com/burdrhi-prog/identity-fairy/issues?q=is%3Aissue+is%3Aopen+M1).
2. **Make the Fairy useful** — evidence-linked account history, recognition/dispute workflow, and privacy-first preservation. [Issues #4–6](https://github.com/burdrhi-prog/identity-fairy/issues?q=is%3Aissue+is%3Aopen+M2).
3. **Bring the Fairy into the physical world** — optional status-only monitor companion, simulator, and proposed ESP32-S3 hardware. [Issues #7–9](https://github.com/burdrhi-prog/identity-fairy/issues?q=is%3Aissue+is%3Aopen+M3).

The physical companion is **not built**; the dashboard is **planned**. The current executable component is a synthetic Python snapshot comparator. [Detailed roadmap](docs/roadmap.md).

## Proposed build stages
1. Synthetic data and a typed snapshot schema — initial implementation complete.
2. Local snapshot comparison and explanation prototype — initial implementation complete; visual timeline remains planned.
3. Plain-language explanation interface.
4. Automated tests and usability review.
5. Security/privacy assessment before real-user data.

## Career relevance
This independent product-design project demonstrates requirements analysis, security-aware UX, identity-data modeling, privacy considerations, and technical product planning. A limited synthetic implementation exists; usability testing, production security, and real-world monitoring remain future milestones.

**No real account data, private investigation files, or credentials are published in this repository.**

## Ambient companion hardware concept

Identity Fairy Home also proposes a **compact, removable monitor companion with softly glowing lights and optional flapping wings**. Original Fairy and Desktop Dude characters would share a status-only hardware platform. The physical design is inspired by the *interaction concept* of historical USB desktop companions, not their branding or appearance. This is not yet built. See [hardware design brief](docs/ambient-companion-hardware.md) and [milestone 3](docs/roadmap.md).
