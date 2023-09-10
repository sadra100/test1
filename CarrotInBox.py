import random

input('Press Enter to begin...')
p1=input('Human player 1 Enter your name:')
p2=input('Human player 2 Enter your name:')
playerNames=p1[:11].center(11)+'     '+p2[:11].center(11)
print('''HERE ARE TWO BOXES:
    __________    __________
  /          /| /          /|
  +---------+ | +---------+ |
  | RED     | | | GOLD    | |
  | BOX     | / | BOX     | /
  +---------+/  +---------+/ ''')
print()
print(playerNames)
print()
print(p1+'you have a red box in front of you')
print(p2+'you have a gold box in front of you')
print()
print(p1+',you will get to look into your box.')
print(p2.upper()+',clos your eyes and don\'t look!!!')
input('when'+p2+'has closed their eyes press ENTER....')
print()
print(p1+'here is insid your box:')
if random.randint(1,2)==1:
    Carrotinbox=True
else:
    Carrotinbox=False

if Carrotinbox:
    print('''
        ___VV_____
       |   VV     |
       |   VV     |
       |___||____-|  ___________
      /    ||    /| /          /|
      +---------+ | +---------+ |
      |     RED | | |    GOLD | |
      |     BOX | / |     BOX | /
      +---------+/  +---------+/
      (carrot!)''')
    print(playerNames)
else:
    print('''
        _________
       |         |
       |         |
       |_________|    __________
      /          /| /          /|
      +---------+ | +---------+ |
      | RED     | | | GOLD    | |
      | BOX     | / | BOX     | /
      +---------+/  +---------+/
      (no carrot!)''')
    print(playerNames)
input('Press ENTER for continue...')
print('\n'*100)
print(p1+',tell'+p2+'to open their eyes')
input('Press ENTER to continue')
print()
print(p2+'do you want swap boxes with?'+p1+'YES/NO')
while True:
    response=input('>').upper()
    if not (response.startswith('Y')or response.startswith('N')):
        print(p2+'please enter YES or NO')
    else:
        break
firstbox='RED'
secondbox='GOLD'
if response.startswith('Y'):
    Carrotinbox=not Carrotinbox
    firstbox ,secondbox=secondbox,firstbox
print('''HERE ARE THE TWO BOXES:
  ___________   ___________
 /          /| /          /|
 +---------+ | +---------+ |
 | {}      | | | {}      | |
 | BOX     | / | BOX     | /
 +---------+/  +---------+/'''.format(firstbox, secondbox))
print(playerNames)
print('Press ENTER to reveal winner')
print()
if Carrotinbox:
    print('''
     ___ VV______  ____________
     |   VV      | |           |
     |   VV      | |           |
     |___||____  | |___________|
     /   ||    / | /          /|
     +---------+ | +---------+ |
     | {}      | | | {}      | |
     | BOX     | / | BOX     | /
     +---------+/  +---------+/'''.format(firstbox, secondbox))
else:
    print('''
        _________   ___VV______
      |          | |   VV      |
      |          | |   VV      |
      |__________| |___||______|
     /          /| /   ||    / |
     +---------+ | +---------+ |
     | {}      | | | {}      | |
     | BOX     | / | BOX     | /
     +---------+/  +---------+/'''.format(firstbox, secondbox))

    print()

if Carrotinbox:
    print(p1+'is the winner')
else:
    print(p2+'is the winner')
