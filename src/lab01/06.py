a=int(input('in_1: '))
sp=[0]*a
for i in range(a):
    sp[i]=input(f'in{i+2}: ').split()
o=0
z=0
for i in range(len(sp)):
    if sp[i][-1]=='True':
        o+=1
    else:
        z+=1
print('out:',o,z)