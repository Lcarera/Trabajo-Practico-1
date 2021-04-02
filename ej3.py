#La variable se llama a si misma hasta que el valor de "n" sea 0
def fact(n):
    if n == 0:
        f = 1
    else:
        f = n * fact(n - 1)
    return f


factorial= int(input("Ingrese un numero entero y se va a devolver su factorial "))
if factorial < 0:
    print("El factorial de",factorial,"es",fact(factorial)*-1)
else:
    print("El factorial de",factorial,"es",fact(factorial))
   

        