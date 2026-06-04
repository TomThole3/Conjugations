# -*- coding: utf-8 -*-

import random as rand
import time


class Conjugar:
    
    def __init__(self, io, db):
        self.io = io
        self.db = db
        self.logic = GameLogic(io, db)
        
    def run(self):
        tenses, endings, powers, infinitives = (self.io.get_filters(
            self.db.get_unique_values(field), field) for field in ('tense', 'ending', 'power', 'infinitive'))
        verbs = self.db.get_filtered_entries(tenses, endings, powers, infinitives)
        rand.shuffle(verbs)
        session = Session(len(verbs))
        wrong = self.logic.gameloop(verbs, session)
        minutes, seconds = session.stop_time()
        self.io.print_final_stats(session.original_total, session.incorrect, minutes, seconds, wrong)
        
        
class Session:
    
    def __init__(self, total_words):
        self.total_words = total_words
        self.original_total = total_words
        self.passed = 0
        self.incorrect = 0
        self.start_time = time.time()
        
    def stop_time(self):
        duration = time.time() - self.start_time
        return int(duration/60), int(duration%60)
        
class GameLogic:

    def __init__(self, io, db):
        self.io = io
        self.db = db
        
    def gameloop(self, verb_list, session, repeat = True):
        wrong = []
        while verb_list:
            self.io.clear_console()
            infinitive, tense, person, answer = verb_list[0]
            self.io.print_stats(session.total_words, session.passed)
            user_answer = self.io.print_question(infinitive, tense, person)
            wrong_index = min(3, len(verb_list))
            if user_answer != answer:
                verb_list.insert(wrong_index, verb_list[0])
                if verb_list[0] in wrong:
                    session.total_words += 1 if repeat else 0
                else:
                    session.total_words += 2 if repeat else 1
                    session.incorrect += 1 if repeat else 0
                    wrong.append(verb_list[0])
                check = self.io.print_correct(answer)
                if check == 'correct':
                    wrong.pop()
                    verb_list.pop(max(0, wrong_index-1))
                elif check == 'table':
                    self.table(infinitive)
            session.passed += 1
            verb_list.pop(0)
        if repeat:
            self.gameloop(wrong.copy(), session, False)
            return wrong
            
    def table(self, infinitive):
        table_information = self.db.get_verb(infinitive)
        self.io.print_table(table_information)
         