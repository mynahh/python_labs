from src.lib.text import normalize, tokenize, count_freq, top_n
txt=normalize(input())
cnt=tokenize(txt)
slov=count_freq(cnt)
top=top_n(slov,n=5)
print(f'Всего слов: {len(cnt)}')
print(f'Уникальных слов: {len(slov)}')
print('Топ-5')
for i in top:
    print(f'{i[0]}:{i[1]}')



