"""El programa pide un numero y haciendo uso de la recursividad devuelve el factorial"""
def fact(n):
    """La variable se llama a si misma hasta que el valor de "n" sea 0
    despues suma todos los resultados que se van almacenando."""

    if n == 0:
        f = 1
    else:
        f = n * fact(n - 1)
    return f


factorial= int(input("Ingrese un numero entero y se va a devolver su factorial: "))
if factorial < 0:
    print("No se puede calcular el factorial de un numero negativo.")
else:
    print(f"El factorial de {factorial} es {fact(factorial)}")
   

        