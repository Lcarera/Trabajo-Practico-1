def calcularPerimetroR(base, altura):
    #Calcula el perimetro de un rectangulo.
    per=(base)*2+(altura)*2
    return "{0:.2f}".format(per)

def calcularAreaR(base,altura):
    #Calcula el area de un rectangulo.
    area= base*altura
    return "{0:.2f}".format(area)

def calcularArea2(x1,x2,y1,y2):
    #Calcula el area de un rectangulo segun sus coordenadas en un grafico.
    area2=(x2-x1)*(y2-y1)
    return "{0:.2f}".format(area2)

def calcularPerimetroC(radio):
    perimetro = radio * 2 * 3.14
    #Calcula el perimetro de un circulo.
    return "{0:.2f}".format(perimetro)

def calcularAreaC(radio):
    #Calcula el area de un circulo.
    area= radio**2 * 3.14
    return "{0:.2f}".format(area) 

def calcularVolumen(radio):
   #Calcula el volumen de una esfera.
    V = 4/3 * 3.14 * radio**3
    return "{0:.2f}".format(V)

def calcularHipotenusa(cateto1,cateto2):
    #Calcula la hipotenusa de un triangulo rectangulo, segun el teorema de pitagoras.
    h =(cateto1**2 + cateto2**2)**0.5
    return "{0:.2f}".format(h)

#"{0:.2f}".format sirve para mostrar solo los dos primeros numeros despues de la coma.

calculo=input("""Elija su calculo:
1.Calcular perimetro.
2.Calcular area.
3.Calcular area dadas sus coordenadas.
4.Calcular el perimetro de un circulo.
5.Calcular el area de un circulo.
6.Calcular el volumen de una esfera.
7.Calcular la hipotenusa.
""")

if calculo.isdigit():
    if calculo == "1" :
        a=int(input("Ingrese la altura: "))
        b=int(input("Ingrese la base: "))
        if a < 1 or b < 1:
            print("No ingrese numeros negativos.")
        else:
            print("El perimetro es:",calcularPerimetroR(a,b))
    if calculo == "2":
        a=int(input("Ingrese la altura: "))
        b=int(input("Ingrese la base: "))
        if a < 1 or b < 1:
             print("No ingrese numeros negativos.")
        else:
             print("El area es ", calcularAreaR(a,b))
    if calculo == "3":
        x1=int(input("Ingrese x1:"))
        x2=int(input("Ingrese x2: "))
        y1=int(input("Ingrese y1: "))
        y2=int(input("Ingrese y2: "))
        if x1 < 1 or x2 < 1 or  y1 < 1 or y2 < 1:
             print("No ingrese numeros negativos.")
        else:
            print ("El area es: ", calcularArea2(x1,x2,y1,y2))
    if calculo == "4" :
        r=int(input("Ingrese el radio: "))
        if r < 1:
            print("No ingrese numeros negativos.")
        else:
            print("El perimetro es: ",calcularPerimetroC(r))
    if calculo == "5" :
        r=int(input("Ingrese el radio: "))
        if r<1:
            print("No ingrese numeros negativos.")
        else:
            print("El perimetro es: ",calcularAreaC(r))
    if calculo == "6" :
        r=int(input("Ingrese el radio: "))
        if r<1:
            print("No ingrese numeros negativos.")
        else:
            print("El volumen es: ",calcularVolumen(r))
    if calculo == "7":
        a=int(input("Ingrese un cateto: "))
        b=int(input("Ingrese el otro cateto: "))
        if a < 1 or b < 1:
             print("No ingrese numeros negativos.")
        else:
             print("La hipotenusa es: ", calcularHipotenusa(a,b))
    if int(calculo) <1 or int(calculo) >7:
        print("Ingrese numero dentro de las opciones.")
else :
    print("Ingrese un numero.")



