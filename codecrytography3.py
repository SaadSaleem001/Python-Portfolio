alphabet='abcdefghijklmnopqrstuvwxyz'

def cesar_decode(message,decode):
    decoded_message=''
    for x in message:
        if x in alphabet:
            value =alphabet.find(x)
            decoded_message+=alphabet[(value+decode)%26]
        else:
            decoded_message+=x
    return decoded_message

y='vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
for i in range(1,26):
    print('offset',i)
    print(cesar_decode(y,i))


    