"""Genera un numero aleatorio y el usuario debe ingresar numeros hasta adivinarlo,
el programa devuelve pistas de si el numero es mayor o menos y permite rendirse cada 5 intentos."""
import random   
from random import randrange

x=(random.randrange(50))

num = 0
intentos=0
rendirse = ""
while not num == x:
   
   
    num = input("Ingrese un numero: ")
    if num.isdigit()== True:
        num = int(num)
        if intentos == 0 and num == x :
            print("SOS UN GENIO, LE PEGASTE A LA PRIMERA")
            break
        elif num > x:
            intentos += 1
            print("El numero es mas chico.")
            
        elif num < x:
            intentos += 1
            print ("El numero es mas grande.")
            
        elif num == x:
            print(f"Le pegaste en {intentos + 1} intentos")
            intentos = 0
            break
    elif num.isdigit() == False:
        print("Solo se pueden ingresar numeros enteros!!!")
        
    if intentos == 5:
        while not rendirse == "si" or rendirse == "no":
            rendirse=input("Te rendis? (si/no) ".lower())
            if rendirse == "si":
                print("El numero era:", x)
                break
            if rendirse == "no":
                print("Suerte!")
                break
            else:
                print("Ingrese si o no.")

    if rendirse == "si":
        break