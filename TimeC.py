__author__ = 'spotapov'
import openpyxl
import Checkdays
import CheckWeek
import os
import GetWeekTotal

# import all files from the location
file_list = os.listdir(r'D:\Psymetrix\Timesheets\\')
#print(file_list)
for file in file_list:
    if file.endswith('V11A.xlsx'):
        wb = openpyxl.load_workbook('D:\Psymetrix\Timesheets\\'+file, data_only=True)
        ws = wb.active
        print("\n")
        print(file)
        c = GetWeekTotal.Get_week_total(ws)
        #print(c)
        # print("Working with", file)
        a = Checkdays.check_days(ws,c)
        b = CheckWeek.Check_week(ws,c)
    # print("\n Results for days:\n",a,"\n","Results a week:\n",b)
    else:
        print(file, "Seems is not a Timesheet report")
