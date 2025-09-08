# This Program utilizes symmetrical encryption through the Fernet Cypher in order to encrypt and decrypt a message

from cryptography.fernet import Fernet


message = input("Enter message: ")

key = Fernet.generate_key()

crypt_key = Fernet(key)

encrypted_message = crypt_key.encrypt(message.encode())

print(f"Encrypted message: {encrypted_message}")

original_message = crypt_key.decrypt(encrypted_message).decode('utf-8')

print(f"Original message: {original_message}")

print("Encryption Success")