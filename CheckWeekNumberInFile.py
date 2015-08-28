__author__ = 'spotapov'

def CheckWeekNumberInFile(ws, week_n):
    week_number_in_file = ws['C1'].value
    if week_number_in_file == week_n:
        error_trigger="Week number in file OK"
    else:
        error_trigger= "Warning: Week number in file doesn't correspond to Current Week"
    return error_trigger
