"""Pide 6 numeros, hace todas las multiplicaciones posibles y devuelve el mayor producto"""
def compararMayor(a,b):
    """Compara dos numeros y devuelve el mayor"""
    if a > b:
        return a
    else:
        return b
numeros=[]
try:
    x1=int(input("ingrese el primer numero: "))
    x2=int(input("ingrese el segundo numero: "))
    x3=int(input("ingrese el tercer numero: "))
    x4=int(input("ingrese el cuarto numero: "))
    numeros=[x1,x2,x3,x4]
except ValueError:
    print("Datos Invalidos")
productos = []

for posicion1, valor1 in enumerate(numeros):
    for posicion2, valor2 in enumerate(numeros):
        if posicion1 != posicion2:
            productos.append(valor1 * valor2)

print(productos)

# mayor1= compararMayor(x12,x13)    
# mayor2= compararMayor(mayor1,x14) 
# mayor3= compararMayor(mayor2,x23) 
# mayor4= compararMayor(mayor3,x24)
# Mayor= compararMayor(mayor4,x34) 
print("El mayor producto es", max(productos))
