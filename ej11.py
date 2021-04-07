# 11. Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje
# necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo
# de exámenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por
# el alumno, indicando con un valor centinela que no hay más exámenes a revisar. Debe
# mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos
# respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.
#  cuantos ej habia
#  cuantos se necesitan
#  valor centinela 
#  cauntos hizo bien el alumno % de bien y si aprobo o no

def aprobarExamen(ejercicios,porcentaje):
    notaMinima=(porcentaje*ejercicios)/100
    return notaMinima

def calcularNota(nota,ejercicios):
    notaPorcentaje=(nota*100)/ejercicios
    return notaPorcentaje
ejercicios = 0
while ejercicios == 0 or ejercicios < -1:
    ejercicios=int(input("Cuantos ejercicios  tiene el examen? "))
    if ejercicios < 0:
        print("Datos no validos.")
    
porcentaje=int(input("Que porcentaje se necesita para aprobar? "))
if porcentaje > 100:
    print("Datos no validos.")
if porcentaje < 0:
    print("Datos no validos.")


nota = 0
while nota != -1:
    nota =int(input("Ingrese cuantos ejercicios correctos: "))
    
    if nota > ejercicios:
        print("Datos no validos.")
    elif nota < -1:
        print("Datos no validos.")
    elif nota == -1:
        break
    else:
        if nota > aprobarExamen(ejercicios,porcentaje):
            print(f"El alumno aprobo con un {calcularNota(nota,ejercicios)}% de los ejercicios correctos")
        elif nota < aprobarExamen(ejercicios,porcentaje):
            print(f"El alumno reprobo con un {calcularNota(nota,ejercicios)}% de los ejercicios correctos")
        elif nota == aprobarExamen(ejercicios,porcentaje):
            print(f"El alumno aprobo con un {calcularNota(nota,ejercicios)}% de los ejercicios correctos")
       
