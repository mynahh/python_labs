from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lab04.io_txt_csv import read_text, write_csv
def report(path: str, encoding: str='utf-8'):
    txt=read_text(path=path,encoding=encoding)
    normtext=normalize(txt)
    token=tokenize(normtext)
    freq=count_freq(token)
    top=top_n(freq,5)
    print('Всего слов:',len(token))
    print('Уникальных слов:',len(freq))
    print('Топ-5:')
    for i in top:
        print(f'{i[0]}:{i[1]}')
    write_csv(rows=top_n(freq,len(freq)),path="data/out/lab04/report.csv",header=('word','count'))

if __name__=='__main__':
    report('data/samples/lab04/input.txt')
    report('data/samples/lab04/zero.txt')
    report('data/samples/lab04/input1251.txt','cp1251')
    print('готово')
