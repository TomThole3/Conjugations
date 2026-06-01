# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:18:36 2026

@author: tthol
"""

import sqlite3
import pandas as pd
import os
from pathlib import Path
from itertools import chain

class Conjugar:
    def __init__(self, io, db):
        self.io = io
        self.db = db
    
    def run(self):
        tenses, endings, powers, infinitives = (self.io.get_filters(
            self.db.get_unique_values(field), field) for field in ('tense', 'ending', 'power', 'infinitive'))
        verbs = self.db.get_filtered_entries(tenses, endings, powers, infinitives)
        print(verbs)
        
class InputOutput:
    
    def get_filters(self, options, type_string):
        selected = []
        while True:
            print(f"Please name one {type_string} you would like to practice, type 'all' to select all, type 'stop' if your selection is complete")
            print("The list to choose from is: " + ', '.join(options))
            selection = input().lower().strip()
            if selection == "stop":
                return selected
            elif selection == 'all':
                selected.extend(options)
                return selected
            elif selection in options:
                selected.append(selection)
                options.remove(selection)
                print('The list you have selected is: ' + ', '.join(selected))
            else:
                print(f'Please select a valid {type_string}')
            if not options:
                return selected
            
    
class DatabaseHandling:
    
    def __init__(self):
        pass
        
    def excel_to_db(self):
        cwd = Path.cwd()
        path = cwd.parents[0]
        path = os.path.join(path, "verbs excel.xlsx")
        ex = pd.read_excel(path)
        with sqlite3.connect('verbs.db') as conn:
            ex.to_sql('Blad1', conn, if_exists='replace')
    
    def get_unique_values(self, column):
        with sqlite3.connect('verbs.db') as conn:
            c = conn.cursor()
            queried_names = c.execute(f"SELECT DISTINCT {column} FROM Blad1")
            names = queried_names.fetchall()
        return [name for (name, ) in names]
    
    def get_filtered_entries(self, tenses, endings, powers, infinitives):
        print(tenses, endings, powers, infinitives)
        tense_placeholder = ', '.join('?' for _ in tenses)
        ending_placeholder = ', '.join('?' for _ in endings)
        power_placeholder = ', '.join('?' for _ in powers)
        infinitive_placeholder = ', '.join('?' for _ in infinitives)
        print(tense_placeholder, ending_placeholder, power_placeholder, infinitive_placeholder)
        query = f"""SELECT infinitive, tense, person, verb FROM Blad1
                    WHERE tense IN ({tense_placeholder})
                    AND ending IN ({ending_placeholder})
                    AND power IN ({power_placeholder})
                    AND infinitive IN ({infinitive_placeholder})"""
        with sqlite3.connect('verbs.db') as conn:
            c = conn.cursor()
            queried_entries = c.execute(query, tuple(chain.from_iterable((tenses, endings, powers, infinitives))))
            names = queried_entries.fetchall()
        return names
        
    
def main():
    io = InputOutput()
    db = DatabaseHandling()
    app = Conjugar(io, db)
    app.run()
    
    
if __name__ == "__main__":
    main()
    

        