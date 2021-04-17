"""Se agrega el metodo "sleep()" para suspender el programa por unos segundos 
despues de un intento fallido, este tiempo va creciendo despues de cada intento fallido."""
import time
from time import sleep
CONTRASEÑA= "master$123"
n = 0
while n < 3:
    contra = input("Ingrese la contraseña: ")
    if contra == CONTRASEÑA:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta.")
        if n == 2:
            print("Supero la cantidad maxima de intentos.")
            break
        else:
            print("Quedan",2 - n,"intentos.")
            time.sleep(n+2)
            n = n + 1
        