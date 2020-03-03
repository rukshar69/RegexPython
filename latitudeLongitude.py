import re

reg = '\([\+-]?(90(\.0+)?|[1-8]\d(\.[0-9]+)?|\d(\.[0-9]+)?), [\+-]?(180(\.0+)?|1[0-7]\d(\.[0-9]+)?|[1-9]\d(\.[0-9]+)?|\d(\.[0-9]+)?)\)'
pattern = re.compile(reg)



n = input()
n = int(n)
for i in range(n):
    s = input()
    x = pattern.search(s)
    if x!=None:
        print('Valid')
    else:
        print('Invalid')