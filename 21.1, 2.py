#21.1
import re


DATE1 = r"\d{1,4}/\d{1,2}/\d{1,2}"
DATE2 = r"\d{1,2}\.\d{1,2}\.\d{1,4}"
DATE = DATE1 +"|"+DATE2
print(DATE)

def _change_date(match):
    print(match)
    date = match.group()
    if "/" in date:
        y, m, d = date.split("/")
    else:
        d, m, y = date.split(".")
    while len(y) != 4:
        y = "0" + y
    if len(m) != 2:
        m = "0" + m
    if len(d) != 2:
        d = "0" + d
    date = ".".join((d, m, y))
    return date

def change_dates(string):
    return re.sub(DATE, _change_date,string)

if __name__ == '__main__':
    with open("21.1_check.txt", "r") as inp:
        s = inp.read()
        s = change_dates(s)
    with open("output.txt", "w") as out:
        out.write(s)

#21.2
s  = input("Input text ")
PATTERN = "[a - z, A - Z] +"
rr = re.compile(PATTERN)
res = rr.findall(s)
print(res)

def printWords(fname, pattern):
    rgx = re.compile(pattern)
    with open(fname, 'r') as f:
        rows = f.readlines()
        for row in rows:
           for word in rgx.finditer(row):
               print(word, end = ' ')

SENTENCE = "[a - z, A - Z,\s, \.,\,] * [\.?!\b]"

SENTENCE = r"[A - ZA - ЯІЇЄ].*?[\.\!\?](?)"

if __name__ == "__main__":
    fn = "3.txt"
    rexp = SENTENCE
    printWords(fn, rexp)
