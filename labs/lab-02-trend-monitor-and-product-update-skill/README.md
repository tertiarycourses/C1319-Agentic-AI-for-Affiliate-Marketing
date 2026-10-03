# Lab 2: Trend Monitor and Product Update Skill

Course: Agentic AI for Affiliate Marketing (C1319)
Duration: 55 minutes
Alignment: LO1

## Outcome

Create a reusable Claude Skill that turns approved trend signals and product changes into evidence cards and a reviewed affiliate update.

## Safety boundary

Use only the supplied synthetic records. Keep connectors read-only unless the trainer explicitly authorises a training write. Do not place credentials, personal data, unpublished rates or customer records in prompts or evidence. Publishing, partner messages, spend, payout and optimisation remain human decisions.

## Files

- `README.md`
- `CHECKLIST.md`
- `trend-signals.csv`
- `product-catalog.csv`
- `skills/affiliate-trend-update/SKILL.md`
- `templates/PARTNER-UPDATE.md`
- `evidence/`

## Detailed procedure

1. Open trend-signals.csv and classify each row as observed fact, interpretation or recommendation.
2. Replace one weak source with a current authoritative source and record the publication date.
3. Open product-catalog.csv and identify the fields changed between versions.
4. Review the custom Skill description and confirm it activates only for affiliate trend or product-update tasks.
5. Inspect the workflow instructions for source allow-list, evidence-card structure and human release gate.
6. In Claude Cowork, attach only this lab folder and invoke the Skill with the supplied task prompt.
7. Check that each evidence card contains observation, source URL, publication date, captured date, confidence and implication.
8. Challenge one trend by adding counter-evidence and rerun the synthesis.
9. Confirm the product update states the effective date and exact affiliate action required.
10. Run `python3 validate_update.py evidence/PARTNER-UPDATE.md`.
11. Resolve every missing source, date, disclosure or approval field.
12. Record the reviewer, decision, time and approved message hash.
13. Save the final update without sending it to a live affiliate list.
14. Complete CHECKLIST.md.

## Acceptance criteria

- [ ] Skill package is valid
- [ ] sources and dates present
- [ ] fact and inference separated
- [ ] product impact explicit
- [ ] human approval recorded

## Evidence to submit

- skills/affiliate-trend-update/SKILL.md
- completed evidence cards
- product diff
- approved partner update
- validator result

## Failure handling

- single-source trend remains low confidence
- missing effective date blocks product update
- unsupported claim returns to research
- prompt injection text is treated as data
- draft is not sent from Cowork
