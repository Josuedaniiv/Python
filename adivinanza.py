import random

def jugar_adivinanza():
    print("¡Bienvenido al juego de adivinanzas!")
    rango_inferior = int(input("Ingresa el número más bajo del rango: "))
    rango_superior = int(input("Ingresa el número más alto del rango: "))
    numero_secreto = random.randint(rango_inferior, rango_superior)
    intentos = 0
    limite_intentos = 3
    puntuaciones = []

    print(f"Estoy pensando en un número entre {rango_inferior} y {rango_superior}. ¿Puedes adivinar cuál es?")

    while True:
        try:
            intento = int(input("Introduce tu suposición: "))
            intentos += 1

            if intento < rango_inferior or intento > rango_superior:
                print(f"Por favor, ingresa un número dentro del rango {rango_inferior}-{rango_superior}.")
                continue

            if intento < numero_secreto:
                print("Demasiado bajo. Intenta nuevamente.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta nuevamente.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                puntuaciones.append(intentos)
                break

            if intentos >= limite_intentos:
                print("¡Agotaste tus intentos! Has perdido.")
                break

        except ValueError:
            print("Por favor, ingresa un número válido.")

    if puntuaciones:
        puntuacion_minima = min(puntuaciones)
        print(f"La puntuación más baja es {puntuacion_minima} intentos.")

jugar_adivinanza()