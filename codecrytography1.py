alphabet='abcdefghijklmnopqrstuvwxyz'

def cesar_decode(message,offset):
    decoded_message=''
    for x in message:
        if x in alphabet:
            value =alphabet.find(x)
            decoded_message+=alphabet[(value+offset)%26]
        else:
            decoded_message+=x
    return decoded_message

output= cesar_decode('xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!',10)   
print(output)

