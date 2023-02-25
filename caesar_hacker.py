
print("Enter your message")
message=input('>')
SYMBOL='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOL)):
    translated=''
    for symbol in message:
        if symbol in SYMBOL:
            num=SYMBOL.find(symbol)
            num=num-key
            if num<0:
                num=num+len(SYMBOL)
            translated=translated+SYMBOL[num]
        else:
            translated=translated+symbol
    print('key #{}:{}'.format(key,translated))