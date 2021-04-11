def comprobarBisiesto(año):
    if año % 4 != 0:
        return 0
    elif año % 4 == 0 and año % 100 != 0: 
	    return 1
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
	    return 0
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	    return 1

def validarMes(mes):
    mescomp= 0
    if mes == "4" or mes == "abril":
        mescomp = 4
    elif mes == "6" or mes == "junio":
        mescomp = 6
    elif mes == "9" or mes == "septiembre":
        mescomp = 9
    elif mes == "11" or mes == "noviembre" :
        mescomp = 11
    elif mes == "1" or mes == "enero":
        mescomp = 1
    elif mes == "3" or mes == "marzo":
        mescomp = 3
    elif mes == "5" or mes == "mayo":
        mescomp = 5
    elif mes == "7" or mes == "julio" :
        mescomp = 7
    elif mes == "8" or mes == "agosto":
        mescomp = 8
    elif mes == "10" or mes == "octubre":
        mescomp = 10
    elif mes == "12" or mes == "diciembre" :
        mescomp = 12
    elif mes== "2" or mes == "febrero" :
        mescomp = 2
    return mescomp

def diasMes(mes, año):
    
    mescomp=validarMes(mes)
    if comprobarBisiesto(año) == False:
        diasMeses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        diasMeses = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return diasMeses[mescomp]  


def validarFecha(dia,mes,año):
    mescomp=validarMes(mes)
    if año < 0:
        print("Año invalido.")
    elif dia < 0 or dia >31:
        print("Dia invalido.")
    elif dia > diasMes(mescomp, año):
        print("Dia invalido.")
    elif mescomp < 0:
        print("Mes invalido.")
    else:
        return 1

def diasRestantesMes(dia,mes,año):
    mescomp=validarMes(mes)
    resta=diasMes(mescomp,año)-dia
    return resta

def diasRestantesAño(dia,mes,año):
    mescomp=validarMes(mes)
    i = mescomp
    dias= diasMes(mescomp, año) - dia
    if comprobarBisiesto(año) == False:
        diasMeses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        diasMeses = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if i < 12:
        while i < 12:
            dias = dias + diasMeses[i]
            i = i + 1
        total =   dias 
        return total 
    else:
        total = diasRestantesMes(dia,mescomp,año)
        return total

def diasTranscurridos(dia,mes,año):
    mescomp=validarMes(mes)
    i = mescomp
    dias= diasMes(mescomp, año) - diasRestantesMes(dia,mescomp,año)
    if comprobarBisiesto(año) == False:
        diasMeses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        diasMeses = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if i > 1:
        while i > 1:
            dias = dias + diasMeses[i]
            i = i - 1
        total =   dias 
        return total 
    else:
        total = diasRestantesMes(dia,mescomp,año)
        return total

def diferenciaFechas(dia1,mes1,año1,dia2,mes2,año2):
    mescomp1=validarMes(mes1)
    mescomp2=validarMes(mes2)
    validarFecha(dia1,mescomp1,año1)
    validarFecha(dia2,mescomp2,año2)
   
    if año1 < año2:
        año = año2 - año1
        mes = mescomp2 - mescomp1
        dia = dia2 - dia1
        if mes < 0:
            año -= 1               
            mes = 12 + mes
        
        if dia < 0:
            mes -=1
            dia = diasMes(mes, año) + dia
        
        diferencia = año,"años,",mes,"meses y",dia,"dias"
        return diferencia
    
    elif año1 > año2:
        año = año1 - año2
        mes = mescomp1 - mescomp2
        dia = dia1 - dia2
        if mes < 0:
            año -= 1               
            mes = 12 + mes
        
        if dia < 0:
            mes -=1
            dia = diasMes(mes, año) + dia
        
        diferencia = str(año),"años,",str(mes),"meses",str(dia),"dias"
        return str(diferencia)
   
    elif año1 == año2:
        año = año1
        if mescomp1 > mescomp2:
            mes = mescomp1 - mescomp2
            dia = dia1 - dia2     
            if dia < 0:
                mes -=1
                dia = diasMes(mescomp1 - mescomp2, año) + dia     
               
            diferencia = mes,"meses y",dia,"dias"
            return diferencia
        
        elif mescomp2 > mescomp1:
            
            mes = mescomp2 - mescomp1
            dia = dia2 - dia1     
            
            if dia < 0:
                mes -=1
                dia = diasMes(mescomp2 - mescomp1, año) + dia     
                
            diferencia = mes,"meses y",dia,"dias"
            return diferencia
       
        elif mescomp1 == mescomp2:
            
            if dia1 > dia2:
                dia = dia1 - dia2
                diferencia = dia,"dias" 
                return diferencia
            
            elif dia2 > dia1:
                dia = dia1 - dia2
                diferencia = dia,"dias" 
                return diferencia
            
            elif dia1 == dia2:
                diferencia="las fechas son iguales"
                return diferencia


       
       
        

        


    

    



opcion=input("""Elija su Funcion:
1. Comprobar si un año es bisiesto.
2. Comprobar cuantos dias tiene un mes.
3. Validar una fecha.
4. Verificar cuantos dias falta para que termine un mes.
5. Verificar cuantos dias falta para que termine el año.
6. Verificar cuantos dias pasaron antes de la fecha ingresada.
7. Verificar el timepo transcurrido entre dos fechas.
""")

if opcion == "1":
    año= int(input("Ingrese el año "))
    bisiesto=comprobarBisiesto(año)
    if bisiesto == 1:
        print("El año",{año}," es bisiesto.")
    else:
         print("El año", {año}," no es bisiesto.")

if opcion == "2":
    mes = input("Ingrese el mes: ".lower())
    año = int(input("Ingrese el año: "))
    if año < 0:
        print("año invalido.")
    print("En el año" ,año, "el mes" ,mes, "tiene",diasMes(mes, año),"dias")

if opcion == "3":
    dia = int(input("Ingrese el dia: "))
    mes = input("Ingrese el mes: ".lower())
    año = int(input("Ingrese el año: "))
    validarFecha(dia,mes,año)
    if validarFecha(dia,mes,año) == 1:
        print("Fecha Valida.")

if opcion == "4":
    dia = int(input("Ingrese el dia: "))
    mes = input("Ingrese el mes: ".lower())
    año = int(input("Ingrese el año: "))
    diasRestantesMes(dia,mes,año)
    print("Faltan",diasRestantesMes(dia,mes,año),"dias para que termine el mes.")
    
if opcion == "5":
    dia = int(input("Ingrese el dia: "))
    mes = input("Ingrese el mes: ".lower())
    año = int(input("Ingrese el año: "))
    diasRestantesAño(dia,mes,año)
    print("Faltan",diasRestantesAño(dia,mes,año),"dias para que termine el año.")

if opcion == "6":
    dia = int(input("Ingrese el dia: "))
    mes = input("Ingrese el mes: ".lower())
    año = int(input("Ingrese el año: "))
    print("Pasaron",diasTranscurridos(dia,mes,año),"hasta la fecha.")

if opcion == "7":
    dia1 = int(input("Ingrese el primer dia: "))
    mes1 = input("Ingrese el primer mes: ".lower())
    año1 = int(input("Ingrese el primer año: "))
    dia2 = int(input("Ingrese el segundo dia: "))
    mes2 = input("Ingrese el segundo mes: ".lower())
    año2 = int(input("Ingrese el segundo año: "))
    print("Pasaron",diferenciaFechas(dia1,mes1,año1,dia2,mes2,año2),"entre las fechas.")






