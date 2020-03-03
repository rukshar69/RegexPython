import re

n = input()
n = int(n)
begin = '^hackerrank'
end = 'hackerrank$'
both = '^hackerrank$'
for i in range(n):
    s = input()
    both_x = re.search(both,s)
    if both_x != None:
        print('0')
    else:
        begin_x = re.search(begin,s)
        if begin_x != None:
            print('1')
        else:
            end_x = re.search(end,s)
            if end_x != None:
                print('2')
            else: print('-1')