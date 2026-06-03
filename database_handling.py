# -*- coding: utf-8 -*-

import sqlite3
from pathlib import Path
import os
import pandas as pd
from itertools import chain

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
            queried_names = c.execute(f"""SELECT DISTINCT {column} FROM Blad1""")
            names = queried_names.fetchall()
        return [name for (name, ) in names]
    
    def get_filtered_entries(self, tenses, endings, powers, infinitives):
        tense_placeholder = ', '.join('?' for _ in tenses)
        ending_placeholder = ', '.join('?' for _ in endings)
        power_placeholder = ', '.join('?' for _ in powers)
        infinitive_placeholder = ', '.join('?' for _ in infinitives)
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
    
    def get_verb(self, infinitive):
        with sqlite3.connect('verbs.db') as conn:
            c = conn.cursor()
            queried_names = c.execute(f"""SELECT person, verb FROM Blad1 WHERE infinitive = '{infinitive}'""")
            names = queried_names.fetchall()
        return names