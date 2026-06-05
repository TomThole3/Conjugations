# -*- coding: utf-8 -*-

import random as rand
import time


class Conjugar:
    """
    Class containing the structure of the program
    """
    
    def __init__(self, io, db):
        """
        Parameters
        ----------
        io : instance of InputOutput class
        db : instance of DatabaseHandling class

        Returns
        -------
        None.
        """
        self.io = io
        self.db = db
        self.logic = GameLogic(io, db)
    
        
    def run(self):
        """
        Handles the main structure of the program directing the different classes

        Returns
        -------
        None.
        """
        self.db.excel_to_db()
        tenses, endings, powers, infinitives = (self.io.get_filters(
            self.db.get_unique_values(field), field) for field in ('tense', 'ending', 'power', 'infinitive'))
        verbs = self.db.get_filtered_entries(tenses, endings, powers, infinitives)
        rand.shuffle(verbs)
        session = Session(len(verbs))
        wrong = self.logic.gameloop(verbs, session)
        minutes, seconds = session.stop_time()
        self.io.print_final_stats(session.original_total, session.incorrect, minutes, seconds, wrong)
        
        
class Session:
    """
    Class containing information of a single session
    """
    
    def __init__(self, total_words):
        """
        Parameters
        ----------
        total_words : the total number of words being practiced in this session

        Returns
        -------
        None.
        """
        self.total_words = total_words
        self.original_total = total_words
        self.passed = 0
        self.incorrect = 0
        self.start_time = time.time()
        
    def stop_time(self):
        """
        Calculates the time since the initialization of the class

        Returns
        -------
        Minutes and seconds since the initialization of the class
        """
        duration = time.time() - self.start_time
        return int(duration/60), int(duration%60)
        
    
class GameLogic:
    """
    Class concerned with the main loop for practicing
    """

    def __init__(self, io, db):
        """
        Parameters
        ----------
        io : instance of InputOutput class
        db : instance of DatabaseHandling class

        Returns
        -------
        None.
        """
        self.io = io
        self.db = db
        
    def gameloop(self, verb_list, session, repeat = True):
        """
        Main loop of practicing verbs. Delegates question to IO and handles incorrect questions. 
        Recursively calls itself to repeat incorrect answers once

        Parameters
        ----------
        verb_list : list containing all words to be practiced.
        session : instance of session class belonging to this practice session
        repeat : whether this verb_list is a repetition of incorrect answers. The default is True

        Returns
        -------
        wrong : list of all words answered incorrectly on the first try
        """
        wrong = []
        while verb_list:
            self.io.clear_console()
            infinitive, tense, person, answer = verb_list[0]
            self.io.print_stats(session.total_words, session.passed)
            user_answer = self.io.print_question(infinitive, tense, person)
            wrong_index = min(3, len(verb_list)) # wrong answers are reasked after 3 words, except at the end of the list
            if user_answer != answer:
                verb_list.insert(wrong_index, verb_list[0])
                if verb_list[0] in wrong: # word has been answered incorrectly before
                    session.total_words += 1 if repeat else 0 
                else:
                    session.total_words += 2 if repeat else 1 # +2 since it will get repeated in 3 words and during next phase
                    session.incorrect += 1 if repeat else 0
                    wrong.append(verb_list[0])
                check = self.io.print_correct(answer)
                if check == 'correct': # user informs that previous answer was actually correct
                    wrong.pop()
                    verb_list.pop(max(0, wrong_index-1))
                elif check == 'table':
                    self.table(infinitive, tense)
            session.passed += 1
            verb_list.pop(0)
        if repeat:
            self.gameloop(wrong.copy(), session, False) # wrong answers are repeated
            return wrong
            
    def table(self, infinitive, tense):
        """
        Helper function to print table of an incorrect word's conjugations

        Parameters
        ----------
        infinitive : infinitive of the table to be printed
        tense : tense of the table to be printed

        Returns
        -------
        None.
        """
        table_information = self.db.get_verb(infinitive, tense)
        self.io.print_table(table_information)
         