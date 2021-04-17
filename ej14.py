"""Genera un numero de 4 cifras distintas y permite que el usuario vaya ingresando
numeros hasta que coincidan."""
import random
from random import randrange

def validarNumero(numero):
    """Valida que el numero tenga 4 cifras y sean distintas"""
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
    """Genera el codigo"""
    codigo = 0
    while not validarNumero(codigo):
        codigo = randrange(10000)
    return codigo

def compararCodigo(codigo,numero):
    """Compara el codigo generado con el ingresado"""
    return str(codigo) == str(numero)

def pedirNumero(numero):
    """Pide el numero"""
    while not validarNumero(numero):
        print("Ingrese un numero valido")
        numero = input("Ingrese un numero de cuatro cifras que no se repitan: ")
    return numero


def Comenzar():
    """Comienza el juego, pide el numero lso compara, en caso de que una cifra coincida en numero y posicion
    lo cuenta como un acierto, si solo coincide en numero lo cuenta como una coincidencia"""
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
