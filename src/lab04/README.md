# Лаборотрная работа №4 - Файлы: TXT/CSV и отчёты по текстовой статистике
## Задание A
### Функция read_text
``` python
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p=Path(path)
    ''' Читает файл и возвращает его в виде строки.
    Аргументы: path, encoding
    -path: путь к файлу
    -encoding: кодировка файла, по умолчанию utf-8, можно выбрать другую
    указав её как аргумент, например: encoding="cp1251" '''
    return p.read_text(encoding=encoding)
```
Функция читает файл и возвращает его одной строкой(по умолчанию'utf-8').Если файл не найден - FileNotFoundError, при неподходящей кодировке UnicodeDecodeError

### Функция write_csv
``` python
def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    '''Записывает список строк|списков|кортежей в csv файл, разделитель - запятая
    Аргументы: rows, path, header
    -rows: строки таблицы(все должны быть одной длины)
    -path: путь к файлу
    -header: заголовок таблицы, пишется первой строкой(при наличии)
    Raise: ValueError если строки разной длины'''
    p = Path(path)
    rows = list(rows)
    if rows:
        ln=len(rows[0])
        for row in rows:
            if len(row)!= ln:
                raise ValueError('все cтроки должны иметь одинаковое количество элементов')
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```
Функция записывает строки в csv файл. Перед записью Проверяется наличие соответсвие строк на равное количество элементов, наличие заголовка.
## Задание B text_report
``` python
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
```
Функция получает на вход путь к файлу, и кодировку, после выводит статистику в консоль(общее количество слов, кол-во уникальных слов, топ в5) сохраняет /data/out/lab04/report.csv отчет по колнкам word count через запятую
## Тесты
### Тест А
Входные данные в input.txt
``` 
Привет, мир! Привет!!!
```
Консоль
![](/images/lab04/консоль_а.png)
Отчет в svc
![](/images/lab04/csv_a.png)
### Тест B
Входной файл пустой
Консоль
![](/images/lab04/консоль_б.png)
Отчет в svc
![](/)
### Тест с
Входной файл в кодировке cp1251
```
Привет #cp1252
```
Консоль
![](/images/lab04/консоль_с.png)
Отчет в svc
![](/images/lab04/csv_c.png)