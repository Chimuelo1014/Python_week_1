
secret_number = 6
number = 0
while True : 
    number = int(input("Adivina el numero: "))       
    if number != secret_number :
        if number > secret_number :
            print("su numero es mayor, intentelo nuevamente")
        elif number < secret_number :
            print("su numero es menor, intentelo nuevamente")
            
    else :
        print("¡ADIVINASTE!")
        break


