# Lab 1: Affiliate Offer Economics and Niche Fit

Course: Agentic AI for Affiliate Marketing (C1319)
Duration: 25 minutes
Alignment: LO1

## Outcome

Evaluate three retail and hospitality offers using the ebook-derived product criteria, current evidence, EPC, conversion, reversal and break-even models.

## Safety boundary

Use only the supplied synthetic records. Keep connectors read-only unless the trainer explicitly authorises a training write. Do not place credentials, personal data, unpublished rates or customer records in prompts or evidence. Publishing, partner messages, spend, payout and optimisation remain human decisions.

## Files

- `README.md`
- `CHECKLIST.md`
- `offer-inputs.csv`
- `offer_economics.py`
- `evidence/SOURCE-NOTES.md`

## Detailed procedure

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

## Acceptance criteria

- [ ] all numeric metrics recompute
- [ ] source dates recorded
- [ ] hard gates applied before ranking
- [ ] pilot has CPC ceiling
- [ ] no unsupported claim

## Evidence to submit

- completed offer-inputs.csv
- offer-economics-report.md
- source notes
- selected offer and rationale
- one rejected offer with gate reason

## Failure handling

- missing denominator blocks calculation
- stale product evidence lowers confidence
- high rate cannot offset poor audience fit
- negative margin rejects paid traffic
- sensitivity range replaces false precision
