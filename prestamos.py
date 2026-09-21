import json
from inventario import cargar_inventario, guardar_inventario

ARCHIVO_PRESTAMOS = "datos/prestamos.json"


def cargar_prestamos():
    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_prestamos(prestamos):
    with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as archivo:
        json.dump(prestamos, archivo, indent=4, ensure_ascii=False)

def registrar_prestamo():
    prestamos = cargar_prestamos()
    inventario = cargar_inventario()

    codigo = input("Ingrese el código del ítem: ").strip()
    usuario = input("Ingrese el nombre del usuario: ").strip()

    item_encontrado = None

    for item in inventario:
        if item["codigo"].lower() == codigo.lower():
            item_encontrado = item
            break

    if item_encontrado is None:
        print("Error: no existe un ítem con ese código.")
        return

    if item_encontrado["cantidad_disponible"] <= 0:
        print("Error: no hay ejemplares disponibles de ese ítem.")
        return

    nuevo_prestamo = {
        "codigo": codigo,
        "usuario": usuario
    }

    prestamos.append(nuevo_prestamo)

    item_encontrado["cantidad_disponible"] -= 1

    guardar_prestamos(prestamos)
    guardar_inventario(inventario)

    print(
        f'Préstamo registrado para el ítem {codigo}. '
        f'Disponibles: {item_encontrado["cantidad_disponible"]}'
    )

def registrar_devolucion():
    prestamos = cargar_prestamos()
    inventario = cargar_inventario()

    codigo = input("Ingrese el código del ítem: ").strip()
    usuario = input("Ingrese el nombre del usuario: ").strip()

    prestamo_encontrado = None

    for prestamo in prestamos:
        if (
            prestamo["codigo"].lower() == codigo.lower()
            and prestamo["usuario"].lower() == usuario.lower()
        ):
            prestamo_encontrado = prestamo
            break

    if prestamo_encontrado is None:
        print("Error: no existe un préstamo registrado para ese usuario y ese ítem.")
        return

    item_encontrado = None

    for item in inventario:
        if item["codigo"].lower() == codigo.lower():
            item_encontrado = item
            break

    if item_encontrado is None:
        print("Error: el ítem no existe en el inventario.")
        return

    prestamos.remove(prestamo_encontrado)
    item_encontrado["cantidad_disponible"] += 1

    guardar_prestamos(prestamos)
    guardar_inventario(inventario)

    print(
        f"Devolución registrada para el ítem {codigo}. "
        f"Disponibles: {item_encontrado['cantidad_disponible']}"
    )
