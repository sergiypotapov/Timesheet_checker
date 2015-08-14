__author__ = 'spotapov'

def check_days(ws):
    days_result = []
    days = tuple(ws.iter_rows('E15:I15'))
    print("Checking days")
    for row in days:
        for cell in row:
            if cell.value > 8:
                days_result.append(str(cell.value)+"WARN")
                print("Warning: one or more Total Days are more than 8 ")
            else:
                days_result.append(cell.value)
            #print(days)
    return days_result
#check_days()