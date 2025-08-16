# Cryptography Program
# V1.2
import tkinter as tk
from tkinter import *
from tkinter import ttk
from cryptography.fernet import Fernet

#Encryption Variables
key = Fernet.generate_key()
fernet = Fernet(key)

#Root
root = Tk()
root.title("Crypto Program (Fernet)")

#Frames
frm = Frame(root)
frm.grid(row=0, column=0)

inputFrame = Frame(frm)
inputFrame.grid(row=0,column=0)

buttonFrame = Frame(frm)
buttonFrame.grid(row=1,column=0)

#Initialize GUI Elements
#Labels
inputTextLabel = Label(inputFrame, text="INPUT TEXT:")
encryptedTextLabel = Label(inputFrame, text="ENCRYPTED/DECRYPTED TEXT:")

#Text Fields
inputTextField = Entry(inputFrame, width=107)
encryptedTextField = Text(inputFrame, width=80, height=4)

#Encryption Methods
def Encrypt(): 
    text = inputTextField.get()
    encryptedTextField.delete(1.0, tk.END)
    encryptedTextField.insert(tk.END, fernet.encrypt(bytes(text, 'utf-8')))

def Decrypt():
    text = inputTextField.get()
    encryptedTextField.delete(1.0, tk.END)
    encryptedTextField.insert(tk.END, fernet.decrypt(text))

#Buttons
encryptButton = Button(buttonFrame, text="Encrypt", command=Encrypt)
decryptButton = Button(buttonFrame, text="Decrypt", command=Decrypt)
quitButton = Button(buttonFrame, text="Quit", command=quit)



#Add GUI Elements to Grid
#Add Buttons
encryptButton.grid(column=0, row=0, padx=10, pady=10)
decryptButton.grid(column=1, row=0, padx=10, pady=10)
quitButton.grid(column=2, row=0, padx=10, pady=10)

#Add Label
inputTextLabel.grid(column=0, row=0, padx=10, pady=10)
encryptedTextLabel.grid(column=0, row=1, padx=10, pady=10)

#Add Fields
inputTextField.grid(column=1, row=0, padx=10)
encryptedTextField.grid(column=1, row=1, padx=10)

root.mainloop()