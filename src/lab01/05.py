a,b,c=input('ФИО: ').split()
#print('ФИО:',a, b, c,)
print('Инициалы: 'f'{a[0].upper()}{b[0].upper()}{c[0].upper()}.')
print('Длина (символов):', len(a)+len(b)+len(c)+2)#добавляю два пробела между фио
