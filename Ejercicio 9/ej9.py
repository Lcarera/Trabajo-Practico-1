"""Pide que se ingrese una contraseña hasta que sea igual a una ya predefinida"""
CONTRASEÑA= "master$123"
contra = ""
while not contra == CONTRASEÑA:
    contra= input("Ingrese la contraseña: ")
    if contra == CONTRASEÑA:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")