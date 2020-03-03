# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

expression = 'href="/questions/(\d+)/.+?>(.+?)</a>.+?class="relativetime">(.+?)</span>'
regex = re.compile(expression, re.DOTALL)
questions = sys.stdin.read()

result = regex.findall(questions)
for line in result:
    #print(*line, sep=';')
    #print(line)
    s = ''
    for l in line:
        s += l +';'
    print(s[:-1])