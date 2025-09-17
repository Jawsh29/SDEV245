# This program utilizes the Caesar Cypher in order to encrypt user input messages, then decrypts the message

def encrypt_text(text, n):
    """Function used to encrypt message with Caesar Cypher"""
    ans = ""
    for ch in text:
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        elif ch.islower():
            ans += chr((ord(ch) + n - 97) % 26 + 97)
        else:
            ans += ch
    return ans


def decrypt_text(ciphertext, n):
    """Function used to decrypt message with reverse Caesar Cypher"""
    ans = ""
    for ch in ciphertext:
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) - n - 65) % 26 + 65)
        elif ch.islower():
            ans += chr((ord(ch) - n - 97) % 26 + 97)
        else:
            ans += ch
    return ans


message = input(str("Enter message you want to encrypt: "))
shift = int(input("Enter cypher shift: "))
enc_text = encrypt_text(message, shift)
print("Encrypted Text: " + enc_text)
print("Decrypted Text: " + decrypt_text(enc_text, shift))



