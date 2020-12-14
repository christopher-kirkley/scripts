#!/usr/bin/env python3

import pandas as pd

def create_df():
    df = pd.read_excel(file, skiprows=4)
    return df

class ImportedCSV:
    def __init__(self, type, file):
        self.file = file
        self.df = pd.read_excel(file, skiprows=4)
        self.type = type #catalog or artist
        self.df = self.df[self.df['Date'].notnull()]
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Memo/Description'] = self.df['Memo/Description'].str.split('  ').str[0]
    
    def do_something(self):
        if self.type == 'artist':
            self.df['Customer'] = self.df['Customer'].str.replace('Artists:','')
            self.df.rename(columns={'Date': 'date',
                            'Customer': 'artist_name',
                            'Name': 'vendor',
                            'Memo/Description': 'description',
                            'Class': 'expense_type',
                            'Amount': 'net'},
                           inplace=True)

        if self.type == 'catalog':
            df['Customer'] = df['Customer'].str.replace('Record Production:','').str[0:6]
            df.rename(columns={'Date': 'date',
                            'Customer': 'catalog_number',
                            'Name': 'vendor',
                            'Memo/Description': 'description',
                            'Class': 'expense_type',
                            'Amount': 'net'},
                           inplace=True)
    def finish(self):
        self.df = self.df.reindex(columns=columns_for_db)
        self.df.to_csv(f'test_{user_value}.csv', index=False)

columns_for_db = [
                  'date',
                  'artist_name',
                  'catalog_number',
                  'vendor',
                  'expense_type',
                  'description',
                  'net',
                  'item_type'
                  ]

choices = {
        '1': 'Artist',
        '2': 'Catalog',
        }

for key, value in choices.items():
    print(f'{key}...........................{value}')

user_key = input('Choose wisely: ')
user_value = choices[user_key].lower()

file = '/Users/ck/Documents/sahel_label/financial/expenses/2019/Sahel+Sounds_QB_artist.xlsx'

new = ImportedCSV(user_value, file)
new.do_something()
new.finish()

