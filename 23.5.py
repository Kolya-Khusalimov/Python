from docx import Document
import re

DATE1 = r"\b(?P<d1>\d{1,2})\.(?P<m1>\d{1,2})\.(?P<y1>\d{1,4})"
DATE2 = r"\b(?P<y2>\d{1,4})\-(?P<m2>\d{1,2})\-(?P<d2>\d{1,2})"
DATE3 = r"\b(?P<y3>\d{1,4})/(?P<m3>\d{1,2})/(?P<d3>\d{1,2})"
DATE = DATE1 + "|" + DATE2 + "|" + DATE3


def change_dates(text, n):

    def _change_date(match):
        if "." in match.group():
            k = "1"
        elif "-" in match.group():
            k = "2"
        else:
            k = "3"

        d = match.group("d" + k)
        m = match.group("m" + k)
        y = match.group("y" + k)

        while len(y) != 4:
            y = "0" + y
        if len(m) != 2:
            m = "0" + m
        if len(d) != 2:
            d = "0" + d

        if n == 1:
            date = ".".join((d, m, y))
        elif n == 2:
            date = "-".join((y, m, d))
        else:
            date = "/".join((y, m, d))
        return date

    return re.sub(DATE, _change_date, string)


def change_dates_docx(inp, out, n):
    doc = Document(inp)

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.text = change_dates(run.text, n)

    doc.save(out)


if name == "main":
    change_dates_docx("input.docx", "output.docx", 1)