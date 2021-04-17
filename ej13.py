"""Compara dos palabras para ver si son iguales pero la segunda en mayusculas"""
def compararPalabra(palabra, palabraupper):
    """Compara las palabras"""
    if palabraupper==palabra.upper():
        return True
    else:
        return False

palabra1=input("Ingrese una palabra: ")
palabra2=input("Ingrese la misma palabra capitalizada: ")
if palabra1.isdigit()==True or palabra2.isdigit()==True:
    print("Ingrese palabras no numeros")

if compararPalabra(palabra1,palabra2) == 1:
    print("Bien")
else:
    print("Mal")