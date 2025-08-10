#module tha implements the clock in and cloc out funcionality
def clock_in():
    """" Records the clock in time """
    global clock_in_time
    clock_in_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Clocked In at: {clock_in_time}")

def clock_out():
    """" Records the clock out time """
    global clock_in_time
    clock_out_time = datetime.datetime.now()
    print(f"Clocked Out at: {clock_out_time.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_hours_worked():
    """ Calculates the hours worked based on clock in and clock out times """
    global clock_in_time
    if clock_in_time:
        hrs_worked = clock_out_time - datetime.datetime.strptime(clock_in_time, "%Y-%m-%d %H:%M:%S")
        hrs_worked = hrs_worked.total_seconds() / 3600  # Convert seconds to hours
        print(f"Hours worked: {hrs_worked:.2f} hours")
    else:
        print("Clock in time not recorded.")