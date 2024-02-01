#cifrado fernet

from cryptography.fernet import Fernet


clave = "6dxE8KRlebH6PD_Y5FvUPcTCrqpW1UX92BIr0CFfYWw="

f = Fernet(clave)

token = "gAAAAABluwfhUf0JYgnSrMeMuqbMP61IOF9g1tYYr0VeCaMqr8UTVCFNJrthZW4O6GKsb3pEEDku43y0ZMQlPskVJ1VdkFyWWA=="




#Descifrar
des= f.decrypt(token)

print(des)