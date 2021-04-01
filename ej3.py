def fact(n):
    if n == 0:
        f = 1
    else:
        f = n * fact(n - 1)
    return f

factorial= int(input("Ingrese un numero entero y se va a devolver su factorial "))
print("El factorial de ",factorial,"es ",fact(factorial))