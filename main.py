# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:18:36 2026

@author: tthol
"""

class Main:
    def main(self):
        io = InputOutput()
        db = DatabaseHandling()
        app = Conjugar(io)
        app.run()
        
class Conjugar:
    def __init__(self, io):
        self.io = io
    
    def run(self):
        pass
    
class InputOutput:
    def get_settings():
        valid_tenses = ("present", "present progressive", "preterite", "imperfect", "future",
                        "conditional", "present perfect", "pluperfect", "future perfect", "conditional perfect",
                        "present subjunctive", "imperfect subjunctive", "present perfect subjunctive",
                        "pluperfect subjunctive", "past progressive", "future progressive" "imperative affirmative",
                        "negative imperative")

        print(
        "What tenses would you like to cover?"
        
        )
        while True:
            tenses = input().lower().split(",")
            stripped_set = set([tense.strip() for tense in tenses])
            if stripped_set.issubset(valid_tenses):
                break
            else:
                print("Invalid input")
            
    def get_verbs():
        pass
    
class DatabaseHandling:
    pass
        