# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:18:36 2026

@author: tthol
"""
class Conjugar:
    def __init__(self, io):
        self.io = io
    
    def run(self):
        tenses = self.io.get_tenses()
        verb_type = self.io.verb_type()
    
class InputOutput:
    
    def get_tenses(self):
        valid_tenses = ("present", "present progressive", "preterite", "imperfect", "future",
                        "conditional", "present perfect", "pluperfect", "future perfect", "conditional perfect",
                        "present subjunctive", "imperfect subjunctive", "present perfect subjunctive",
                        "pluperfect subjunctive", "past progressive", "future progressive" "imperative affirmative",
                        "negative imperative")

        print("What tenses would you like to cover?")
        
        while True:
            tenses = input().lower().split(",")
            stripped_set = set([tense.strip() for tense in tenses])
            if stripped_set.issubset(valid_tenses):
                break
            else:
                print("Invalid input")
        return stripped_set
    
    def verb_type(self):
        while True:
            type_ = input("Do you want to select verbs based on ending, power or name? ")
            type_ = type_.strip().lower()
            if type_ == "ending" or type_ == "power" or type_ == "name":
                return type_
            print("Invalid input")
        
            
    def get_verbs(self):
        pass
    
class DatabaseHandling:
    pass


def main():
    io = InputOutput()
    db = DatabaseHandling()
    app = Conjugar(io)
    app.run()
    
if __name__ == "__main__":
    main()
    

        