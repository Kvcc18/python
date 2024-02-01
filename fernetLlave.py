from cryptography.fernet import Fernet

#ALICE
key = Fernet.generate_key()

print('LLAVE: ', key)
f = Fernet(key)
token = f.encrypt(b"Mi mensaje")

#BOB
d = Fernet(key)
print("MENSAJE: ", d.decrypt(token))