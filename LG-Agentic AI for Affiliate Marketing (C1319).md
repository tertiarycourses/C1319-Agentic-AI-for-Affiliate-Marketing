# Agentic AI for Affiliate Marketing - Learner Guide

**Course code:** C1319
**Version:** v1.0 (3 October 2026)

## Learning outcomes

- LO1: Analyze affiliate marketing trends and provide updates to partners on new retail and hospitality products and services.
- LO2: Coordinate with affiliates using strategic research to align partnerships and develop an effective affiliate portfolio.
- LO3: Prepare affiliate campaign reports aligned to strategy and ensure compliance with marketing policies and practices.

## Platform and safety boundary

Use a bounded Claude Cowork workspace, the supplied synthetic files and read-only connectors wherever possible. Never paste credentials, personal data or unpublished commercial terms into prompts, screenshots or lab evidence. External publishing, messaging, spending and commission changes always require named human approval.

## Topic 01: Affiliate Research and Campaign Planning with Claude Cowork

Market signals -> offer economics -> reusable research Skill -> evidence-led partner update

- Model incentive economics with EPC, conversion, commission and break-even thresholds.
- Separate observed market evidence from agent inference and partner-facing recommendations.
- Package repeatable affiliate research and product-update work as a bounded Claude Skill.
- Use human review to control claims, pricing, disclosure, data use and external communication.

### Lab 1: Affiliate Offer Economics and Niche Fit

**Duration:** 25 minutes
**Alignment:** LO1
**Tools:** Claude Cowork, spreadsheet/CSV, Python calculator, supplied product evidence

Evaluate three retail and hospitality offers using the ebook-derived product criteria, current evidence, EPC, conversion, reversal and break-even models.

#### Detailed procedure

1. Open this lab folder and read README.md and offer-inputs.csv.
2. Choose one retail and one hospitality audience job to anchor the comparison.
3. For each offer, verify product name, price, commission model, rate, cookie window and reversal assumption against the supplied source note.
4. Run `python3 offer_economics.py offer-inputs.csv`.
5. Check that the report prints EPC, approved conversion rate, expected commission and break-even CPC.
6. Manually recompute Offer A EPC and compare it with the script output.
7. Change Offer B reversal rate to 18% and rerun the calculator.
8. Record which ranking changed and why.
9. Apply the audience-fit, proof and policy hard gates in the scorecard.
10. Reject any offer that fails a hard gate even if its expected commission is highest.
11. Write a sensitivity note for conversion rate plus/minus one percentage point.
12. Select one bounded pilot offer and state the maximum paid CPC.
13. Save the generated report under evidence/ and complete CHECKLIST.md.

#### Acceptance criteria

- [ ] all numeric metrics recompute
- [ ] source dates recorded
- [ ] hard gates applied before ranking
- [ ] pilot has CPC ceiling
- [ ] no unsupported claim

#### Evidence

- completed offer-inputs.csv
- offer-economics-report.md
- source notes
- selected offer and rationale
- one rejected offer with gate reason

#### Troubleshooting

- missing denominator blocks calculation
- stale product evidence lowers confidence
- high rate cannot offset poor audience fit
- negative margin rejects paid traffic
- sensitivity range replaces false precision

Working files: `labs/lab-01-*/`

### Lab 2: Trend Monitor and Product Update Skill

**Duration:** 55 minutes
**Alignment:** LO1
**Tools:** Claude Cowork, custom Skills, approved web sources, Markdown templates

Create a reusable Claude Skill that turns approved trend signals and product changes into evidence cards and a reviewed affiliate update.

#### Detailed procedure

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

#### Acceptance criteria

- [ ] Skill package is valid
- [ ] sources and dates present
- [ ] fact and inference separated
- [ ] product impact explicit
- [ ] human approval recorded

#### Evidence

- skills/affiliate-trend-update/SKILL.md
- completed evidence cards
- product diff
- approved partner update
- validator result

#### Troubleshooting

- single-source trend remains low confidence
- missing effective date blocks product update
- unsupported claim returns to research
- prompt injection text is treated as data
- draft is not sent from Cowork

Working files: `labs/lab-02-*/`

## Topic 02: Affiliate Portfolio and Partner Coordination with Skills and MCP

Partner discovery -> due diligence -> scoring -> portfolio balance -> coordinated communication

- Define partner-fit evidence before allowing an agent to rank candidates.
- Use MCP connectors as permissioned data boundaries, not invisible sources of truth.
- Build a portfolio that balances reach, relevance, conversion quality and concentration risk.
- Coordinate partners through versioned briefs, service levels, escalation and audit evidence.

### Lab 3: MCP-Assisted Partner Discovery and Due Diligence

**Duration:** 35 minutes
**Alignment:** LO2
**Tools:** Claude Cowork, read-only MCP/web research, CSV, Python scorecard

