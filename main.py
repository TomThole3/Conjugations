# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:18:36 2026

@author: tthol
"""

import sqlite3
import pandas as pd
import os
from pathlib import Path

class Conjugar:
    def __init__(self, io, db):
        self.io = io
        self.db = db
    
    def run(self):
        possible_tenses = self.db.get_unique_values('tense')
        tenses = self.io.get_filters(possible_tenses, 'tense')
        possible_endings = self.db.get_unique_values('ending')
        endings = self.io.get_filters(possible_endings, 'ending')
        possible_powers = self.db.get_unique_values('power')
        power = self.io.get_filters(possible_powers, 'power')
        possible_infinitives = self.db.get_unique_values('infinitive')
        infinitives = self.io.get_filters(possible_infinitives, 'infinitive')
            
    
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
                selected.append(options)
                return selected
            elif selection in options:
                selected.append(selection)
                options.remove(selection)
                print('The list you have selected is' + ', '.join(selected))
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
        
    
def main():
    io = InputOutput()
    db = DatabaseHandling()
    app = Conjugar(io, db)
    app.run()
    
    
if __name__ == "__main__":
    main()
    

        