message =  input("Message Encryption:")
trans=''
i=len(message)-1
while i>=0:
    trans=trans+message[i]
    i=i-1

print(trans)
me=input('Message Decryption :')
te=""
iq=len(me)-1
while iq>=0:
    te+=me[iq]
    iq-=1

print(te)
