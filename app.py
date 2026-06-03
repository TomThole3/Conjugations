# -*- coding: utf-8 -*-

import random as rand

class Conjugar:
    def __init__(self, io, db):
        self.io = io
        self.db = db
        self.total_words = 0
        self.passed = 0
    
    def run(self):
        tenses, endings, powers, infinitives = (self.io.get_filters(
            self.db.get_unique_values(field), field) for field in ('tense', 'ending', 'power', 'infinitive'))
        verbs = self.db.get_filtered_entries(tenses, endings, powers, infinitives)
        rand.shuffle(verbs)
        self.total_words = len(verbs)
        self.gameloop(verbs)
        
    def gameloop(self, verb_list, repeat = True):
        wrong = []
        while verb_list:
            self.io.clear_console()
            infinitive, tense, person, answer = verb_list[0]
            self.io.print_stats(self.total_words, self.passed+1)
            user_answer = self.io.print_question(infinitive, tense, person)
            wrong_index = min(3, len(verb_list))
            if user_answer != answer:
                verb_list.insert(wrong_index, verb_list[0])
                self.total_words += 1
                check = self.io.print_correct(answer)
                if check == 'correct':
                    wrong.pop(0)
                    verb_list.pop(max(0, wrong_index-1))
                elif check == 'table':
                    self.table(infinitive)
                wrong.append(verb_list[0])
            else:
                self.passed += 1
            verb_list.pop(0)
        if repeat:
            self.gameloop(wrong, False)
            
    def table(self, infinitive):
        table_information = self.db.get_verb(infinitive)
        self.io.print_table(table_information)
        