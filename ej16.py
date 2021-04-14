def sacarVocales(cadena):
    for c in cadena:
        if c in "aeiouAEIOU":
            cadena = cadena.replace(c,"")
    return cadena

def sacarConsonantes(cadena):
    for c in cadena:
        if not c in "aeiouAEIOU":
            cadena = cadena.replace(c,"")
    return cadena

vocales=["a","e","i","o","u"]

def remplazarVocal(cadena):

    for c in cadena:
        if c in "aeiouAEIOU":
            if c == "a" or c== "A":
                i = 0
                cadena = cadena.replace(c,vocales[i+1])  
            if c == "e" or c== "E":
                i = 1
                cadena = cadena.replace(c,vocales[i+1])  
            if c == "i" or c== "I":
                i = 2
                cadena = cadena.replace(c,vocales[i+1])  
            if c == "o" or c== "O":
                i = 3
                cadena = cadena.replace(c,vocales[i+1])  
            if c == "u" or c=="U":
                i = -1
                cadena = cadena.replace(c,vocales[i+1])      
    
    return cadena                  

def detectarPalindromos(cadena1,cadena2):
    if cadena2 == cadena1[::-1]:
        return 1
    else:
        return 0


opcion=int(input("""Elija la funcion a realizar:
1. Sacar vocales de una cadena.
2. Sacar consonantes de una cadena.
3. Remplazar las vocales de una cadena por su siguiente vocal 
4. Revisar si dos cadena son capicua.
"""))

if opcion == 1:
    cadena = input("Ingrese una cadena: \n")
    print("Su cadena sin vocales queda",sacarVocales(cadena))
elif opcion == 2:
    cadena = input("Ingrese una cadena: \n")
    print("Su cadena sin consonantes queda",sacarConsonantes(cadena))
elif opcion == 3:
    cadena = input("Ingrese una cadena: \n")
    print("Su cadena con las vocales remplazadas queda",remplazarVocal(cadena))
elif opcion == 4:
    cadena1 = input("Ingrese una cadena: \n")
    cadena2 = input("Ingrese otra cadena: \n")
    if detectarPalindromos(cadena1,cadena2) == 1:
        print("Las cadenas ingresadas son capicua.")
    else:
        print("Las cadenas ingresadas no son capicua")

