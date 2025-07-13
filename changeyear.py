day=int(input('enter the day'))
month=int(input('enter the month'))
year=int(input('enter the year'))

def changeyear(day,month,year):
    if month>10 or day>10 and month==10:
        date=year+622
    else:
        date=year+621
    print(date)
  
changeyear(day,month,year)
    