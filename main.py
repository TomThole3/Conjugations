# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:18:36 2026

@author: tthol
"""

import sqlite3
import pandas as pd

class Conjugar:
    def __init__(self, io):
        self.io = io
    
    def run(self):
        db = DatabaseHandling()
        db.excel_to_db()
        db.get_names()
    
class InputOutput:
    
    def get_tenses(self):
        valid_tenses = {"present", "present progressive", "preterite", "imperfect", "future",
                        "conditional", "present perfect", "pluperfect", "future perfect", "conditional perfect",
                        "present subjunctive", "imperfect subjunctive", "present perfect subjunctive",
                        "pluperfect subjunctive", "past progressive", "future progressive" "imperative affirmative",
                        "negative imperative"}

        print("Please indicate which tenses you would like to cover?")
        
        while True:
            tenses = input().lower().split(",")
            stripped_set = set([tense.strip() for tense in tenses])
            if stripped_set.issubset(valid_tenses):
                break
            else:
                print("Please select a valid set of tenses")
        return stripped_set
    
    def verb_selector(self):
        while True:
            selector = input("Would you like to select verbs based on ending, power or name? ")
            selector = selector.strip().lower()
            if selector == "ending" or selector == "power" or selector == "name":
                return selector
            print("Please enter a valid input")
            
    def get_ending(self):
        print("Which verb endings would you like to practice?")
        while True:
            ending = input("Please choose one from ir, ar, er ").lower().strip()
            if ending == "ir" or ending == "ar" or ending == 'er':
                return ending
            print('Please select a valid ending')
    
    def get_power(self):
        print("Which power would you like to practice?")
        while True:
            ending = input("Please choose one from strong, weak ").lower().strip()
            if ending == "weak" or ending == 'strong':
                return ending
            print('Please select a valid power')
    
    def get_names(self):
        pass
    
    
class DatabaseHandling:
    
    def __init__(self):
        pass
    
    def excel_to_db(self):
        path = r"C:\Users\tthol\OneDrive\Bureaublad\de echte git programmaties\spanish verb conjugations\verbs excel.xlsx"
        ex = pd.read_excel(path)
        with sqlite3.connect('verbs.db') as conn:
            ex.to_sql('Blad1', conn, if_exists='replace')
    
    def get_names(self):
        with sqlite3.connect('verbs.db') as conn:
            c = conn.cursor()
            queried_names = c.execute("SELECT DISTINCT infinitive FROM  Blad1")
            names = queried_names.fetchall()
        return [name for (name, ) in names]
    
def main():
    io = InputOutput()
    db = DatabaseHandling()
    app = Conjugar(io)
    app.run()
    
if __name__ == "__main__":
    main()
    

        