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
    
    
if __name__=='__main__':
    csv_to_xlsx('data/samples/lab05/cities.csv','data/out/lab05/cities.xlsx')
    csv_to_xlsx('data/samples/lab05/csvxlsx.csv','data/out/lab05/csvxlsx.xlsx')
    print('готово')
#python3 -m src.lab05.csv_xlsx
    
    