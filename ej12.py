"""Devuelve cuantas vocales tiene una cadena, ingresada por el usuario."""
def contarVocales(cadena):
    """Cuenta las vocales de una cadena."""
    vocal = 0
    for c in cadena:
        if c in "aeiouAEIOU":
            vocal = vocal + 1
    return vocal

cadena= input("Ingrese una cadena y se devolvera cuantas vocales tiene: ")
print(f"{cadena} tiene {contarVocales(cadena)} vocales.")