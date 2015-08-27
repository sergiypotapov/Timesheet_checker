__author__ = 'spotapov'

def Check_week(ws,cn):
    week_result = []
    ncn = cn[1:]
    cn = 'D'+ncn
#TODO make human readable variable
    d15 = ws[cn].value
    d15 = int(d15)
    #print("Checking week")
    if d15 != None:
        if d15 > 40:
            print("Warning: Week is more then 40! Value is ", d15)
            error_trigger = 'Warning'
        else:
            print("Week OK - ", d15 )
            error_trigger = 'OK'
    return error_trigger
