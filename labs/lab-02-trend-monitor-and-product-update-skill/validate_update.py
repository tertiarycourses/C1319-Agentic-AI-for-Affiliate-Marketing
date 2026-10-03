from pathlib import Path
import csv, json
BASE=Path(__file__).resolve().parent
def rows(name):
    with (BASE/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def save(name,obj):
    (BASE/'evidence').mkdir(exist_ok=True); (BASE/'evidence'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
signals=rows('trend-signals.csv'); product=json.loads((BASE/'product-record.json').read_text())
accepted=[s for s in signals if s['confidence'] in {'medium','high'} and s['source_url'].startswith('https://')]
save('validated-update.json',{'product_id':product['product_id'],'effective_at':product['effective_at'],'accepted_signal_ids':[s['signal_id'] for s in accepted],'approved_claims':product['approved_claims'],'requires_human_release':True}); print('PASS',len(accepted),'traceable signals')
