__author__ = 'spotapov'

def CheckWeekNumberInFile(ws, week_n):
    week_number_in_file = ws['C1'].value
    if week_number_in_file == week_n:
        print("Week number in file corresponds to Curren Week Number")
    else:
        print("Warning: Week number in file", week_number_in_file, "Doesn't correspond to Current Week", week_n)
