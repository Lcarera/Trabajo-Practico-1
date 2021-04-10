# 16. Escribir funciones que dada una cadena de caracteres:
# 1. Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
# 'logaritmos' debe devolver 'lgrtms' .
# 2. Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
# devolver 'i ooae'.
# 3. Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
# devolver 'vistaerou'.
# 4. Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo
# (se lee igual de izquierda a derecha que de derecha a izquierda).

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
            print(c)
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


print(remplazarVocal("baloo"))