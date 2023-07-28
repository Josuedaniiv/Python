# Definimos la función para sumar
def sumar(num1, num2):
    return num1 + num2

# Definimos la función para restar
def restar(num1, num2):
    return num1 - num2

# Definimos la función para multiplicar
def multiplicar(num1, num2):
    return num1 * num2

# Definimos la función para dividir
def dividir(num1, num2):
    # Verificamos que el divisor no sea cero
    if num2 == 0:
        print("¡Error! No se puede dividir entre cero.")
        return None
    else:
        return num1 / num2

# Pedimos al usuario que ingrese los números y la operación deseada
operacion = input("¿Qué operación desea realizar? (+, -, *, /): ")
num1 = None
while num1 is None:
    try:
        num1 = float(input("Ingrese el primer número: "))
    except ValueError:
        print("Entrada no válida. Intente nuevamente.")
num2 = None
while num2 is None:
    try:
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Entrada no válida. Intente nuevamente.")

# Realizamos la operación correspondiente
if operacion == "+":
    resultado = sumar(num1, num2)
elif operacion == "-":
    resultado = restar(num1, num2)
elif operacion == "*":
    resultado = multiplicar(num1, num2)
elif operacion == "/":
    resultado = dividir(num1, num2)
else:
    print("Operación no válida.")
    resultado = None

# Mostramos el resultado al usuario
if resultado is not None:
    print(f"El resultado es: {resultado:.4f}")

# Preguntamos al usuario si quiere realizar otra operación
otra_operacion = input("¿Desea realizar otra operación? (s/n): ")
while otra_operacion.lower() == "s":
    operacion = input("¿Qué operación desea realizar? (+, -, *, /): ")
    num1 = None
    while num1 is None:
        try:
            num1 = float(input("Ingrese el primer número: "))
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
    num2 = None
    while num2 is None:
        try:
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

    # Realizamos la operación correspondiente
    if operacion == "+":
        resultado = sumar(num1, num2)
    elif operacion == "-":
        resultado = restar(num1, num2)
    elif operacion == "*":
        resultado = multiplicar(num1, num2)
    elif operacion == "/":
        resultado = dividir(num1, num2)
    else:
        print("Operación no válida.")
        resultado = None

    # Mostramos el resultado al usuario
    if resultado is not None:
        print(f"El resultado es: {resultado:.4f}")

    # Preguntamos al usuario si quiere realizar otra operación
    otra_operacion = input("¿Desea realizar otra operación? (s/n): ")