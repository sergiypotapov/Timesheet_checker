__author__ = 'spotapov'
import TimeC

days = tuple(TimeC.ws.iter_rows('E15:I15'))
for row in days:
    for cell in row:
        if cell.value > 8:
            day_warning = True
            print(cell.value, " - - Error")
        else:
            print(int(cell.value), str(" - - OK"))

#print(days.type)
#print(days)