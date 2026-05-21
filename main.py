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
    pass

class DatabaseHandling:
    pass
        