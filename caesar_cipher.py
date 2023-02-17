import pyperclip

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    print("Do you want encrypt or decypt?")
    response=input('>').lower()
    if response.startswith('e'):
        mode='encrypt'
        break

    elif response.startswith('d'):
        mode='decrypt'
        break
while True:
    maxkey=len(SYMBOLS)-1
    print('please enter the key(0 to {}) to use.'.format(maxkey))
    response=input('>')
    if not response.isdigit():
        continue
    if 0<int(response)<maxkey:
        key=int(response)
        break

print('Enter your message')
message=input('>').upper()

translate=''

for symbol in message:
    if symbol in SYMBOLS:
        num=SYMBOLS.find(symbol)
        if mode=='encrypt':
            num=num+key
        else:
            num=num-key

        if num>maxkey:
            num=num-len(SYMBOLS)
        elif num<0:
            num=num+len(SYMBOLS)

        translate=translate+SYMBOLS[num]
    else:
        translate=translate+symbol

print(translate)