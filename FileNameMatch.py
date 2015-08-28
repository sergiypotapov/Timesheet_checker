__author__ = 'spotapov'
from fnmatch import fnmatch
import re
patern = 'LUXOFT_URTDSM_timesheet_[0-9]*_2015_*_*V11A.xlsx'
def CheckFileNameMatch(file, week_n):

    if fnmatch(file, patern):
        week_in_file = re.findall(r'\d+',file)
        week_in_file = week_in_file[0]
        if week_in_file == week_n:
            error_triger = "File name OK"
        else:
            error_triger="Warning: File Name is wrong"
    else:
        error_triger="Warning: File Name is wrong"
    return error_triger


    #print(patern)

#CheckFileNameMatch('LUXOFT_URTDSM_timesheet_10_2015_Denys_LebedevV11A.xlsx', 35)