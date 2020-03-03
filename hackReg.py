import re

reg = '[hH][aA][cC][kK][eE][rR][rR][aA][nN][kK]'



n = input()
n = int(n)
count =0
for i in range(n):
    s = input()
    x = re.findall(reg,s)
    if(len(x)>0) :count+=1


print(count)