"""Paragraph-TOC renumber: locate each entry in reading order in the rendered PDF, write the page, re-export until stable."""
import subprocess, sys
from docx import Document
sys.path.insert(0, 'build'); from docxutil import set_para
for f in sys.argv[1:]:
    docx = f"courseware/{f}-Agentic AI for Affiliate Marketing.docx"; pdf = docx[:-5] + ".pdf"
    for it in range(3):
        subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', docx, '--outdir', 'courseware'], capture_output=True)
        pages = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout.split('\f')
        d = Document(docx); changed = 0; cur = 3
        for pp in d.paragraphs:
            if '\t' not in pp.text: continue
            title, old = pp.text.split('\t')
            key = ' '.join(title.split()[:5])
            pg = next(i + 1 for i in range(cur, len(pages)) if any(' '.join(l.split()).startswith(key) for l in pages[i].splitlines()))
            cur = pg - 1
            if str(pg) != old: set_para(pp, f"{title}\t{pg}"); changed += 1
        print(f, 'pass', it, 'changed', changed)
        if not changed: break
        d.save(docx)
