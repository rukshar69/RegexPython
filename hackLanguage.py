import re

n = input()
n = int(n)
languages = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'
languages = languages.split(':')
s = ''
for l in languages:
    s += l
    s += '|'

s = s[:-1]
#print(s)

regex = '^[1-9]\d{4} ('+s+')$'
for i in range(n):
    st = input()
    x = re.search(regex,st)
    if x!=None:
        print('VALID')
    else: print('INVALID')
    