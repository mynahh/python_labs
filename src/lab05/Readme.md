# Лабораторная работа №5 JSON и конвертации (JSON↔CSV, CSV→XLSX)
## Задание А JSON↔CSV
### Функция json_to_csv
```python
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    if json_path[-5:].lower()!='.json':
        raise ValueError('Входной файл должен быть .json')
    if csv_path[-4:].lower()!='.csv':
        raise ValueError('Выходной файл должен быть .csv')
    json_path=Path(json_path)
    csv_path=Path(csv_path)
    try:
        with open(json_path,encoding='utf-8',) as jf:
            data=json.load(jf)
    except json.JSONDecodeError:
        raise ValueError('пустой json или неподдерживаемая структура')
    if not isinstance(data,list) or not data:
        raise ValueError('json должен быть списком словарей')
    for it in data:
        if not isinstance(it,dict):
            raise ValueError('каждый элемент списка должен быть словарем')
    fields = set()
    for it in data:
        fields.update(it.keys())
    if not fields:
        raise ValueError('элементы списка пустые')
    with open(csv_path,'w',newline='',encoding='utf-8') as cf:
        w = csv.DictWriter(cf,fieldnames=sorted(fields),restval="")
        w.writeheader()
        w.writerows(data)

```
Функция проверяет расширения файлов(json-csv), проверяет чтобы объект являлся не пустым списком словарей, собирает все ключи в алфавитном порядке, проверяет наличие заголовков колонок а после записывает заголовок и строки в csv(кодировка utf-8).
### Функция csv_to_json
```python
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    if csv_path[-4:].lower()!='.csv':
        raise ValueError('Входной файл должен быть .csv')
    if json_path[-5:].lower()!='.json':
        raise ValueError('Выходной файл должен быть .json')
    csv_path=Path(csv_path)
    json_path=Path(json_path)
    with open(csv_path,encoding='utf-8',newline='') as cf:
        read=csv.DictReader(cf)
        if not read.fieldnames:
            raise ValueError('csv пуст')
        data=list(read)
        if not data:
            raise ValueError('csv не содержит строк данных')
    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(data, jf, ensure_ascii=False, indent=2)
```
Функция проверяет расширение файлов(csv-json), читает csv в кодировке utf-8, проверяет наличие заголовка, строк данных, формирует список словарей, а после записывает его в json
## Задание B CSV → XLSX
```python
from openpyxl import Workbook
import csv
from pathlib import Path
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использует openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    if csv_path[-4:].lower()!='.csv':
        raise ValueError('входной файл должен быть csv')
    if xlsx_path[-5:].lower()!='.xlsx':
        raise ValueError('выходной файл должен быть xlsx')
    csv_path=Path(csv_path)
    xlsx_path=Path(xlsx_path)
    wb=Workbook()
    ws=wb.active
    ws.title='Sheet1'
    
    with open(csv_path,encoding='utf-8',newline='') as cf:
        data=list(csv.reader(cf))
        if not data:
            raise ValueError('csv файл пустой')
    for row in data:
        ws.append(row)
    for column in ws.columns:
        maxlen=-1
        for cell in column:
            if cell.value:
                leng=len(str(cell.value))
                maxlen=max(leng,maxlen)
        letter=column[0].column_letter
        ws.column_dimensions[letter].width = max(8,maxlen)                      
    wb.save(xlsx_path)
```
Функция проверяет расширения файлов(csv-xlsx), читает csv в кодировке utf-8, создает книгу с листом 'Sheet1', записывает строки, подбирает длинну каждой колонки по максимальной длине текста, после сохраняет xlsx файл
## Тесты
### json_to_csv
#### Входные данные
![](/images/lab05/json-csv1in.png)
![](/images/lab05/jsoncsv2in.png)
#### Вывод
![](/images/lab05/out/1.png)
![](/images/lab05/out/2.png)
### csv_to_json
#### Входные данные
![](/images/lab05/csv-json1in.png)
![](/images/lab05/cvsjson2in.png)
#### Вывод
![](/images/lab05/out/3.png)
![](/images/lab05/out/4.png)
### csv_to_xlsx
#### Входные данные
![](/images/lab05/cvs-xlsx1in.png)
![](/images/lab05/csvxlsx2in.png)
#### Вывод
![](/images/lab05/out/5.png)
![](/images/lab05/out/5.png)