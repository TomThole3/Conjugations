# -*- coding: utf-8 -*-

import os

class InputOutput:
    
    def get_filters(self, options, type_string):
        selected = []
        while options:
            print(f"Please name one {type_string} you would like to practice, type 'all' to select all, type 'stop' if your selection is complete")
            print("The list to choose from is: " + ', '.join(options))
            selection = input().lower().strip()
            if selection == "stop":
                return selected
            elif selection == 'all':
                selected.extend(options)
                return selected
            elif selection in options:
                selected.append(selection)
                options.remove(selection)
                print('The list you have selected is: ' + ', '.join(selected))
            else:
                print(f'Please select a valid {type_string}')
                
    def print_question(self, infinitive, tense, person):
        print(f'{infinitive} {tense}')
        return input(f'{person} ')
    
    def print_correct(self, answer):
        print(f"The correct answer was: {answer}")
        return input("Press enter to skip, type correct to rectify answer, type table to see the entire table ")
    
    def print_stats(self, total, passed):
        print(f'Progress: word {passed}/{total}')
        
    def clear_console(self):
        try:
            from IPython import get_ipython
            get_ipython().run_line_magic('clear', '')
        except Exception:
            os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_table(self, table_information):
        for (person, verb) in table_information:
            print(f'{person}, {verb}')
        input("Press enter to continue")
        
    def print_final_stats(self, total, incorrect, minutes, seconds, wrong):
        print(f'Session complete! It took a total of {minutes} minutes and {seconds} seconds')
        print(f'You answered {total-incorrect} out of the {total} questions right')
        print('The words that you answered incorrectly were: ')
        for (_, _, person, answer) in wrong:
            print(f'{person} {answer}')