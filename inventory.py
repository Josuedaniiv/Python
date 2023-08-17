inventario = {}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    inventario[nombre] = cantidad
    print("Producto agregado al inventario.")

def mostrar_inventario():
    print("Inventario:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    main()