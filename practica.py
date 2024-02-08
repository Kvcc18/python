import random
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

g = 2
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF

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
    print("Las claves secretas SI son iguales.")
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
