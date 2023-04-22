import rsa
import os
import msvcrt

#********* Read Private & Public Keys **************
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

with open("publicKey_Richard.pem", "rb") as f:
    public_key_Richard = rsa.PublicKey.load_pkcs1(f.read())

# with open("publicKey_Sherifat.pem", "rb") as f:
#     public_key_Sherifat = rsa.PublicKey.load_pkcs1(f.read())
#********* Read Private & Public Keys **************


os.system('cls')
print("This is an interactive Script!")
username = input("Please enter your name: ")
os.system('cls')

#Loop to main menu
while True:
    print("\nWelcome " + username + "!")

    options = input("What would you like to do today? \n1. Send an Encrypted Message? \n2. Decrypt a message? \n3. Generate Keys \n4. Exit \n\nEnter options 1 - 4: ")

    #*****************Encrypt Msg***********************
    if options =="1":
        #os.system('cls')
        rname = input("\nEnter Recepient Name: \n1. Richard \n2. Sherifat \n3. Martins \n\nEnter any of the above names: ")
        emessage = input("\nEnter message: ")
        #os.system('cls')
        
        if rname =="Richard" or rname =="richard" or rname =="1":
            encrypted_message = rsa.encrypt(emessage.encode(), public_key_Richard)
            print("\nHere is your encrypted message below in quotes: ")
            print("----------------------------------------------------")
            print(encrypted_message)
            print("----------------------------------------------------")

            #Save encrypted message to file
            with open("Richard_encrypted.message", "wb") as f:
                f.write(encrypted_message)
                print("\nMessage saved!")

            #Waits for the user to press a key before continuing
            def press_any_key():
                print("Press any key to go back to the main menu...")
                msvcrt.getch()

            print("\n")
            # Call the press_any_key() function to wait for a key press
            press_any_key()
        
        elif rname =="Sherifat" or rname=="sherifat" or rname =="2":
            encrypted_message = rsa.encrypt(emessage.encode(), public_key_Sherifat)
            print("\nHere is your encrypted message below in quotes: ")
            print("----------------------------------------------------")
            print(encrypted_message)
            print("----------------------------------------------------")

            #Save encrypted message to file
            with open("Sherifat_encrypted.message", "wb") as f:
                f.write(encrypted_message)
                print("\nMessage saved!")
        
            #Waits for the user to press a key before continuing
            def press_any_key():
                print("Press any key to go back to the main menu...")
                msvcrt.getch()

            print("\n")
            # Call the press_any_key() function to wait for a key press
            press_any_key()

        else:
            encrypted_message = rsa.encrypt(emessage.encode(), public_key)
            print("\nHere is your encrypted message below in quotes: ")
            print("----------------------------------------------------")
            print(encrypted_message)
            print("----------------------------------------------------")
        
            #Save encrypted message to file
            with open("encrypted.message", "wb") as f:
                f.write(encrypted_message)
                print("\nMessage saved!")

        #Waits for the user to press a key before continuing
        def press_any_key():
            print("Press any key to go back to the main menu...")
            msvcrt.getch()

            print("\n")
            # Call the press_any_key() function to wait for a key press
            press_any_key()


    #********************Decrypt Msg*****************************        
    elif options == "2":

        while True:
            # Get the filename from the user
            print("\n")
            filename = input("Enter a filename: ")

            # Make sure the file exists and is a file (not a directory)
            if os.path.isfile(filename):
                # Read the contents of the file
                with open(filename, "rb") as file:
                    contents = file.read()
                clear_message = rsa.decrypt(contents, private_key)
                print("\n")
                print("Decrypted contents of", filename, ":")
                print("\n")
                print(clear_message.decode())

                #Waits for the user to press a key before continuing
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
        

#**************End of Decryption***************

    elif options == "3" or options == "Self":
        
        #********************Generate Keys*****************************
        public_key, private_key = rsa.newkeys(1024)

        with open("public.pem", "wb") as f: 
            f.write(public_key.save_pkcs1("PEM"))

        with open("private.pem", "wb") as f:
            f.write(private_key.save_pkcs1("PEM")) 
        print("Key generated Succesfully!")

    elif options == "4" or options == "Exit":
        #End of Main Loop
        # break
        exit()
        
        

    else:
        print("Error!!! You have entered a wrong number")
        # exit()