from pathlib import Path
import re

p = Path('/home/himanshul')
files = list(p.glob('*.txt'))
inp = ["r", "'"]
inpt = input()
inp.append(inpt)
inp.append("'")
inp = "".join(inp)
print(inp)
s = re.compile(inp)


val = None
for i in files:
    val = open(i)
    val = val.readlines()
    val = val[0]
    if s.search(val).group():
        print(s.search(val).group())
    val.close()
