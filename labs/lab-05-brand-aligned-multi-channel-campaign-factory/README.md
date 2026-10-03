# Lab 5: Brand-Aligned Multi-Channel Campaign Factory

Course: Agentic AI for Affiliate Marketing (C1319)
Duration: 55 minutes
Alignment: LO3

## Outcome

Use a bounded content Skill to produce website, email, social and video briefs from one approved campaign contract, with disclosure and claim controls.

## Safety boundary

Use only the supplied synthetic records. Keep connectors read-only unless the trainer explicitly authorises a training write. Do not place credentials, personal data, unpublished rates or customer records in prompts or evidence. Publishing, partner messages, spend, payout and optimisation remain human decisions.

## Files

- `README.md`
- `CHECKLIST.md`
- `campaign-brief.json`
- `approved-claims.json`
- `skills/campaign-factory/SKILL.md`
- `compliance_check.py`
- `evidence/`

## Detailed procedure

1. Open campaign-brief.json and verify objective, audience, offer, partner, source IDs, prohibited claims and CTA.
2. Validate the brief with `python3 compliance_check.py campaign-brief.json`.
3. Review approved-claims.json and remove any claim that lacks current evidence.
4. Inspect the campaign-factory Skill output schema for website review, email, social post and video brief.
5. Invoke the Skill in Claude Cowork using only the approved brief and claims files.
6. Confirm every channel artifact keeps the same offer version and core claim.
7. Check that each artifact adapts format and context rather than copying identical text.
8. Verify the affiliate disclosure appears before or with the endorsement.
9. Check each CTA uses the assigned partner and campaign tracking fields.
10. Run the compliance checker against the generated evidence folder.
11. Resolve missing disclosure, unsupported claim, broken link and prohibited-word findings.
12. Record the human reviewer and SHA-256 hash for every approved artifact.
13. Confirm no channel has been published or scheduled from the lab.
14. Complete CHECKLIST.md.

## Acceptance criteria

- [ ] brief passes schema
- [ ] four channel artifacts created
- [ ] claims trace to sources
- [ ] disclosure passes
- [ ] human approval hashes recorded

## Evidence to submit

- campaign-brief.json
- four channel drafts
- compliance-report.json
- resolved findings
- human approval hashes

## Failure handling

- channel draft cannot alter offer terms
- missing disclosure blocks release
- unsupported superlative is flagged
- brand and legal issues are separate
- no draft publishes automatically
