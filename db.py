""" 
Contains the database connection and session management 
for the application. 
"""
import datetime
import sqlite3


def get_db_connection():
    """ Establishes a connection to the SQLite database."""
    # Create Database or Connect to one
    conn = sqlite3.connect('app.db')

    # Create a Cursor (to execute SQL commands)
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute(""" CREATE TABLE if not exists hours(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                clock_in_time TEXT,
                clock_out_time TEXT,
                hours_worked REAL)
            """)

    # commit the changes
    conn.commit()

    # Close the connection
    conn.close()

def add_record(date, clock_in_time, clock_out_time, hours_worked):
    """ Adds a record of clock in and clock out times to the database. """
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO hours (date, clock_in_time, clock_out_time, hours_worked) VALUES (?, ?, ?, ?)",
              (date, clock_in_time, clock_out_time, hours_worked))
    
    conn.commit()
    conn.close()

def get_records(period_start, period_end):
    """ Retrieves hours worked records for a specific period."""
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM hours where date BETWEEN ? AND ?", (period_start, period_end))
    records = c.fetchall()
    
    conn.close()
    return records

