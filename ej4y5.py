
def conversorC(f):
    Celsius= (f-32)*5/9
    return "{0:.2f}".format(Celsius)

def conversorF(c):
    Fahrenheit= (9/5) * c + 32
    return "{0:.2f}".format(Fahrenheit)

def tablaConversion(f):   
    for i in range (13): 
        print(str(i*10)+"° son "+str(conversorC(f))+"°")
        f = f + 10 

conversion=(input(""" 
1. Convertir Fahrenheit a Celsius
2. Convertir Celsius a Fahrenheit
3. Tabla de conversion
"""))
if conversion == "1" :
    temp=float(input("Ingrese la temperatura a convertir "))
    print(str(temp)+"° son "+str(conversorC(temp))+"°")
elif conversion == "2" :
    temp=float(input("Ingrese la temperatura a convertir "))
    print(str(temp)+"° son "+str(conversorF(temp))+"°")
elif conversion == "3" :
    temp = 0
    tablaConversion(temp)
else:
    print("Ingrese un valor valido")