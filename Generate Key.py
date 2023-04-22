import rsa

# Generate a new RSA key pair
public_key, private_key = rsa.newkeys(1024)

# Save public key
with open("publicKey_Sherifat.pem", "wb") as f: 
    f.write(public_key.save_pkcs1("PEM"))

# Save private key
with open("privateKey_Sherifat.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM")) 
