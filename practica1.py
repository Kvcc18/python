
#importamos 
from Crypto.Util import number
import random 

#Ejercicio 1
print('Ejercicio 1 - Obtener numero aleatorio de 256 bits usando la función random', random.getrandbits(2056), '')

#Ejercicio 2
#Obten un numero primo 
i=0
while(True):
    i = i + i
    j = random.getrandbits(1024)
    esPrimo = number.isPrime(j)
    if(esPrimo):
        print("En la interacion: ", i,"se encontro el primo ", j, "\n")
        break

#Ejercicio 3
#Obtener inverso multiplicado
#La clave privada d es un numero que cumpla que e*d mod F = 1
#El inverso multiplicativo solo funciona si los dos numeros son primos entre si
def inversoMultiplicativo(x,y):
    print("Ejercicio 3 - El inverso multiplicativo del numerio x: ", "\n", x, "\n", "y el numero y: ",
           "\n", y, "\n", "es: ", "\n", number.inverse(x,y), "")
    
a = random.getrandbits(1024)
b = random.getrandbits(1024)

inversoMultiplicativo(a,b)
    
#Ejercicio 4
#Potencia de un numero 2*(e) mod p, donde "e" es un numero de 256 bits y "p" es un primo de 1024 bits
a = 2
b = random.getrandbits(256)
c = j

def potencia(x,y,z):
    print("Ejercicio 4 - La potencia de x a la mod 2 es: ", "\n", pow(x,y,z))
    


