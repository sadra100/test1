import random,datetime

def get_birthday(birthdaynum):
    birthdays = []

    for i in range(birthdaynum):
     startdate=datetime.date(2001,1,1)
     randomNumberOfDay=datetime.timedelta(random.randint(0,364))
     birthday=startdate+randomNumberOfDay
     birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    if len(birthdays)==len(set(birthdays)):
        return None
    for i,birthdayA in enumerate(birthdays):
        for j,birthdayB in enumerate(birthdays[i+1:]):
            if birthdayA==birthdayB:
                return birthdayA

MONTH=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

while True:
    print("How many shall i generated birthday(Max 100)?")
    respons=(input('>'))
    if respons.isdecimal() and (0 < int(respons)< 100):
        numBDays=int(respons)
        break

print("Here are {} birthdays".format(numBDays))
birthdays=get_birthday(numBDays)
for i,birthday in enumerate(birthdays):
    if i !=0:
        print(',',end='')
    Month_name=MONTH[birthday.month-1]
    dateText= '{} {}'.format(Month_name,birthday.day)
    print(dateText)
print()
print()

match=get_match(birthdays)
if match!=None:
    monthname=MONTH[match.month-1]
    dateText='{} {}'.format(monthname,match.day)
    print('{} people have birthday on'.format(dateText))
else:
    print("there are no matching birthday")
print()

print('generating',numBDays,'100000 times...')

simMatch=0
for i in range(100_000):
    if i%10000==0:
        print('{}simulation run...'.format(i))
    birthday=get_birthday(numBDays)
    if get_match(birthday)!=None:
        simMatch=simMatch+1

probability=round(simMatch/100_000*100,2)
print(numBDays,'people have',probability,'chance of matching birthdays')