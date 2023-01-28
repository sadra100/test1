import random,datetime

def get_birthday(birthdaynum):
    for i in range(birthdaynum):
     birthdays=[]
     startdate=datetime.date(2001,1,1)
     randomNumberOfDay=datetime.timedelta(random.randit(0,364))
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