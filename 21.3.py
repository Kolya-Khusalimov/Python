import re

PATTERN = r"\b(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b"

PATT_COMP = re.compile(PATTERN, flags = 0)

def reading():
    f = open("Numbers.txt", 'r')
    t = f.read()
    list = []
    for number in re.finditer(PATT_COMP,t):
        if number.group() != "":
           list.append(number.group())
    f.close()
    return print(list)


if __name__ == '__main__':
    reading()