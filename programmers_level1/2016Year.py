def solution(a, b):
    answer = ''
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    a = int(a)
    b = int(b)

    # if (2016 % 4 == 0 & 2016 % 100 != 0) | 2016 % 400 == 0:
    startDay = 'FRI'
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    temp = sum(month[:a - 1]) + (b - 1)
    temp += days.index(startDay)

    x = temp % len(days)

    return days[x]


solution(5, 24)

'''
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
return days[(sum(months[:a-1])+b-1)%7]
'''


'''
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

print(getDayName(5,24))
'''
