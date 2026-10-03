from pathlib import Path
import csv, json
BASE=Path(__file__).resolve().parent
def rows(name):
    with (BASE/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def save(name,obj):
    (BASE/'evidence').mkdir(exist_ok=True); (BASE/'evidence'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
data=rows('partner-candidates.csv'); out=[]
for r in data:
    fit,identity,quality,risk=map(float,(r['audience_fit'],r['identity_evidence'],r['engagement_quality'],r['policy_risk']))
    score=.4*fit+.25*identity+.25*quality+.1*(100-risk); decision='review' if identity>=80 and risk<=30 else 'hold'
    out.append({**r,'weighted_score':round(score,1),'decision':decision,'connector_scope':'read-only'})
save('due-diligence-report.json',out); print('PASS',sum(x['decision']=='review' for x in out),'review candidates')
