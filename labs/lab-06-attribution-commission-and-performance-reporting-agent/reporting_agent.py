from pathlib import Path
import csv, json
BASE=Path(__file__).resolve().parent
def rows(name):
    with (BASE/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def save(name,obj):
    (BASE/'evidence').mkdir(exist_ok=True); (BASE/'evidence'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
clicks=rows('click-events.csv'); conv=rows('conversion-events.csv'); stmt=rows('commission-statement.csv')
ids=[r['click_id'] for r in clicks]; dup=sorted({x for x in ids if ids.count(x)>1}); valid=set(ids)
unmatched=[r['order_id'] for r in conv if r['click_id'] not in valid]; approved=[r for r in conv if r['status']=='approved' and r['click_id'] in valid]
revenue=sum(float(r['revenue']) for r in approved); commission=sum(float(r['commission']) for r in stmt); unique=len(set(ids)); epc=commission/unique if unique else 0
save('reconciliation-report.json',{'period':'2026-09-12','unique_clicks':unique,'approved_orders':len(approved),'approved_revenue':round(revenue,2),'statement_commission':round(commission,2),'epc':round(epc,2),'duplicate_click_ids':dup,'unmatched_orders':unmatched,'observation':'Two valid approved orders generated attributable revenue.','inference':'The sample is too small for a channel winner.','recommendation':'Run a two-week creative test with unsubscribe and reversal guardrails.','requires_human_approval':True}); print('PASS report generated; exceptions',len(dup)+len(unmatched))
