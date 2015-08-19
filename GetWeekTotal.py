__author__ = 'spotapov'

def Get_week_total(ws):

    for row in ws.rows:
        for cell in row:
            cell.value = str(cell.value)
            if cell.value == 'Week total:  ':
                                cn=cell.coordinate
    return (cn)