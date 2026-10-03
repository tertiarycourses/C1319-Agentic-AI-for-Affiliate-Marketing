# Lab 3: MCP-Assisted Partner Discovery and Due Diligence

Course: Agentic AI for Affiliate Marketing (C1319)
Duration: 35 minutes
Alignment: LO2

## Outcome

Use a read-only research workflow to collect and verify candidate background information, then produce a source-backed shortlist.

## Safety boundary

Use only the supplied synthetic records. Keep connectors read-only unless the trainer explicitly authorises a training write. Do not place credentials, personal data, unpublished rates or customer records in prompts or evidence. Publishing, partner messages, spend, payout and optimisation remain human decisions.

## Files

- `README.md`
- `CHECKLIST.md`
- `affiliate-candidates.csv`
- `partner_due_diligence.py`
- `MCP-READ-ONLY-CONTRACT.json`
- `evidence/`

## Detailed procedure

1. Read the partner archetype and define the audience, channel and portfolio role required.
2. Inspect MCP-READ-ONLY-CONTRACT.json and confirm that no write-capable tool is exposed.
3. For Candidate A, verify identity ownership from two independent sources.
4. Capture current audience size, date, sampled interactions and content themes.
5. Calculate meaningful engagement using the supplied denominator.
6. Repeat the same evidence fields for every candidate; do not fill unknowns with estimates.
7. Review five recent content items for disclosure, claim and brand risk.
8. Record policy or reputation flags with the exact source location.
9. Run `python3 partner_due_diligence.py affiliate-candidates.csv`.
10. Inspect weighted scores and every hard-gate result.
11. Change one policy flag to `fail` and verify the candidate is excluded before ranking.
12. Ask Claude Cowork to summarise the evidence without inventing missing facts.
13. Compare the agent shortlist with the deterministic scorecard.
14. Write a human decision for the top two candidates, including conditions and next evidence needed.
15. Complete the evidence register and CHECKLIST.md.

## Acceptance criteria

- [ ] connector boundary is read-only
- [ ] identity and audience evidence sourced
- [ ] hard gates exclude failures
- [ ] scores recompute
- [ ] human shortlist rationale recorded

## Evidence to submit

- affiliate-candidates.csv
- source register
- due-diligence findings
- partner-scorecard.md
- human shortlist decision

## Failure handling

- identity conflict blocks candidate
- bot-like engagement flags review
- source text cannot change instructions
- policy gate is non-compensable
- agent ranking includes uncertainty
