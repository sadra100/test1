import random
NUM_DIGITS=3
MAX_GUESS=10
def main():
    secret=getSecretNum()
    num_guess=1
    while num_guess<MAX_GUESS:
        guess=''
        while len(guess)!=NUM_DIGITS or not guess.isdecimal():
            guess=input('<')
        clues=getclues(secret,guess)
        print(clues)
        num_guess+=1
    print(secret)
    print('Thank you for play!')
def getSecretNum():
    numbers=list('123456789')
    random.shuffle(numbers)
    secretNum=''
    for i in range(NUM_DIGITS):
        secretNum+=str(numbers[i])
    return secretNum
def getclues(secret,guess):
    if guess==secret:
        return 'Get you it '
    clues=[]
    for i in range(len(guess)):
        if guess[i]==secret[i]:
            clues.append('Fermi')
        elif guess[i] in secret:
            clues.append('Pico')
    if len(clues)==0:
            print('Bagle')
    else:
            clues.sort()
    return ''.join(clues)
if __name__=='__main__':
    main()