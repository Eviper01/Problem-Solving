def isLeap(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False


def DaysofMonth(year,month):
    monthindex = month-1
    MonthsDays = [31,"error",31,30,31,30,31,31,30,31,30,31]
    if monthindex==1:
        if isLeap(year):
            return 29
        else:
            return 28
    else:
        return MonthsDays[monthindex]

#monday is 1
#sunday is 0
start = 2 #1901 starts on tuesday
total = 0

for year in range(1901,2001):
    for month in range(1,13):
        if start==0:
            total+=1
        start += DaysofMonth(year,month)%7
        start = start%7

print(total)
