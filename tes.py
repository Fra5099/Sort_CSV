from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.colors import Color
import csv
from googletrans import Translator, constants

styles = getSampleStyleSheet()

def translatet(word):
    tra = Translator()
    tt = tra.translate(word)
    return tt.text

def make_report():
    doc = SimpleDocTemplate("hello.pdf")
    story = []
    style = styles["Normal"]
    hh = ParagraphStyle('title', fontSize=16, leading=24)
    ps = ParagraphStyle('title', fontSize=14, leading=24)
    link = ParagraphStyle('title', fontSize=12, leading=24, textColor=colors.blue)
    filec = open('output_file.csv', encoding="utf-8-sig")
    reader = csv.reader(filec)
    reader.__next__
    dup=""
    for row in reader:
        if dup==row[2]:
            pass
        else:
            p1 = translatet(row[0])
            h1 = " <b>"+translatet(row[1])+"</b>"
            url = row[2]
            dup=url
            url = url[4:]
            l1 = '<link href="' + url + '">Source</link>' 
            datap = []
            datah = []
            datal = []
            p = [Paragraph(p1, ps)]

            h = [Paragraph(h1, hh)]

            l = [Paragraph(l1, link)]

            datap.append(p)
            datah.append(h)
            datal.append(l)
            p1 = Table(datap)
            h1 = Table(datah)
            l1 = Table(datal)
            tst = TableStyle([\
                    ('GRID', (0,0), (-1,-1), 0.25, colors.black, None, (2,2,1)),\
                    ])
            p1.setStyle(tst)
            h1.setStyle(tst)
            l1.setStyle(tst)
            story.append(h1)
            story.append(p1)
            story.append(l1)
            story.append(Spacer(1,0.2*inch))
    doc.build(story)

if __name__ == "__main__":
    make_report()


