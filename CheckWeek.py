__author__ = 'spotapov'
import TimeC

d15 = TimeC.ws['D15'].value
print(d15)

if d15 > 40:
        week_warning = True
        print("Warning: Week is more then 40!")
else:
        print("Week number is not bigger then 40 hours")

