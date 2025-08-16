from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

def Encrypt(text): return fernet.encrypt(bytes(text, 'utf-8'))
def Decrypt(text): return fernet.decrypt(text)

text = input("Enter text for encryption: ")

encrypted = Encrypt(text)

print("Encrypted Data\n", encrypted.decode())

print(Decrypt(encrypted).decode())