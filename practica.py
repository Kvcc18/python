import random
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

g = 2
p = 23

#Claves privadas aleatorias para Alice y Bob
private_key_A = random.getrandbits(256)
private_key_B = random.getrandbits(256)

#Simular el cambio de números entre Alice y Bob
public_key_A = pow(g, private_key_A, p)
public_key_B = pow(g, private_key_B, p)

#Clave secreta
secret_key_A = pow(public_key_B, private_key_A, p)
secret_key_B = pow(public_key_A, private_key_B, p)


print("Secret Key A:", secret_key_A)
print("Secret Key B:", secret_key_B)

#Checar si las claves secretas son iguales
if secret_key_A == secret_key_B:
    print("Las claves secretas son iguales.")
else:
    print("Las claves secretas NO son iguales.")

#Clave de Fernet utilizando la clave secreta
key = Fernet.generate_key()
cipher_suite = Fernet(key)
data = b"Message"
cipher_text = cipher_suite.encrypt(data)
plain_text = cipher_suite.decrypt(cipher_text)

#Checar que el mensaje cifrado y descifrado sea igual al original
assert plain_text == data
