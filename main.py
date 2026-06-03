# -*- coding: utf-8 -*-

from input_output import InputOutput
from database_handling import DatabaseHandling
from app import Conjugar
    
def main():
    io = InputOutput()
    db = DatabaseHandling()
    app = Conjugar(io, db)
    app.run()
    
if __name__ == "__main__":
    main()
    

        