import pandas as pd 

with open('books.json', encoding='utf-8-sig') as f:
    df = pd.read_json(f)
    df.index += 2

df.to_csv('books.csv', encoding='utf-8')