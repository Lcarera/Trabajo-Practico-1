def contarVocales(cadena):
    vocal = 0
    for c in cadena:
        if c in "aeiouAEIOU":
            vocal = vocal + 1
    return vocal

cadena= input("Ingrese una cadena y se devolvera cuantas vocales tiene: ")
print(cadena,"tiene",contarVocales(cadena),"vocales.")