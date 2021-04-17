"""Pide cuantos ejercicios tiene un examen y que porcentaje debe ser correcto para estar aprobado,
despues permite ingresar cuantos ejercicicos correctos tiene un examen y devuelve si esta aprobado o no."""
def aprobarExamen(ejercicios,porcentaje):
    """Calcula la nota minima"""
    notaMinima=(porcentaje*ejercicios)/100
    return notaMinima

def calcularNota(nota,ejercicios):
    """Calcula el porcentaje de ejercicios correctos"""
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
       
