import sql_queries

import sqlite3

from sqlite3 import Error

def initialize_db():
    """ create a database connection to a SQLite database """
    try:
        connection = sqlite3.connect('metrics.db')
        _initialize_tables(connection)
    except Error as e:
        print('An error occurred %s', e)
        return e

def _initialize_tables(connection):
    """ Creates database tables if they do not exist """
    with connection:
        c = connection.cursor()
        c.execute(sql_queries.CREATE_TABLE)

def insert_metrics(data):
    """ perform a db INSERT """
    pass

def get_all_data():
    """ returns all stored metrics """
    pass