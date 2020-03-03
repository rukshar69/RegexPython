import re

n = input()
n = int(n)


#print(s)

regex = '^(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})$'
for i in range(n):
    st = input()
    x = re.findall(regex,st)
    tup = x[0]
    c = tup[0]
    local = tup[1]
    number = tup[2]
    print('CountryCode='+c+',LocalAreaCode='+local+',Number='+number)    