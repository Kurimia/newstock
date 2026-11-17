t=open('template.html',encoding='utf-8').read()
d=open('data.js',encoding='utf-8').read()
assert t.count('/*DATA*/')==1
open('index.html','w',encoding='utf-8').write(t.replace('/*DATA*/',d))
print("built")
