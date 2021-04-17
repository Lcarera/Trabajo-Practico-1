"""Pide un año y devuelve su equivalente en numeros romanos"""
num_rom = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
           (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def convertirAño(num):
  """Convierte el numero ingresado en numeros romanos"""
    rom = ""

    while num > 0:
        for n, r in num_rom:
            while num > n or num == n:
                rom = rom + r
                num = num - n
                
        
    return rom

año=int(input("Ingrese un año y se devolvera en numeros romanos: "))
if año < 0:
    "Año no valido"
elif año == 0:
    "Los numeros romanos no representan los 0"
else: 
    print(convertirAño(año))