import random

numeroSecreto = random.randint(1, 101)
adivinado = False
vidas = 5 #me pareció más simple con un sistema de vidas y que reduzca en 1 por cada error

print("Bienvenido al juego")

while not adivinado:
    if vidas == 0: 
        print(f"Game over, el numero era {numeroSecreto}") #al perder, me pareció bueno que muestre el número a adivinar
        break
    else:
        numero = int(input("introduzca un numero del 1 al 99: "))
        if numero == numeroSecreto:
            print("Adivinaste")
            adivinado = True
        elif numero < numeroSecreto:
            print("Tu número es mas bajo, volve a intentarlo")
            vidas -=1
        elif numero > numeroSecreto:
            print("Tu número es mas alto, volve a intentarlo")
            vidas -=1
        else:
            print("hubo un error") #TODO manejo de errores, ejemplo: se ingresa texto
    