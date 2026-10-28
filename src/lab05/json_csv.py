import json, csv
from pathlib import Path
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
    
if __name__=='__main__':
    json_to_csv('data/samples/lab05/people.json','data/out/lab05/people_from_json.csv')
    json_to_csv('data/samples/lab05/jsonsvc.json','data/out/lab05/jsonsvc_from_json.csv')
    csv_to_json('data/samples/lab05/people.csv','data/out/lab05/lpeople_from_csv.json')
    csv_to_json('data/samples/lab05/svcjson.csv','data/out/lab05/svcjson_from_csv.json')
    print('готово')
#python3 -m src.lab05.json_csv