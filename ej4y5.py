
def conversorC(f):
    #Convierte grados Celsius a Fahrenheit.
    Celsius= (f-32)*5/9
    return "{0:.2f}".format(Celsius)

def conversorF(c):
    #Convierte grados Fahrenheit a Celsius.
    Fahrenheit= (9/5) * c + 32
    return "{0:.2f}".format(Fahrenheit)

#"{0:.2f}".format sirve para mostrar solo los dos primeros numeros despues de la coma.

def tablaConversion():   
    f = 0
    while f <= 120:
        #Imprime una tabla de conversion entre grados Fahrenheit y Celsius.
        print(str(f)+"°F son "+str(conversorC(f))+"°C.")
        f = f + 10 

conversion=(input(""" 
1. Convertir Fahrenheit a Celsius.
2. Convertir Celsius a Fahrenheit.
3. Tabla de conversion.
"""))
if conversion == "1" :
    temp=float(input("Ingrese la temperatura a convertir: "))
    print(str(temp)+"°F son ",(str(conversorC(temp)))+"°C.")
elif conversion == "2" :
    temp=float(input("Ingrese la temperatura a convertir: "))
    print(str(temp)+"°C son "+str(conversorF(temp))+"°F.")
elif conversion == "3" :
    tablaConversion()
else:
    print("Ingrese un valor valido.")