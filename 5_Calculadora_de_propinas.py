total = int((input("Ingrese el total de la cuenta: ")))
porcentage = float((input("¿Que porcentaje de propina quiere dejar?\nSeleccione 1 para 10%\nSeleccione 2 para 15%\nSeleccione 3 para 20%: ")))
if porcentage == 1 :
    tip = total*0.10 
elif porcentage == 2 :
    tip = total*0.15
else :
    tip = total*0.20

print("La propina es de: $","%.2f" % tip)