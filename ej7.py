#Escribir funciones que resuelvan los siguientes problemas:
#1. Dado un año indicar si es bisiesto. (Nota: un año es bisiesto si es un número divisible
#por 4, pero no si es divisible por 100, excepto que también sea divisible por 400).
#2. Dado un mes, devolver la cantidad de días correspondientes.
#3. Dada una fecha (día, mes, año), indicar si es válida o no.
#4. Dada una fecha, indicar los días que faltan hasta fin de mes.
#5. Dada una fecha, indicar los días que faltan hasta fin de año.
#6. Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
#7. Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
#entre ambas, en años, meses y días.
#Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.
def comprobarBisiesto(año):
    if año % 4 != 0:
        return 0
    elif año % 4 == 0 and año % 100 != 0: 
	    return 1
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
	    return 0
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	    return 1

def diasMes(mes, año):
    if mes == "4" or mes == "abril" or mes == "ABRIL" or mes == "Abril" or mes == "6" or mes == "junio" or mes == "JUNIO" or mes == "Junio" or mes == "9" or mes == "septiembre" or mes == "SEPTIEMBRE" or mes == "Septiembre"or mes == "11" or mes == "noviembre" or mes == "NOVIEMBRE" or mes == "Noviembre" :
        dias = 30
        return dias
    elif mes== "2" or mes == "febrero" or mes == "FEBRERO" or mes == "Febrero":
        if comprobarBisiesto(año) == 0 :

            dias = int(28)
            return dias
        else :
            dias = int(29)
            return dias
    elif mes == "1" or mes == "enero" or mes == "ENERO" or mes == "Enero" or mes == "3" or mes == "marzo" or mes == "MARZO" or mes == "Marzo" or mes == "5" or mes == "mayo" or mes == "MAYO" or mes == "Mayo"or mes == "7" or mes == "julio" or mes == "JULIO" or mes == "Julio" or mes == "8" or mes == "agosto" or mes == "AGOSTO" or mes == "Agosto" or mes == "10" or mes == "octubre" or mes == "OCTUBRE" or mes == "Octubre" or mes == "12" or mes == "diciembre" or mes == "DICIEMBRE" or mes == "Diciembre" :
        dias = int(31)
        return dias
    elif año < 0:
        print("Año invalido")
    else:
        print("Datos Invalidos")

def validarFecha(dia,mes,año):
    if año < 0:
        print("Año invalido")
    elif dia < 0 or dia >31:
        print("Dia invalido")
    elif dia > (diasMes(mes, año)):
        print("Dia invalido")
    elif mes < 0:
        print("Mes invalido")
    else:
        print("Fecha Valida")

opcion= input("""
1. Comprobar si un año es bisiesto.
2. Comprobar cuantos dias tiene un mes.
3. Validar una fecha
""")

if opcion == "1":
    año= int(input("Ingrese el año "))
    bisiesto=comprobarBisiesto(año)
    if bisiesto == 1:
        print("El año",año,"es bisiesto.")
    else:
         print("El año",año,"no es bisiesto.")

if opcion == "2":
    mes = (input("Ingrese el mes "))
    año = (input("Ingrese el año "))
    print("En el año",año,", el mes",mes,"tiene",diasMes(mes, año),"dias")

if opcion == "3":
    dia = int(input("Ingrese el dia "))
    mes = int(input("Ingrese el mes "))
    año = int(input("Ingrese el año "))
    validarFecha(dia,mes,año)






