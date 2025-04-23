###Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.###
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n1>n2 :
    print(n1," es mayor que",n2)
elif n1<n2 :
    print(n1," es menor que",n2)
else :
    print("Los numeros son iguales")
    