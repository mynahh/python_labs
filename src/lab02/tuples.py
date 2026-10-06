def format_record(rec: tuple[str,str, float]) -> str:
    if not isinstance(rec, tuple):
        raise TypeError('запись должна быть кортежем')
    if len(rec) !=3:
        raise ValueError('неверное количество элементов в записи')
    fio, group, gpa = rec
    if not isinstance(gpa, (float,int)):
        raise TypeError('GPA должен быть числом')
    if not 0.0 <= gpa <= 5.0:
        raise ValueError('GPA должен быть в диапазоне от 0 до 5')
    if not isinstance(fio, str):    
        raise TypeError('ФИО должен быть строкой')
    if not isinstance(group, str):
        raise TypeError('группа должна быть строкой')
    FIOSPLIT= fio.split()
    if len(FIOSPLIT) not in (2,3):
        raise ValueError('ФИО должно состоять из 2 или 3 слов')
    surname= FIOSPLIT[0].strip().capitalize()
    initials= ''.join(f"{name[0].upper()}." for name in FIOSPLIT[1:])
    group = group.strip()
    if not group:
        raise ValueError('группа не может быть пустой строкой')
    return f'{surname} {initials}, гр. {group}, GPA {gpa:.2f}'
def result(function, cases) -> None:
    for value in cases:
        try:
            result = function(value)
        except (ValueError, TypeError) as error:
            result = error

        print(f"{value} -> {result}")
if __name__ == '__main__':
    print('format_record:')
    result(format_record, [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "BPM-01", 3.999),
    ("Иванов Иван", "", 4.0),
    ("Иванов Иван", "BIVT-01", "пять"),
    ])