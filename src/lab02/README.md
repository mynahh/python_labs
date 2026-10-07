# Лабороторная работа №2 - Коллекции и матрицы
## arrays.py
### min_max
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError('Пустой список')
    maxx=nums[0]
    minn=nums[0]
    for num in nums:
        if num <minn:
            minn=num
        if num >maxx:
            maxx=num
    return minn,maxx
```

Функция проверяет список, если он не пустой, то выводит кортежем наименеший и наибольший элемент входного списка.
![](/images/lab02/mimaxexit.png)

### unique_sorted

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    for num in nums:
        if not isinstance(num,(int,float)):
            raise TypeError('Все элементы списка должны быть числами')
    uniq=list(set(nums))
    for i in range(len(uniq)):
        for x in range(i+1,len(uniq)):
            if uniq[i]>uniq[x]:
                uniq[i],uniq[x]=uniq[x],uniq[i]
    return uniq
```

Функция  проверяет состоит ли список из чисел(int|float), исключает повторы создавая множество, после снова создает список и сортирует его.

![](/images/lab02/unique_sortedexit.png)

### flatten
```python
def flatten(mat: list[list | tuple]) -> list:
    flat=[]
    for row in mat:
        if not isinstance(row,(list,tuple)):
            raise TypeError('Все элементы должны быть списками или кортежами')
        flat.extend(row)
    return flat
```

Функция проверяет, является ли списком или кортежем каждый элемент полученного списка, затем добавляет их в выходной список.
![](/images/lab02/flattenexit.png)

## matrix.py
### check(вспомогательная функция)
Проверяет все строки матрицы, на то являются ли они спсиками, и проверяет является ли матрица прямоугольной.
```python
def check(mat: list[list[float | int]]) -> None:
    for row in mat:
        if not isinstance(row,list):
            raise TypeError('Все строки матрицы должны быть списками')
    if mat:
        lenrow=len(mat[0])
        for row in mat:
            if len(row) != lenrow:
                raise ValueError('Матрица должна быть прямоугольной')
```
### transpose
С помощью функции check проверяет матрицу, за тем по каждому столбцу создаёт строку новый матрицы, сохраняя их в res.
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    check(mat)
    if not mat:
        return []
    res=[]
    for i in range(len(mat[0])):
        nrow=[]
        for row in mat:
            nrow.append(row[i])
        res.append(nrow)
    return res
```
![](/images/lab02/transposeexit.png)
### row_sums
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    check(mat)
    return [sum(row) for row in mat]
```

Функция проверяет на правильность матрицу с помощью функции check, а после возвращает генератор с суммой для каждой строки матрицы.
![](/images/lab02/rowsumsexit.png)
### col_sums
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    check(mat)
    return(row_sums(transpose(mat)))
```
![](/images/lab02/colsumsexit.png)
Функция проверяет на правильность матрицу с помощью функции check, а после возвращает генератор с суммой для каждой строки транспонированной матрицы.
## tuples.py
```python
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
```
Функция проветряет ФИО, группу и GPA на правильность, если данные правильные, выводит фамилию с заглавной буквы вместе со склееными инициалами, группу и GPA(до двх знаков после запятой)
![](/images/lab02/tuplesexit.png)



