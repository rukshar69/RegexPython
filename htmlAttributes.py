import re
from collections import defaultdict

n = input()
n = int(n)
lines = []
for i in range(n):
    s = input()
    lines.append(s)

htmlFile = ''.join([inp for inp in lines])
regex1 = r'<(\w+)(|\s+[^>]*)>'
regex2 = r'(\w+)=[\'\"]'

parsedStr = re.findall(regex1, htmlFile, re.I)


tag_attributes = defaultdict(list)

for tup in parsedStr:
    tag, attr = tup
    #print('tag ',tag,'attr ',attr)
    tag_attributes[tag].extend(re.findall(regex2, attr))

for tag, attr in sorted(tag_attributes.items()):
    setOfAttr = set(attr)
    sortedAttr = sorted(setOfAttr)
    attrList = ','.join(sortedAttr)
    tagAndAttr = ':'.join([tag, attrList])
    print(tagAndAttr)