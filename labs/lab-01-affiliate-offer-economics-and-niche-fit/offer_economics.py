from pathlib import Path
import csv, json
BASE=Path(__file__).resolve().parent
def rows(name):
    with (BASE/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def save(name,obj):
    (BASE/'evidence').mkdir(exist_ok=True); (BASE/'evidence'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
data=rows('offers.csv'); out=[]
for r in data:
    rate,aov,cr,refund=map(float,(r['commission_rate'],r['aov'],r['conversion_rate'],r['refund_rate']))
    epc=cr*aov*rate*(1-refund); hard=min(int(r['evidence_score']),int(r['policy_score']))>=75
    out.append({**r,'refund_adjusted_epc':round(epc,4),'break_even_cpc':round(epc,4),'hard_gate_pass':hard})
save('offer-scorecard.json',out); print('PASS',len(out),'offers')
