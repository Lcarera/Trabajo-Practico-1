"""Pide el nombre dek usuario y devuele un saludo,
despues pide dos factores para hacer un producto"""
try:
    nombre = input("Ingrese su nombre completo \n")
    if nombre.isdigit() == True:
        print("No ingrese numeros!")
    else:
        if nombre == "":
            print("No ingreso su nombre")
        else:
            print(f"Hola {nombre}!")
except ValueError:
    print("Nombre no valido")

try:   
    fact1 = float(input("Ingrese el primer factor: "))
    fact2 = float(input("Ingrese el segundo factor: "))
    prod = fact1 * fact2
    print(f"El producto entre {fact1} y {fact2} es {prod}")
except ValueError:
    print("Datos no validos")