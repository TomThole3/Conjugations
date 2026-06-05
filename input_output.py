# -*- coding: utf-8 -*-

import os

class InputOutput:
    """
    Class concerned with all (console-based) input and output
    """
    
    def get_filters(self, options, type_string):
        """
        Prompts user which items of a given selection it wants to practice

        Parameters
        ----------
        options : full list of all items that can be chosen
        type_string : type of item that is chosen (e.g. tense)

        Returns
        -------
        selected : list of all selected items
        """
        selected = []
        while options:
            print(f"Please name one {type_string} you would like to practice, type 'all' to select all, type 'stop' if your selection is complete")
            print('The list to choose from is: ' + ', '.join(options))
            selection = input().lower().strip()
            if selection == 'stop' and selected:
                return selected
            elif selection == 'stop' and not selected:
                print(f'please select at least one {type_string} first')
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
        """
        Formulates user question for a verb in a certain tense
        
        Parameters
        ----------
        infinitive : infinitive of the target answer
        tense : tense of the target answer
        person : person of the target answer

        Returns
        -------
        Answer given by the user
        """
        print(f'{infinitive} {tense}')
        return input(f'{person} ')
    
    def print_correct(self, answer):
        """
        Shows correct answers after a wrong answer and asks user if they want to rectify 
        the answer or show the entire table
        
        Parameters
        ----------
        answer : correct answer

        Returns
        -------
        User's choice of the next action
        """
        print(f'The correct answer was: {answer}')
        return input('Press enter to skip, type correct to rectify answer, type table to see the entire table ')
    
    def print_stats(self, total, passed):
        """
        Parameters
        ----------
        total : total number of questions
        passed : number of questions answered so far

        Returns
        -------
        None.
        """
        print(f'Progress: word {passed}/{total}')
        
    def clear_console(self):
        """
        Clears the console

        Returns
        -------
        None.
        """
        try:
            from IPython import get_ipython
            get_ipython().run_line_magic('clear', '')
        except Exception:
            os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_table(self, table_information):
        """
        Prints all conjugation in a certain tense

        Parameters
        ----------
        table_information : all conjugations and their associate person

        Returns
        -------
        None.
        """
        self.clear_console()
        for (person, verb) in table_information:
            print(f'{person}, {verb}')
        input('Press enter to continue')
        
    def print_final_stats(self, total, incorrect, minutes, seconds, wrong):
        """
        Prints overall statistics 

        Parameters
        ----------
        total : total number of words practiced
        incorrect : number of incorrect answers in the first pass
        minutes : minutes that practicing took
        seconds : seconds that practicing took
        wrong : list of wrong answers

        Returns
        -------
        None.
        """
        self.clear_console()
        print(f'Session complete! It took a total of {minutes} minutes and {seconds} seconds')
        print(f'You answered {total-incorrect} out of the {total} questions right')
        print('The words that you answered incorrectly were: ')
        for (_, _, person, answer) in wrong:
            print(f'{person} {answer}')