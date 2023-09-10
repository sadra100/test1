import datetime


DAYS=('Sunday','Monday','Thursday','Wedenseday','Tuseday','Friday','Saturday')
MONTH=('January','February','March','April','May','June','Jully','August','September','October','November','December')

while True:
    print('Please enter the year')
    response=input('>')
    if response.isdecimal() and int(response)>0:
        year=int(response)
        break
    print('Please enter numeric year')
    continue

while True:
    print('Please enter a month')
    response=input('>')
    if not response.isdecimal():
        print("Please enter a numeric month")
        continue
    month=int(response)
    if 1<=month<=12:
        break
    print('Please enter number in range 1 to 12')

def getCalenderFor(month,year):
    calText=''
    calText+=(' '*34)+MONTH[month-1]+''+str(year)+'\n'
    calText+='...Sunday.....Monday.....Thursday.....Wedensday.....Tusday.....Friday.....Saturday..\n'
    weekSeparator=('+----------'*7)+'+\n'
    blankRow=('|         '*7)+'+\n'
    currentDate=datetime.date(year,month,1)
    while currentDate.weekday()!=6:
        currentDate-=datetime.timedelta(days=1)
    while True:
        calText+=weekSeparator
        dayNumRow=''
        for i in range(7):
            dayNumLable=str(currentDate.day).rjust(2)
            dayNumRow+='|'+dayNumLable+(' '*8)
            currentDate+=datetime.timedelta(days=1)
        dayNumRow+='|\n'
        calText+=dayNumRow
        for i in range(3):
            calText+=blankRow
        if currentDate.month!=month:
            break
    calText+=weekSeparator
    return calText
caltext=getCalenderFor(month,year)
print(caltext)
calenderFilename='calender_{}_{}.text'.format(year,month)
with open(calenderFilename,'w') as file0bj:
 file0bj.write(caltext)
print('Saved to'+calenderFilename)
