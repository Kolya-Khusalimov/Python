import re
ip_adress = r"<\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}>"
adress = r"<http://.+>"
date_time = r"<\d{1,2}\.\d{1,2}\.\d{1,4} \d{1,2}:\d{1,2}:\d{1,2}>"
txt = ip_adress + adress + date_time
re.compile(txt, flags = 0)


def searching():
    f = open("adress.txt", 'r')
    t = f.read()
    s = []
    for a_d_t in re.finditer(txt, t):
        s.append(a_d_t.group())
    f.close()
    return print(s)


if __name__ == '__main__':
    searching()
