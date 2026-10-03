# Lab 4: Affiliate Portfolio and Communication Agent

Course: Agentic AI for Affiliate Marketing (C1319)
Duration: 35 minutes
Alignment: LO2

## Outcome

Construct a role-balanced portfolio and a controlled communication cadence that keeps partner briefs, product updates and escalations traceable.

## Safety boundary

Use only the supplied synthetic records. Keep connectors read-only unless the trainer explicitly authorises a training write. Do not place credentials, personal data, unpublished rates or customer records in prompts or evidence. Publishing, partner messages, spend, payout and optimisation remain human decisions.

## Files

- `README.md`
- `CHECKLIST.md`
- `portfolio.csv`
- `portfolio_analysis.py`
- `communication-cadence.csv`
- `skills/partner-coordinator/SKILL.md`
- `templates/PARTNER-BRIEF.md`
- `evidence/`

## Detailed procedure

1. Open portfolio.csv and assign each partner one primary strategic role.
2. Run `python3 portfolio_analysis.py portfolio.csv`.
3. Confirm current role shares total 100% and note the top-three revenue concentration.
4. Identify one role gap and one duplicated audience cluster.
5. Propose a rebalance that respects partner capacity and existing commitments.
6. Assign strategic, growth or standard service tiers using transparent criteria.
7. Open communication-cadence.csv and set a routine cadence, response target and escalation owner for each tier.
8. Review the partner-coordinator Skill and confirm it cannot alter commission terms.
9. Invoke the Skill with the approved product update from Lab 2 and one shortlisted partner from Lab 3.
10. Check the generated brief for campaign ID, partner ID, product version, approved claims, prohibited claims and tracked URL.
11. Create an acknowledgement event and next action.
12. Simulate an SLA breach and verify the named escalation route.
13. Record the human approval decision and brief hash.
14. Complete CHECKLIST.md.

## Acceptance criteria

- [ ] portfolio shares reconcile
- [ ] concentration reported
- [ ] role gap identified
- [ ] brief versioned and approved
- [ ] SLA escalation works

## Evidence to submit

- portfolio.csv
- portfolio-analysis.md
- communication-cadence.csv
- approved partner brief
- message and escalation log

## Failure handling

- duplicate audience creates hidden concentration
- old brief version is blocked
- SLA miss triggers named escalation
- agent cannot change commercial terms
- unacknowledged update stays open
