"""Database initialization."""
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as database:
    connection.executescript(database.read())

connection.commit()
connection.close()
