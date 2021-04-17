"""Se agrega un limite de intentos para ingresar la contraseña."""
CONTRASEÑA= "master$123"
n = 0
while n < 3:
    contra = input("Ingrese la contraseña: ")
    if contra == CONTRASEÑA:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta.")
        if n == 2:
            print("Supero la cantidad maxima de intentos.")
            break
        else:
            print("Quedan",2 - n,"intentos.")
            n = n + 1


