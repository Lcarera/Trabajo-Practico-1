import time
from time import sleep
CONTRASEÑA= "master$123"
n = 0
def comprobarContra(contra):
    if contra == CONTRASEÑA:
        return 1
    else: 
        return 0

while n < 3:
    contra = input("Ingrese la contraseña: ")
    if comprobarContra(contra) == 1:
        print("Contraseña correcta.")
        break
    elif comprobarContra(contra) == 0:
        print("Contraseña incorrecta.")
        if n == 2:
            print("Supero la cantidad maxima de intentos.")
            break
        else:
            print("Quedan",2 - n,"intentos.")
            time.sleep(n+2)
            n = n + 1
        