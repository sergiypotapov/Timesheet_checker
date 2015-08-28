__author__ = 'spotapov'

def check_days(ws,cn):

    cn = cn[1:]
    one_cn = 'E'+cn
    second_cn = ':I'+cn
    result_cn = one_cn+second_cn
    days = tuple(ws.iter_rows(result_cn))
    #print("Checking days")
    for row in days:
        for cell in row:
            cell.value = int(cell.value)
            if cell.value != None:
                if cell.value > 8:
                    error_trigger = "Warning: one or more Total Days are more than 8."
                else:
                    error_trigger = 'OK'
            else:
                print("No value here")
        if error_trigger != "Warning: one or more Total Days are more than 8.":
            error_trigger = "Days OK"
            #print(days)
    return error_trigger
#check_days()