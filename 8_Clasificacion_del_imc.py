###Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra: "Bajo peso" si es menor a 18.5"Normal" si está entre 18.5 y 24.9"Sobrepeso" si está entre 25 y 29.9"Obesidad" si es mayor o igual a 30###
weight = float(input("Ingrese su peso: "))
height = float(input("Ingrese su altura : "))
imc = weight/(height*height)
if imc < 18.5 :
    print("Bajo peso")
elif imc >=18.5 and imc < 25 :
    print("Normal")
elif imc >=25 and imc <30 :
    print("Sobrepeso")
else :
    print("Obesidad")