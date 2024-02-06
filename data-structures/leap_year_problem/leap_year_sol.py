###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    _year = year
    _month = month
    _day = (day + 1) % 31
    if _day == 0 :
        _day = 1
        _month = (month + 1) % 13
    if _month == 0:
        _month = 1
        _year += 1

    return (_year, _month, _day)

print(nextDay(1999, 12, 30))
print(nextDay(2013, 1, 30))
print(nextDay(2012, 12, 30))

#suggested solution
def nextDay(year, month, day):
    """
    Warning all months are 30days
    """
    if day < 30:
        return year, month, day+1
    else:
        if month < 12:
            return year, month+1,1
        else:
            return year+1, 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    year, month, day = year1, month1, day1
    nb = 0
    while (year, month, day) != (year2, month2, day2):
        (year, month, day) = nextDay(year, month, day)
        nb +=1
    # YOUR CODE HERE!
    return nb

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()
