alphabet='abcdefghijklmnopqrstuvwxyz'

def Vig_cipher(message,keyword):
    keyword_text=''
    keyword_index=0
    for i in message:
        if keyword_index >=len(keyword):
            keyword_index=0
        if i in alphabet:
            keyword_text+=keyword[keyword_index]
            keyword_index+=1
        else:
            keyword_text+=i

    decode_message=''
    for i in range(len(message)):
        if message[i] in alphabet:
            text_index=alphabet.find(message[i])
            offset_index=alphabet.find(keyword_text[i])
            new_text=alphabet[(text_index-offset_index)%26]
            decode_message+=new_text
        else:
            decode_message+=message[i]
    return decode_message

vig_message='barry in the spy'
vig_key='dog'

print(Vig_cipher(vig_message,vig_key))