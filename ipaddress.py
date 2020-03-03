import re


n = input()
n = int(n)

ip4Reg = '^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'

ip6Reg = '^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$'

for i in range(n):
    s = input()
    x4 = re.search(ip4Reg, s)
    x6 = re.search(ip6Reg,s)
    if x4 != None:
        print('IPv4')
    elif x6 != None:
        print('IPv6')
    else: print('Neither')