def isLeapYear(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    if year % 100 != 0 and year % 4 == 0:
        return True
    return False


years = list(range(1999, 2024))
total_days = 0
for year in years:
    total_days += 365
    if isLeapYear(year):
        total_days +=1

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysBetweenDates(y1, m1, d1,  y2, m2, d2):
    start_month = m1
    start_day = d1
    end_day = d2
    total_days = 0
    for year in range(y1, y2+1):
        end_month = 12
        start_month = 1

        if year == y2:
            end_month = m2
        if year == y1:
            start_month = m1
        for m in range(start_month, end_month+1):
            start_day = 1
            end_day = months[m - 1]
            if isLeapYear(year) and m == 2:
                end_day += 1
            if year == y1 and m == m1:
                start_day = d1
            if year == y2 and m == m2:
                end_day = d2
            total_days +=  end_day - start_day + 1
    print(total_days)

daysBetweenDates(2002, 2, 14, 2024, 2, 20)