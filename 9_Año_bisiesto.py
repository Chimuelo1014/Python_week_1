###Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).###
year = int(input("Ingrese el año: "))

if year % 4 == 0 and year % 100 != 0 and year % 400 != 0 :
    print("El año es bisiesto")
else :
    print("El año no es bisiesto")