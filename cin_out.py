""""
clock in and clock out functions
module tha implements the clock in and clock out funcionality
"""
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

