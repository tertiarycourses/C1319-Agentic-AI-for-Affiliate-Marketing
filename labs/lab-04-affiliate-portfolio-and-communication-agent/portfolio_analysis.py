from pathlib import Path
import csv, json
BASE=Path(__file__).resolve().parent
def rows(name):
    with (BASE/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def save(name,obj):
    (BASE/'evidence').mkdir(exist_ok=True); (BASE/'evidence'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
data=rows('portfolio-input.csv'); clicks=sum(int(r['forecast_clicks']) for r in data); out=[]
for r in data:
    share=int(r['forecast_clicks'])/clicks; out.append({**r,'traffic_share':round(share,4),'concentration_flag':share>.40,'communication_status':'draft_review'})
save('portfolio-plan.json',out); print('PASS',len(out),'partners','max_share',max(x['traffic_share'] for x in out))
