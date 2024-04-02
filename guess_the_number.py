import random

def adivina_el_numero(numero_secreto, intentos):
    if intentos == 0:
        print(f"Te has quedado sin intentos, el numero secreto era {numero_secreto}")
        return
    else:
        intento = int(input("\nAdivina el numero (1-100): "))
        if intento == numero_secreto:
            print("Felicidades, haz adivinado el numero secreto")
            return
        elif intento < numero_secreto:
            print(f"El numero secreto es mayor que {intento}")
        else:
            print(f"El numero secreto es menor que {intento}")

        adivina_el_numero(numero_secreto, intentos - 1)

numero_secreto = random.randint(1,100)
intentos = 5

print("Adivina el numero secreto")
print(f"Tienes {intentos} intentos")

adivina_el_numero(numero_secreto, intentos)