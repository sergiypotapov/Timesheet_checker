__author__ = 'spotapov'
import openpyxl
import Checkdays
import CheckWeek
import os
import GetWeekTotal
import FileNameMatch
import GetCurrentWeekNumber
import CheckWeekNumberInFile
import sys

#TODO HTML report
#TODO WBS code corresponds to indicated Phase
#TODO Check if someone forgot to send a file

result = []
def RunTests(arg1):

# import all files from the location
    dir = arg1
    #dir = sys.argv[1]
    file_list = os.listdir(dir)

# getting current week number
    week_n = GetCurrentWeekNumber.GetCurrentWeekNuber()

    for file in file_list:
    #if file.endswith('V11A.xlsx'):
        wb = openpyxl.load_workbook(dir+file, data_only=True)
        ws = wb.active
        print("\n")
        print(file)
        e = CheckWeekNumberInFile.CheckWeekNumberInFile(ws, week_n)
        c = GetWeekTotal.Get_week_total(ws)
        d = FileNameMatch.CheckFileNameMatch(file,week_n)

                #TODO make human readable variables
        a = Checkdays.check_days(ws,c)
        b = CheckWeek.Check_week(ws,c)
        pre_result = [file,a,b,d,e]
        result.append(pre_result)
        print(result)
    # print("\n Results for days:\n",a,"\n","Results a week:\n",b)
    #else:
        #print(file, "Seems is not a Timesheet report")
    return result, week_n
# if __name__ == "__main__":
#     RunTests(sys.argv[1])
# def hi ():
#     a = [1,2,3]
#     return a