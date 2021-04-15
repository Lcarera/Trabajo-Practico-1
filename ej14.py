# 14. Mastermind: Cada vez que se empieza un partido, el programa debe “eligir” un número de
# cuatro cifras (sin cifras repetidas), que será el código que el jugador debe adivinar en la
# menor cantidad de intentos posibles. Cada intento consiste en una propuesta de un código
# posible que tipea el jugador, y una respuesta del programa. Las respuestas le darán pistas al
# jugador para que pueda deducir el código.
# Estas pistas indican cuán cerca estuvo el número propuesto de la solución a través de dos
# valores: la cantidad de aciertos es la cantidad de dígitos que propuso el jugador que también
# están en el código en la misma posición. La cantidad de coincidencias es la cantidad de
# digitos que propuso el jugador que también están en el código pero en una posición distinta.
# Por ejemplo, si el código que eligió el programa es el 2607, y el jugador propone el 1406, el
# programa le debe responder un acierto (el 0, que está en el código original en el mismo
# lugar, el tercero), y una coincidencia (el 6, que también está en el código original, pero en la
# segunda posición, no en el cuarto como fue propuesto). Si el jugador hubiera propuesto el
# 3591, habría obtenido como respuesta ningún acierto y ninguna coincidencia, ya que no hay
# números en común con el código original, y si se obtienen cuatro aciertos es porque el
# jugador adivinó el código y ganó el juego.
# El programa, entonces, debe generar un número que el jugador no pueda predecir. A
# continuación, debe pedirle al usuario que introduzca un número de cuatro cifras distintas, y
# cuando éste lo ingresa, procesar la propuesta y evaluar el número de aciertos y de
# coincidencias que tiene de acuerdo al código elegido. Si es el código original, se termina el
# programa con un mensaje de felicitación. En caso contrario, se informa al jugador la
# cantidad de aciertos y la de coincidencias, y se le pide una nueva propuesta. Este proceso se
# repite hasta que el jugador adivine el código.

import random
from random import randrange

def validarNumero(numero):
    numero= str(numero)
    if numero.isdigit():

        if(len(numero) == 4):

            return(numero[0:1] != numero[1:2]
            and numero[0:1] != numero[2:3]
            and numero[0:1] != numero[3:4]
            and numero[1:2] != numero[2:3]
            and numero[1:2] != numero[3:4]
            and numero[2:3] != numero[3:4])
        else:
            return False
    else:
        return False

def generarCodigo():
    codigo = 0
    while not validarNumero(codigo):
        codigo = randrange(10000)
    return codigo

def compararCodigo(codigo,numero):
    return str(codigo) == str(numero)

def pedirNumero(numero):
    while not validarNumero(numero):
        print("Ingrese un numero valido")
        numero = input("Ingrese un numero de cuatro cifras que no se repitan: ")
    return numero


def Comenzar():
    nuevoCodigo = generarCodigo()
    print("""
    REGLAS:
    Al comenzar el juego se generara un codigo de 4 cifras distintas.
    Se debe ingresar otro numeor de 4 cifras distintas.
    Si un numero coincide y esta en la misma posicion cuenta como acierto.
    Si un numero coincide pero esta en otra posicion cuenta como coincidencia.

    """)
    numero = pedirNumero(input
    ("Ingrese un numero de cuatro cifras que no se repitan: "))

    while not compararCodigo(numero,nuevoCodigo):
        aciertos = 0
        coincidencias = 0

        num= str(numero)
        cod= str(nuevoCodigo)
        print(cod)
        for i in range(1,5):

            if(num[i-1:i] == cod[i-1:i]):
                aciertos +=1
    
            elif(num[i-1:i] == cod[1:2] or num[i-1:i] == cod[2:3] or num[i-1:i] == cod[3:4]):
                coincidencias +=1

        print(f"""No acerto

        Aciertos ={aciertos}
        Coincidencias ={coincidencias}

        """)
        numero = pedirNumero(input
        ("Ingrese un numero de cuatro cifras que no se repitan: "))


        print("Gano el juego!")

Comenzar()
