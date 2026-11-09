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

## Explore
- [Product vision](docs/product-vision.md)
- [Development roadmap](docs/roadmap.md)
- [Proposed architecture](docs/architecture.md)
- [Privacy and evidence principles](docs/privacy-and-evidence.md)

## Proposed build stages
1. Synthetic data and a typed snapshot schema — initial implementation complete.
2. Local snapshot comparison and explanation prototype — initial implementation complete; visual timeline remains planned.
3. Plain-language explanation interface.
4. Automated tests and usability review.
5. Security/privacy assessment before real-user data.

## Career relevance
This independent product-design project demonstrates requirements analysis, security-aware UX, identity-data modeling, privacy considerations, and technical product planning. A limited synthetic implementation exists; usability testing, production security, and real-world monitoring remain future milestones.

**No real account data, private investigation files, or credentials are published in this repository.**
