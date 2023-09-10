import random,sys

JAPANIES_NUMBER={1:'ICHI',2:'NI',3:'SAN',4:'SHI ',5:'GO',6:'ROKU'}
purse=5000
while True:
    print('You have',purse,'mon how you much or do you bet?(QUIT) ')
    while True:
        pot=input('>')
        if pot.upper()=='QUIT':
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number')
        elif int(pot)<purse:
            print('You have not enough to make that bet')
        else:
            pot=int(pot)
            break
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
