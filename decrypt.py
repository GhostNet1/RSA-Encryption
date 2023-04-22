import rsa
import os
import msvcrt

#---------Read Private Key----------------------
with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
#End Read Keys

while True:
    # Get the filename from the user
    filename = input("Enter a filename: ")

    # Make sure the file exists and is a file (not a directory)
    if os.path.isfile(filename):
        # Read the contents of the file
        with open(filename, "rb") as file:
            contents = file.read()
        clear_message = rsa.decrypt(contents, private_key)
        print("Decrypted contents of", filename, ":")
        print(clear_message.decode())

        def press_any_key():
            
            print("Press any key to go back to the main menu...")
            msvcrt.getch()

        print("\n")
        # Call the press_any_key() function to wait for a key press
        press_any_key()

        # This line of code will only execute after the user has pressed a key
        print("Continuing...")
        print("\n")

        # Exit the loop, since we found a valid file
        break
    else:
        print("Error: file", filename, "does not exist or is not a file.")
        print("\n")

    
    




    #Decrypt Message
""" encrypted_message = open("encrypted.message", "rb").read()

clear_message = rsa.decrypt(encrypted_message, private_key)

print(clear_message.decode()) """
