a=input()
h=''
for i in range(len(a)):
    if a[i]==a[i].upper():
        h=a[i]
        break
s=a.find(h)
a=a[s:-1]
print(a)
sp=[]
for i in range(0,10):
    if a.find(str(i))>=0:
        sp+=[a.find(str(i))]
u=min(sp)
o=''
for i in range(0,len(a),u+1):
    o+=a[i]
o+='.'
print('out:',o)
    