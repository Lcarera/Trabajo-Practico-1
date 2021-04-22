"""Da 3 opciones para modificar una cadena, sacarle las vocales,
sacarle las consonantes o remplazar las vocales"""
def sacarVocales(cadena):
    """Recorre la cadena ingresada y saca las vocales"""
    for c in cadena:
        if c in "aeiouAEIOU":
            cadena = cadena.replace(c,"")
    return cadena

def sacarConsonantes(cadena):
    """Recorre la cadena ingresada y saca las consonantes"""
    for c in cadena:
        if not c in "aeiouAEIOU":
            cadena = cadena.replace(c,"")
    return cadena


def remplazarVocal(cadena):
    vocales=["a","e","i","o","u"]
    """Recorre la cadena ingresada y remplaza las vocales por su siguiente vocal
    Ej.: a se remplaza por e"""
    for c in cadena:
        if c in "aeiouAEIOU":
            if c == "a" or c== "A":
                i = 0
                if c == "a":
                    cadena = cadena.replace(c,vocales[i+1])  
                elif c == "A":
                    cadena = cadena.replace(c,vocales[i+1].upper())

            if c == "e" or c== "E":
                i = 1
                if c == "e":
                    cadena = cadena.replace(c,vocales[i+1])  
                elif c == "E":
                    cadena = cadena.replace(c,vocales[i+1].upper())
            if c == "i" or c== "I":
                i = 2
                if c == "i":
                    cadena = cadena.replace(c,vocales[i+1])  
                elif c == "I":
                    cadena = cadena.replace(c,vocales[i+1].upper())
            if c == "o" or c== "O":
                i = 3
                if c == "o":
                    cadena = cadena.replace(c,vocales[i+1])  
                elif c == "O":
                    cadena = cadena.replace(c,vocales[i+1].upper())  
            if c == "u" or c=="U":
                i = -1
                if c == "u":
                    cadena = cadena.replace(c,vocales[i+1])  
                elif c == "U":
                    cadena = cadena.replace(c,vocales[i+1].upper())   
    
    return cadena                  

def detectarPalindromos(cadena):
    """Compara una cadena, con la misma cadena pero dada vuelta para comprobar sies un palindromo."""
    if cadena == cadena[::-1]:
        return 1
    else:
        return 0

cadena = input("Ingrese una cadena: \n")
opcion=int(input("""Elija la funcion a realizar:
1. Sacar vocales de una cadena.
2. Sacar consonantes de una cadena.
3. Remplazar las vocales de una cadena por su siguiente vocal 
4. Revisar si dos cadena son capicua.
"""))

if opcion == 1:
    print("Su cadena sin vocales queda",sacarVocales(cadena))
elif opcion == 2:
    print("Su cadena sin consonantes queda",sacarConsonantes(cadena))
elif opcion == 3:
    print("Su cadena con las vocales remplazadas queda",remplazarVocal(cadena))
elif opcion == 4:
    if detectarPalindromos(cadena) == 1:
        print("La cadena ingresada es capicua.")
    else:
        print("La cadena ingresada no es capicua.")

