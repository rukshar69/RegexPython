import re

n = input()
n = int(n)
regex = '^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'
for i in range(n):
    s = input()
    x = re.search(regex,s)
    if x!=None:
        print('VALID')
    else: print('INVALID')