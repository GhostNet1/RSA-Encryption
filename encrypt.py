import rsa

#-----------Read Keys--------------
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

#-----------End Read Keys---------------

#Encrypt Message
message = "This is my second python script"

encrypted_message = rsa.encrypt(message.encode(), public_key)

print(encrypted_message)

with open("encrypted.message", "wb") as f:
    f.write(encrypted_message)
