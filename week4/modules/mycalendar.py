import sys

locations = sys.path
for i in locations:
    print(i)

import calendar
leapdays = calendar.leapdays(2000, 2100)
print(leapdays)
isitleap = calendar.isleap(2036)
print(isitleap)