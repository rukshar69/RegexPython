import re


n = input()
n = int(n)
s = []

for i in range(n):
    line  = input()
    #s.append(line)
    x = re.findall("<\\b(\\w+)\\b.*?>", line)
    for a in x:
        s.append(a)

st = set(s)
st = list(st)
st.sort()
s = ''
for a in st:
    s+=a
    s += ';'
print(s[:-1])
#print(s)

