from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font


# Encoding Function
def encode(key, message):
    enc = []
    for i in range(len(message)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(message[i]) + ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Decoding Function
def decode(k, dkey, code):
    if k == dkey:
        dec = []
        enc = base64.urlsafe_b64decode(code).decode()
        for i in range(len(enc)):
            list_key = dkey[i % len(dkey)]
            list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)

            dec.append(list_dec)
        return "".join(dec)
    elif dkey != k:
        messagebox.showerror('CYPHER', 'INVALID SECRETE KEY. Try again.')
        return ""

# Function that executes on clicking Show Message function
def result():
    message = Message.get()
    k = key.get()
    i = mode.get()
    if i == 1:
        Output.set(encode(k, message))
    elif k == "" or message == "":
        messagebox.showinfo('CYPHER', 'Please fill the fields. Try again.')
    else:
        messagebox.showinfo('CYPHER', 'Please Choose Encryption. Try again.')


# Function that executes on clicking Reset function, resets all the input fields to blank
def reset():
    Message.set("")
    key.set("")
    mode.set(0)
    Output.set("")


def d_result():
    message2 = d_Message.get()
    k2 = d_key.get()
    k = key.get()
    i = mode.get()
    if i == 2:
        d_Output.set(decode(k, k2, message2))
    elif k2 == "" or message2 == "":
        messagebox.showinfo('CYPHER', 'Please fill the fields. Try again.')
    else:
        messagebox.showinfo('CYPHER', 'Please Choose Decryption . Try again.')


def d_reset():
    d_Message.set("")
    d_key.set("")
    mode.set(0)
    d_Output.set("")


window = Tk()
window.geometry("1300x500")
window.configure(bg='azure2')
window.title("Cypher")
window.iconbitmap(r"key.ico")

Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

d_Message = StringVar()
d_key = StringVar()
d_mode = IntVar()
d_Output = StringVar()

headingFrame1 = LabelFrame(window, bg="gray91", bd=5, text='Encrypt Message')
headingFrame1.grid(column=2, row=1, pady=10, padx=30)

#Header Text or section
headingLabel = Label(window, text="Symmetric Encryption and Decryption System",
                     font=('Open Sans', 20, 'bold'), padx=10, pady=10)
headingLabel.grid(column=0, row=0, columnspan=5, padx=40, pady=10)

label1 = Label(headingFrame1, text='Enter the Message', font=('Courier', 10, 'bold'))
label1.grid(column=1, row=3, padx=10, pady=10)

message = Entry(headingFrame1, textvariable=Message, width=35, font=('calibre', 10, 'normal'))
message.grid(column=2, row=3, padx=10, pady=10)

label2 = Label(headingFrame1, text='Enter Secret key', font=('Courier', 10, 'bold'))
label2.grid(column=1, row=4, padx=10, pady=10)

InputKey = Entry(headingFrame1, textvariable=key, width=35, font=('calibre', 10, 'normal'))
InputKey.grid(column=2, row=4, padx=10, pady=10)

label3 = Label(headingFrame1, text='Click the button to confirm ', font=('Courier', 10, 'bold'))
label3.grid(column=1, row=5, padx=10, pady=10)

Radiobutton(headingFrame1, text='YES Encrypt', variable=mode, value=1).grid(column=1, row=6, padx=5, pady=5)

label3 = Label(headingFrame1, text='Encrypted text', font=('Courier', 10, 'bold'))
label3.grid(column=1, row=8, padx=10, pady=10)

res = Entry(headingFrame1, textvariable=Output, width=35, font=('calibre', 10, 'normal'))
res.grid(column=2, row=8, padx=10, pady=10)

ShowBtn = Button(headingFrame1, text="Generate Ciphertext", bg='green', fg='black', width=15, height=1, command=result)
ShowBtn['font'] = font.Font(size=12)
ShowBtn.grid(column=2, row=9, padx=10, pady=10)

ResetBtn = Button(headingFrame1, text='Reset', bg='blue', fg='black', width=15, height=1, command=reset)
ResetBtn['font'] = font.Font(size=12)
ResetBtn.grid(column=1, row=9, padx=10, pady=10)


# Decipher Section
decipher = LabelFrame(window, text='Decipher', bd=5)
decipher.grid(column=4, row=1, padx=10, pady=10)

d_label1 = Label(decipher, text='Enter the Ciphertext', font=('Courier', 10, 'bold'))
d_label1.grid(column=4, row=3, padx=10, pady=10)

d_message = Entry(decipher, textvariable=d_Message, width=35, font=('calibre', 10, 'normal'))
d_message.grid(column=5, row=3, padx=10, pady=10)

d_label2 = Label(decipher, text='Enter Private key', font=('Courier', 10, 'bold'))
d_label2.grid(column=4, row=4, padx=10, pady=10)

dInputKey = Entry(decipher, textvariable=d_key, width=35, font=('calibre', 10, 'normal'))
dInputKey.grid(column=5, row=4, padx=10, pady=10)

d_label3 = Label(decipher, text='Click the button to confirm', font=('Courier', 10, 'bold'))
d_label3.grid(column=4, row=5, padx=10, pady=10)

Radiobutton(decipher, text='Decrypt', variable=mode, value=2).grid(column=4, row=7, padx=5, pady=5)

d_label3 = Label(decipher, text='Plain text', font=('Courier', 10, 'bold'))
d_label3.grid(column=4, row=8, padx=10, pady=10)

d_res = Entry(decipher, textvariable=d_Output, width=35, font=('calibre', 10, 'normal'))
d_res.grid(column=5, row=8, padx=10, pady=10)

d_showBtn = Button(decipher, text="Generate Message", bg='green', fg='black', width=15, height=1, command=d_result)
d_showBtn['font'] = font.Font(size=12)
d_showBtn.grid(column=5, row=9, padx=10, pady=10)

d_resetBtn = Button(decipher, text='Reset', bg='blue', fg='black', width=15, height=1, command=d_reset)
d_resetBtn['font'] = font.Font(size=12)
d_resetBtn.grid(column=4, row=9, padx=10, pady=10)

QuitBtn = Button(window, text='Exit', bg='red', fg='black', width=15, height=1, command=window.destroy)
QuitBtn['font'] = font.Font(size=12)
QuitBtn.grid(column=3, row=4)

window.mainloop()
