__author__ = 'spotapov'

import isoweek
def GetCurrentWeekNuber():

    todays_week = isoweek.Week.thisweek()
    todays_week = str(todays_week)

    week_split = todays_week.split('W')
    #print(week_split)
    week_n = week_split[1]
    print(week_n)

    return week_n
GetCurrentWeekNuber()