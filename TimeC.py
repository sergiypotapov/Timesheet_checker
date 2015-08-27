__author__ = 'spotapov'
import openpyxl
import Checkdays
import CheckWeek
import os
import GetWeekTotal
import FileNameMatch
import GetCurrentWeekNumber

#TODO HTML report
#TODO math WK number in file (from date library)
#TODO WBS code corresponds to indicated Phase
#TODO Check if someone forgot to send a file
#TODO mnake executable artifact
#TODO give a parameter "path to reports" to executable file


# import all files from the location
dir = 'D:\\Test\\'
file_list = os.listdir(dir)

# getting current week number
week_n = GetCurrentWeekNumber.GetCurrentWeekNuber()

for file in file_list:
    #if file.endswith('V11A.xlsx'):
        wb = openpyxl.load_workbook(dir+file, data_only=True)
        ws = wb.active
        print("\n")
        print(file)

        c = GetWeekTotal.Get_week_total(ws)
        d = FileNameMatch.CheckFileNameMatch(file,week_n)
        #print(c)
        # print("Working with", file)
        #TODO make human readable variables
        a = Checkdays.check_days(ws,c)
        b = CheckWeek.Check_week(ws,c)
    # print("\n Results for days:\n",a,"\n","Results a week:\n",b)
    #else:
        #print(file, "Seems is not a Timesheet report")
