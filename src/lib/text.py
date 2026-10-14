import re
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


def tokenize(text: str) -> list[str]:
    sp=re.findall(r'\w+(?:-\w+)*',text)
    return sp

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq={}
    for w in tokens:
        freq[w] = freq.get(w,0)+1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sp=sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return sp[0:n]


