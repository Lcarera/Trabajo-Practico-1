"""El programa da 3 opciones.
Dependiendo de la opcion elegida pide la temperatura y la devuelva convertida,
o devuelve una tabla de conversion."""
def conversorC(f):
    """Convierte grados Celsius a Fahrenheit."""
    Celsius= (f-32)*5/9
    return "{0:.2f}".format(Celsius)

def conversorF(c):
    """Convierte grados Fahrenheit a Celsius."""
    Fahrenheit= (9/5) * c + 32
    return "{0:.2f}".format(Fahrenheit)

#"{0:.2f}".format sirve para mostrar solo los dos primeros numeros despues de la coma.

def tablaConversion():   
    f = 0
    while f <= 120:
        """Imprime una tabla de conversion entre grados Fahrenheit y Celsius."""
        print(f"{f} °F son {conversorC(f)} °C.")
        f = f + 10 

conversion=(input(""" 
1. Convertir Fahrenheit a Celsius.
2. Convertir Celsius a Fahrenheit.
3. Tabla de conversion.
"""))
if conversion == "1" :
    temp=float(input("Ingrese la temperatura a convertir: "))
    print(f"{temp}°F son {conversorC(temp)}°C.")
elif conversion == "2" :
    temp=float(input("Ingrese la temperatura a convertir: "))
    print(f"{temp}°C son {conversorF(temp)}°F.")
elif conversion == "3" :
    tablaConversion()
else:
    print("Ingrese un valor valido.")