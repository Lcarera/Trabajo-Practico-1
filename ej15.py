

def mostrarSiglas(cadena):
    palabras = cadena.split(" ")
    siglas=""
    for i in palabras:
        siglas += i[0]

    return siglas.upper()

def ponerMayus(cadena):
    palabras = cadena.split(" ")
    frase=""
    for i in palabras:
        frase += i.capitalize() + " "

    return frase

def mostrarPorLetra(cadena, letra):
    palabras = cadena.split(" ")
    encontrarPalabras = ""
    for i in palabras:
        if i[0] == letra:
            encontrarPalabras += i + " "
    if encontrarPalabras=="":
        encontrarPalabras=f"No hay palabras con la letra {letra}"

    return encontrarPalabras

cadena=input("Ingrese una frase: ")

opcion=int(input("""
1. Mostrar siglas de la frase.
2. Poner en mayuscula la primera letra de cada palabra.
3. Mostrar las palabras de la frase que empiecen por una letra indicada.
"""))

if opcion == 1:
    print(f"Las siglas de {cadena} son {mostrarSiglas(cadena)}")
elif opcion == 2:
    print(ponerMayus(cadena))
elif opcion == 3:
    letra= input("Ingrese una letra: ")
    print(mostrarPorLetra(cadena,letra))

