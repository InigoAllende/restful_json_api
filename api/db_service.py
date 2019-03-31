import sql_queries

import json
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
    with sqlite3.connect('metrics.db') as connection:
        cursor = connection.cursor()
        for item in data:
            query = (sql_queries.INSERT_METRIC % (data[item]['name'], data[item]['value'], data[item]['timestamp']))
            cursor.execute(query)

def get_all_data():
    """ returns all stored metrics """
    pass
