# ЛР3 — Тексты и частоты слов (словарь/множество)
## text.py
### normilize 
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=str(text)
    if casefold:
        text=text.casefold()
    else:
        text=text.lower()
    if yo2e:
        text=text.replace('ё','е')
    text=text.replace('\t',' ').replace('\r',' ').replace('\n',' ')
    text=' '.join(text.split())
    return text
```
тест
```python
#normalize
print(normalize("ПрИвЕт\nМИр\t") )
print(normalize("ёжик, Ёлка") )
```
![](/images/lab03/count_freq.png)
### tokenize
Выделяет слова из текста и выводит список строк
```python
import re
def tokenize(text: str) -> list[str]:
    sp=re.findall(r'\w+(?:-\w+)*',text)
    return sp
```
тест
```python
# tokenize
print(tokenize("привет, мир!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год")
```
![](/images/lab03/tokenize.png)
### count_freq
На вход функция получает список строк, возвращает словарь, со словом и количеством его повторений
```python 
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq={}
    for w in tokens:
        freq[w] = freq.get(w,0)+1
    return freq
```
тест
```python
# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
print(top_n(freq, 2))
```
![](/images/lab03/count_freq.png)
### top_n
на вход функция получает словарь, выводит список топ n слов по повторениям
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sp=sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return sp[0:n]
```
тест
```python
# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
print(top_n(freq2, 2))
```
![](/images/lab03/top_n.png)
## text_stats.py
Программа читает строку из stdin и выводит количество слов, уникальных слов,
топ-5 самых частоповторяющихся слов, пользуясь функциями из файла text.py
```python
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
```
пример работы
![](/images/lab03/text_stats.png)