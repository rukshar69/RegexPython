import re


n = input()
n = int(n)

sentences = []
for i in range(n):
    line = input()
    sentences.append(line)


q = input()
q = int(q)

queries = []
for i in range(q):
    line = input()
    queries.append(line)
    qu = line
    reg = '\w+'+qu+'\w+'
    count =0
    for s in sentences:
        x = re.findall(reg, s)
        count += len(x)
    print(count)
