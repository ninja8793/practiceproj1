import cryptography
from cryptography.fernet import Fernet

'''
key = Fernet.generate_key()
print("Original key:",key)


#write key into file...........................
print(".....................File write successfully into file.............................")
file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()

#read key from file............................
file = open('key.key', 'rb')
print("Read from file:",file.read())
file.close()


password_provided = "password" # This is input in the form of a string
password = password_provided.encode()
print('Byte:',password)

'''

print("Encrypyion of message..........................................")
key = Fernet.generate_key()
print("Original key:",key)
message = "my deep dark secret".encode()

f = Fernet(key)
encrypted = f.encrypt(message)
print("Original Message:",message)
print("Encrypted msg:",encrypted)

print("\n\nDecryption of message............................................")
f = Fernet(key)
dencrypted = f.decrypt(encrypted)
print("Dencrypted msg:",dencrypted)
