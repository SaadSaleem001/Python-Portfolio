alphabet='abcdefghijklmnopqrstuvwxyz'

def cesar_encode(message,offset):
    decoded_message=''
    for x in message:
        if x in alphabet:
            value =alphabet.find(x)
            decoded_message+=alphabet[(value-offset)%26]
        else:
            decoded_message+=x
    return decoded_message

encode_output= cesar_encode('xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!',10)   
print(encode_output)


alphabet='abcdefghijklmnopqrstuvwxyz'

def cesar_encode(message,offset):
    encode_message=''
    for x in message:
        if x in alphabet:
            value=alphabet.find(x)
            encode_message+=alphabet[(value-offset)%26]
        else:
            encode_message+=x
    return encode_message

encode_output=cesar_encode('xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!',-10)
print(encode_output)


