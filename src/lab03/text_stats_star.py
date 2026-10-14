from src.lib.text import normalize, tokenize, count_freq, top_n
txt=normalize(input())
cnt=tokenize(txt)
slov=count_freq(cnt)
top=top_n(slov,n=5)
print(f'{'слово':<10}{'| частота':>7}')
print('----------------------')
for i in top:
    print(f'{i[0]:<10}{'|':>1} {i[1]}')