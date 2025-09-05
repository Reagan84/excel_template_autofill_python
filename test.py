def dateWithinRange(dateOne, dateTwo, dateToCheck): 
    dateLength = 3
    dateToVerify = dateToCheck.split('-')
    dateEarlier = dateOne.split('-')
    datePast = dateTwo.split('-')
    for i in range(dateLength):
        if int(dateEarlier[i]) > int(dateToVerify[i]) and int(datePast[i]) > int(dateToVerify[i]):
            return False
    return True
    

# date one is old, date two is new, final is to check
within = dateWithinRange("2013-06-14", "2011-01-06", "2002-12-07")
print(within)