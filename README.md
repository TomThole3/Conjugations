# Verb Conjugations
This project is a console-based word repetition application to practice verb conjugations in Spanish. It is written in Python. I have written this program because of the lack of free practice software available with the functionality I wanted (rectification of answers, option to print tables). The user can make a selection of which verbs they want to practice based on infinitive, tense, ending or regularity, and will subsequently be tested. The verbs are stored in a SQLite3 database which can easily be edited through an excel file. 

## Requirements:
 - Python 3.10+
 - pandas
 - openpyxl

## Running the script
To run the script, navigate to the folder using your console. Then, run main.py file (be sure to have python added to your PATH).
You are now able to select the verbs you want to practice.

cd path/to/project
python main.py

## Updating the database
The easiest way to update the database is to edit the excel file. State the infinitive, tense, person (yo, tú, él, nosotros, vosotros, ellos), ending (ir, ar, er) and conjugation for each verb you would like to practice. Once the file is saved the program will automatically update the database with the new contents of the excel file.
Tip: LLMs are excellent for completing this task with ease.

## How it works (High level)
- Verbs are imported from the excel file to the database
- User selects which verbs they want to practice
- Verbs are prompted to the user and repeated after 3 words if they answer incorrectly
- Wrong answers are repeated once more at the end
- Final statistics are shown
