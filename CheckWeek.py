__author__ = 'spotapov'

def Check_week(ws):
    week_result = []
    d15 = ws['D15'].value
    print("Checking week")

    if d15 > 40:
        week_result.append(str(d15)+"WARN")
        print("Warning: Week is more then 40!")
    else:
        week_result.append(d15)
        print("Seems Total Week hours are OK")
    return week_result
