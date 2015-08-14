__author__ = 'spotapov'
import openpyxl
import Checkdays
import CheckWeek
wb = openpyxl.load_workbook('test.xlsx', data_only=True)
ws = wb.active
a = Checkdays.check_days(ws)
b = CheckWeek.Check_week(ws)
print("\n Results for days:\n",a,"\n","Results a week:\n",b)
