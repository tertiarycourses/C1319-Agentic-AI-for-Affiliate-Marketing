from pathlib import Path
import csv, json
BASE=Path(__file__).resolve().parent
def rows(name):
    with (BASE/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def save(name,obj):
    (BASE/'evidence').mkdir(exist_ok=True); (BASE/'evidence'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
brief=json.loads((BASE/'approved-brief.json').read_text()); data=rows('content-drafts.csv'); out=[]
for r in data:
    errors=[]
    if r['claim'] not in brief['approved_claims']: errors.append('unapproved_claim')
    if not r['disclosure'].strip(): errors.append('missing_disclosure')
    if r['cta_url']!=brief['cta_url']: errors.append('wrong_cta')
    out.append({**r,'status':'release_candidate' if not errors else 'blocked','errors':errors})
save('compliance-report.json',out); print('PASS',sum(x['status']=='release_candidate' for x in out),'of',len(out),'assets')
