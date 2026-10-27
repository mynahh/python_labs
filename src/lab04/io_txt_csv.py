from pathlib import Path
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p=Path(path)
    ''' Читает файл и возвращает его в виде строки.
    Аргументы: path, encoding
    -path: путь к файлу
    -encoding: кодировка файла, по умолчанию utf-8, можно выбрать другую
    указав её как аргумент, например: encoding="cp1251" '''
    return p.read_text(encoding=encoding)

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
