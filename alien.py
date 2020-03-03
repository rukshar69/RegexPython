
import re


n = input()
n = int(n)

reg = '^[_.]\d+[a-zA-Z]*_?$'
for i in range(n):
    s = input()
    x = re.search(reg, s)
    if x != None: print('VALID')
    else: print('INVALID')