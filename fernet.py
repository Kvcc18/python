#Cifrado Fernet

#Importamos fernet
from cryptography.fernet import Fernet

#Generamos la clave
clave = Fernet.generate_key()

#Creamos la instancia de fernet
f = Fernet(clave)

#Encriptamos el mensaje
token = f.encrypt(b'Otaku de closet')

print(token)
print(clave)

#Decifrar
des = f.decrypt(token)

print(des)