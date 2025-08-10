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


# clock in and clock out functions
#module tha implements the clock in and clock out funcionality
import datetime


class clockInOut:
    """ Class to handle clock in and clock out functionality """
    def __init__(self):
        """ Initializes the clock in and clock out times """
        self.clock_in_time = None
        self.clock_out_time = None

    def clock_in(self):
        """" Records the clock in time """
        clock_in_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Clocked In at: {clock_in_time}")
        return clock_in_time

    def clock_out(self):
        """" Records the clock out time """
        clock_out_time = datetime.datetime.now()
        print(f"Clocked Out at: {clock_out_time.strftime('%Y-%m-%d %H:%M:%S')}")
        return clock_out_time

    def calculate_hours_worked(self, clock_in_time, clock_out_time):
        """ Calculates the hours worked based on clock in and clock out times """
        if clock_in_time:
            hrs_worked = clock_out_time - datetime.datetime.strptime(clock_in_time, "%Y-%m-%d %H:%M:%S")
            hrs_worked = hrs_worked.total_seconds() / 3600  # Convert seconds to hours
            print(f"Hours worked: {hrs_worked:.2f} hours")
        else:
            print("Clock in time not recorded.")

