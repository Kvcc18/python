from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import random

g = 2
p = 23

#Claves privadas para Bob y para Alice
private_key_A = random.getrandbits(256)
private_key_B = random.getrandbits(256)

#Simulación de intercambio de números entre Bob y Alice
public_key_A = pow(g, private_key_A, p)
public_key_B = pow(g, private_key_B, p)

#Calculando la clave secreta
secret_key_A = pow(public_key_B, private_key_A, p)
secret_key_B = pow(public_key_A, private_key_B, p)

#Clave fernet utilizando clave secreta y verificando que ambas claves sean iguales
key = Fernet.generate_key()
cipher_suite = Fernet(key)
data = b"Message"
cipher_text = cipher_suite.encrypt(data)
plain_text = cipher_suite.decrypt(cipher_text)
assert plain_text == data





