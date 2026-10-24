from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lab04.io_txt_csv import read_text, write_csv
path="data/input.txt"
txt=read_text(path)
normtext=normalize(txt)
token=tokenize(normtext)
freq=count_freq(token)
top=top_n(freq,5)
print('Всего слов:',len(token))
print('Уникальных слов:',len(freq))
print('Топ-5:')
for i in top:
    print(f'{i[0]}:{i[1]}')
write_csv(rows=top_n(freq,len(freq)),path="data/report.csv",header=('word','count'))