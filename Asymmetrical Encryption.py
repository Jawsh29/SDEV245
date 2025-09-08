# This program utilizes asymmetrical encryption to code and decode massages.
# A public and private key were generated to be used in this program (private_key.pem and public _key.pem)

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Open private Key
with open('private_key.pem', 'rb') as file:
    private_key = serialization.load_pem_private_key(
        file.read(),
        password=None,
        backend=default_backend()
    )

# Open public Key
with open('public_key.pem', 'rb') as file:
    public_key = serialization.load_pem_public_key(
        file.read(),
        backend=default_backend(),
    )

# Enter Message
message = input('Enter message: ').encode('utf-8')

# Encrypt Message
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f'Encrypted Message : {encrypted_message}')

# Decrypt Message
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f'Decrypted Message : {decrypted_message}')