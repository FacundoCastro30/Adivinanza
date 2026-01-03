import random

numeroSecreto = random.randint(1, 101)
adivinado = False
vidas = 3 # me pareció más simple con un sistema de vidas y que reduzca en 1 por cada error

# print(numeroSecreto) -> Esto fue solo para adivinar y probar todo
print("¡Bienvenido al juego de adivinanzas!")

while not adivinado:
    if vidas == 0: 
        print(f"¡Game over! El numero era {numeroSecreto}") # al perder, me pareció bueno que muestre el número a adivinar
        break
    numero = int(input("Ingresá un numero del 1 al 99: "))
    if numero == numeroSecreto:
        print("¡Adivinaste!")
        adivinado = True
    elif numero < numeroSecreto:
        print("Tu número es mas bajo")
    elif numero > numeroSecreto:
        print("Tu número es mas alto")
    else:
        print("Hubo un error") #TODO manejo de errores, ejemplo: se ingresa texto
    vidas -=1
    print(f"Te quedan {vidas} vidas")