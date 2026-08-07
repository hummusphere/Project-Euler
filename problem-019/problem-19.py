day = 7
month = 0
months = [31, {"leap": 29, "normal": 28}, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
counter = 0
year = 1900

def is_leap():
    if(month==1):
        if year%4==0 and (year%100!=0 or year%400==0):
            days = months[month]["leap"]
        else:
            days = months[month]["normal"] 
    else:
        days = months[month]
    return days

while(year<2001):
    day+=7

    days = is_leap()

    if (day>days):
        day-=days
        if (day==1 and year>1900 and year<2001):
            counter+=1
        month+=1
        if (month==12):
            month=0
            year+=1

print(counter)