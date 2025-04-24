
while True :                                                 ### En este while, (como en el resto de los while), para evitar errores, en este caso para cuando el usuario ingrese un espacion en blanco para el nombre del producto, asi que se repetira hasta resivir caracteres###
    name = input("Ingrese el nombre del producto: ")         ### Guarda el nombre del producto ingresado por el usuario###
    if name != "" :                                          ###El if nos va decir si el espacio no esta en blanco se salte el while sino que lo repita hasta que se ingresen caracteres validos###
        break                                                ###si no se cumple la condicion envia mensaje de advertencia###
    else :
     print("¡Debe ingresar el nombre del producto!")

while True :
    unity = int(input("Ingrese el precio unitario del producto: "))   ###Pide el valor de la unidad del producto###  
    if unity >= 0 :
        break                                               ###El break sirve para salir del ciclo###
    else :
        print("¡Ingrese un valor valido!")
 
while True :
    amount = int(input("Ingrese la cantidad de unidades del producto: "))
    if amount >= 0 :                                                          ###Valida que no sea menor a cero y se ingrese una cantidad valida###
        break
    else :
        print("¡Ingrese un valor valido!")                               ###si esta mal sale un aviso###
        
    
porcen = input("¿Tiene descuento? Y(si)/N(no): ")
if porcen == "Y" or porcen == "y":                                         ###sirve para saber si se hara con descuento o no, si es asi, aplicara el descuento###
    
    while True :                                                             
        discount = int(input("Ingrese el descuento a aplicar: "))
        if discount > 0 or discount < 100 :
            break
        else :
            print("¡Ingrese un valor valido!")
    valor1 = unity*amount
    desc = discount*0.01 
    descu = valor1*desc
    valortotal = valor1-descu 

else :                                                                       ###si no aplicara descuento se ira por este lado###
    valor1 = unity*amount
    valortotal = valor1
   
 
print("Producto: ",name)                                  ###se imprimen el nombre del producto , el precio de unidad y el valor total con descuento o no, segun el caso###
print("Precio unitario: $","%.2f" % unity)
print("Valor total: $","%.2f" % valortotal)



    
                

    
