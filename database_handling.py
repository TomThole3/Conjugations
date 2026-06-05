# -*- coding: utf-8 -*-

import sqlite3
from pathlib import Path
import pandas as pd
from itertools import chain

class DatabaseHandling:
    """
    Class concerned with reading and writing the SQLite3 database
    """

    def __init__(self):
        cwd = Path.cwd()
        self.db_path = cwd / 'verbs.db'
        self.excel_path = cwd / 'verbs.xlsx'

    def get_connection(self):
        """
        Establishes connection with the database

        Returns
        -------
        The connection
        """
        return sqlite3.connect(self.db_path)

    def excel_to_db(self):
        """
        Imports the contents of an excel sheet to the SQLite3 database

        Returns
        -------
        None.
        """
        ex = pd.read_excel(self.excel_path)
        with self.get_connection() as conn:
            ex.to_sql('Blad1', conn, if_exists='replace')

    def get_unique_values(self, column):
        """
        Returns the unique values of one column of the database,
            such as every tense that occurs

        Parameters
        ----------
        column : columns of which the unique values are required

        Returns
        -------
        list of unique values

        """
        with self.get_connection() as conn:
            c = conn.cursor()
            queried_names = c.execute(f"SELECT DISTINCT {column} FROM Blad1")
            return [name for (name,) in queried_names.fetchall()]

    def get_filtered_entries(self, tenses, endings, powers, infinitives):
        """
        Querying the database for all verbs that will be practiced

        Parameters
        ----------
        tenses : list of tenses that will be practiced
        endings : list of endings that will be practiced
        powers : list of powers that will be practiced
        infinitives : list of infinitives that will be practiced

        Returns
        -------
        list of all verbs conforming the parameters

        """
        tense_placeholder = ', '.join('?' for _ in tenses)
        ending_placeholder = ', '.join('?' for _ in endings)
        power_placeholder = ', '.join('?' for _ in powers)
        infinitive_placeholder = ', '.join('?' for _ in infinitives)
        query = f"""SELECT infinitive, tense, person, verb FROM Blad1
                    WHERE tense IN ({tense_placeholder})
                    AND ending IN ({ending_placeholder})
                    AND power IN ({power_placeholder})
                    AND infinitive IN ({infinitive_placeholder})"""
        with self.get_connection() as conn:
            c = conn.cursor()
            queried_entries = c.execute(query, tuple(chain.from_iterable((tenses, endings, powers, infinitives))))
            return queried_entries.fetchall()

    def get_verb(self, infinitive, tense):
        """
        Query for all conjugations of a certain verb

        Parameters
        ----------
        infinitive : queried infinitive
        tense : queried tense

        Returns
        -------
        names : list of verbs conforming to the parameters

        """
        with self.get_connection() as conn:
            c = conn.cursor()
            queried_names = c.execute("""SELECT person, verb FROM Blad1 WHERE infinitive = ? AND tense = ? """ , (infinitive, tense))
            names = queried_names.fetchall()
        return names