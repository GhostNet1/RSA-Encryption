import rsa

# Generate a new RSA key pair
(pubkey, privkey) = rsa.newkeys(512)

# Share the public key with the recipient
recipient_pubkey = pubkey

# Encrypt the shared key using the recipient's public key
shared_key = b"secret key"
encrypted_key = rsa.encrypt(shared_key, recipient_pubkey)

# Send the encrypted key to the recipient
print(encrypted_key)

# The recipient can then decrypt the key using their private key
decrypted_key = rsa.decrypt(encrypted_key, privkey)
print(decrypted_key.decode())
