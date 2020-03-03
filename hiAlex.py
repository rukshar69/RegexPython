import re

n = input()
n = int(n)
regex = '^[Hh][Ii] [^Dd]'
for i in range(n):
    s = input()
    x = re.search(regex,s)
    if x:
        print(x.string)
    