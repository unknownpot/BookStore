import pandas as pd 

with open('books.json') as f:
    df = pd.read_json(f)

df.to_csv('books.csv', index = False)