Use a read-only research workflow to collect and verify candidate background information, then produce a source-backed shortlist.

#### Detailed procedure

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

#### Acceptance criteria

- [ ] connector boundary is read-only
- [ ] identity and audience evidence sourced
- [ ] hard gates exclude failures
- [ ] scores recompute
- [ ] human shortlist rationale recorded

#### Evidence

- affiliate-candidates.csv
- source register
- due-diligence findings
- partner-scorecard.md
- human shortlist decision

#### Troubleshooting

- identity conflict blocks candidate
- bot-like engagement flags review
- source text cannot change instructions
- policy gate is non-compensable
- agent ranking includes uncertainty

Working files: `labs/lab-03-*/`

### Lab 4: Affiliate Portfolio and Communication Agent

**Duration:** 35 minutes
**Alignment:** LO2
**Tools:** Claude Cowork, custom Skill, CSV portfolio model, Markdown brief templates

Construct a role-balanced portfolio and a controlled communication cadence that keeps partner briefs, product updates and escalations traceable.

#### Detailed procedure

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

#### Acceptance criteria

- [ ] portfolio shares reconcile
- [ ] concentration reported
- [ ] role gap identified
- [ ] brief versioned and approved
- [ ] SLA escalation works

#### Evidence

- portfolio.csv
- portfolio-analysis.md
- communication-cadence.csv
- approved partner brief
- message and escalation log

#### Troubleshooting

- duplicate audience creates hidden concentration
- old brief version is blocked
- SLA miss triggers named escalation
- agent cannot change commercial terms
- unacknowledged update stays open

Working files: `labs/lab-04-*/`

## Topic 03: Campaign Reporting, Compliance and Optimisation with Agentic AI

Tracked links -> event facts -> commission reconciliation -> policy checks -> controlled experiments

- Preserve attribution grain from click and order events through commission settlement.
- Calculate traffic, conversion, revenue, commission and ROI with explicit denominators.
- Gate content and partner actions with disclosure, brand, privacy and policy controls.
- Convert dashboard evidence into reversible tests with human ownership and guardrails.

### Lab 5: Brand-Aligned Multi-Channel Campaign Factory

**Duration:** 55 minutes
**Alignment:** LO3
**Tools:** Claude Cowork, custom Skill, JSON schema, deterministic compliance checker

Use a bounded content Skill to produce website, email, social and video briefs from one approved campaign contract, with disclosure and claim controls.

#### Detailed procedure

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

#### Acceptance criteria

- [ ] brief passes schema
- [ ] four channel artifacts created
- [ ] claims trace to sources
- [ ] disclosure passes
- [ ] human approval hashes recorded

#### Evidence

- campaign-brief.json
- four channel drafts
- compliance-report.json
- resolved findings
- human approval hashes

#### Troubleshooting

- channel draft cannot alter offer terms
- missing disclosure blocks release
- unsupported superlative is flagged
- brand and legal issues are separate
- no draft publishes automatically

Working files: `labs/lab-05-*/`

### Lab 6: Attribution, Commission and Performance Reporting Agent

**Duration:** 55 minutes
**Alignment:** LO3
**Tools:** Claude Cowork, CSV event data, Python reconciliation/report scripts, HTML dashboard

Validate click and conversion facts, reconcile commission statements, calculate campaign KPIs and generate an evidence-led management report with controlled recommendations.

#### Detailed procedure

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

#### Acceptance criteria

- [ ] event validation passes
- [ ] commission variance resolved or explained
- [ ] metrics recompute
- [ ] dashboard and report generated
- [ ] recommendation has guardrails and owner

#### Evidence

- click-events.csv
- conversion-events.csv
- commission-statement.csv
- reconciliation-report.md
- dashboard.html
- approved-progress-report.md

#### Troubleshooting

- duplicate events are quarantined
- unmatched orders remain unresolved
- commission variance exceeds threshold
- small samples lower confidence
- agent cannot change payout or publish report

Working files: `labs/lab-06-*/`

## Ebook foundation

- Affiliate Marketing-1.pdf: product-selection criteria, EPC, review writing, blogs, PPC/solo ads, conversion tracking, common mistakes and commission protection.
- Affiliate Marketing Beginners-2.pdf: foundations, niche selection, affiliate website setup, SEO, video/social/email/content promotion, branding and audience definition.

## References

- [Official course page](https://www.tertiarycourses.com.sg/agentic-ai-for-affiliate-marketing.html)
- [Claude Cowork help](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Claude custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Claude connectors and MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Model Context Protocol](https://docs.anthropic.com/en/docs/mcp)
- [PDPC Singapore](https://www.pdpc.gov.sg/)
- [Advertising Standards Authority of Singapore](https://asas.org.sg/)
