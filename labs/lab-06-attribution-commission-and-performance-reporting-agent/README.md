# Lab 6: Attribution, Commission and Performance Reporting Agent

Course: Agentic AI for Affiliate Marketing (C1319)
Duration: 55 minutes
Alignment: LO3

## Outcome

Validate click and conversion facts, reconcile commission statements, calculate campaign KPIs and generate an evidence-led management report with controlled recommendations.

## Safety boundary

Use only the supplied synthetic records. Keep connectors read-only unless the trainer explicitly authorises a training write. Do not place credentials, personal data, unpublished rates or customer records in prompts or evidence. Publishing, partner messages, spend, payout and optimisation remain human decisions.

## Files

- `README.md`
- `CHECKLIST.md`
- `click-events.csv`
- `conversion-events.csv`
- `commission-statement.csv`
- `reporting_agent.py`
- `metric-dictionary.md`
- `evidence/`

## Detailed procedure

1. Open the three CSV files and identify click_id, order_id, partner_id, campaign_id and status fields.
2. Run `python3 reporting_agent.py`.
3. Review the validation section for duplicate clicks, unmatched orders and invalid statuses.
4. Quarantine the supplied duplicate event and rerun the script.
5. Reconcile approved revenue, reversal amount and payable commission with the network statement.
6. Investigate any variance above the stated materiality threshold.
7. Open metric-dictionary.md and manually recompute CTR, approved conversion rate, EPC and ROI for one partner.
8. Confirm every dashboard label states the denominator and reporting period.
9. Segment performance by partner and channel; identify the real bottleneck rather than the largest absolute number.
10. Ask Claude Cowork to explain the variance using only the generated facts and metric dictionary.
11. Require the narrative to separate observation, inference and recommendation.
12. Write one reversible optimisation experiment with primary metric, guardrails, sample/window and stop rule.
13. Review disclosure, privacy and brand implications before approving the recommendation.
14. Generate the final partner progress report with commission and activity sections.
15. Record owners, due dates and human approval, then complete CHECKLIST.md.

## Acceptance criteria

- [ ] event validation passes
- [ ] commission variance resolved or explained
- [ ] metrics recompute
- [ ] dashboard and report generated
- [ ] recommendation has guardrails and owner

## Evidence to submit

- click-events.csv
- conversion-events.csv
- commission-statement.csv
- reconciliation-report.md
- dashboard.html
- approved-progress-report.md

## Failure handling

- duplicate events are quarantined
- unmatched orders remain unresolved
- commission variance exceeds threshold
- small samples lower confidence
- agent cannot change payout or publish report
