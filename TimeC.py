__author__ = 'spotapov'
import openpyxl

wb = openpyxl.load_workbook('test.xlsx', data_only=True)
ws = wb.active