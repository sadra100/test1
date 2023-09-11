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
        elif int(pot)>purse:
            print('You have not enough to make that bet')
        else:
            pot=int(pot)
            break
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print(' CHO (even) or HAN (odd)?')
    while True :
        bet=input('>').upper()
        if bet!='CHO' and bet!='HAN':
            print('Please enter either CHO or HAN')
            continue
        else:
            break
    print('The dealer lifts the cup to reveal')
    print(' ',JAPANIES_NUMBER[dice1],'-',JAPANIES_NUMBER[dice2])
    print('   ',dice1,'-',dice2)
    rollIsEven=(dice1+dice2)%2==0
    if rollIsEven:
        correctBet='CHO'
    else:
        correctBet='HAN'
    playerWon=bet==correctBet
    if playerWon:
        print('you won ,you take',pot,'mon.')
        purse=purse+pot
        print('The house collect a',pot//10,'mon fee.')
    else:
        purse=purse-(pot//10)
        print('You lost')
    if purse==0:
        print('You have run out of money!')
        print('Thank you')
        sys.exit()