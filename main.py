print("BiblioStock - Biblioteca Horizonte")
print("Sistema de inventario y préstamos")

def mostrar_menu():
    print("\n==========================================")
    print("BIBLIOSTOCK CLI - BIBLIOTECA HORIZONTE")
    print("==========================================")
    print("1. Registrar ítem")
    print("2. Listar ítems")
    print("3. Buscar ítem")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Salir")
    print("==========================================")

from inventario import registrar_item, listar_items, buscar_item


print("BiblioStock - Biblioteca Horizonte")
print("Sistema de inventario y préstamos")


def mostrar_menu():
    print("\n==========================================")
    print("BIBLIOSTOCK CLI - BIBLIOTECA HORIZONTE")
    print("==========================================")
    print("1. Registrar ítem")
    print("2. Listar ítems")
    print("3. Buscar ítem")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Salir")
    print("==========================================")


def ejecutar_menu():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_item()

        elif opcion == "2":
            listar_items()

        elif opcion == "3":
            buscar_item()

        elif opcion == "4":
            print("Función de préstamos próximamente.")

        elif opcion == "5":
            print("Función de devoluciones próximamente.")

        elif opcion == "6":
            print("Gracias por utilizar BiblioStock.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_menu()