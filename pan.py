import re

n = input()
n = int(n)
regex = '^[A-Z]{5}\d{4}[A-Z]$'
for i in range(n):
    s = input()
    x = re.search(regex,s)
    if x!=None:
        print('YES')
    else: print('NO')