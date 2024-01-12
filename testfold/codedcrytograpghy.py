alphabet='abcdefghijklmnopqrstuvwxyz'
message='xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

translated_messsage=''
for x in message:
    if x in alphabet:
        value=alphabet.find(x)
        translated_messsage+= alphabet[(value+10)%26]
    else:
        translated_messsage += x

print(translated_messsage)