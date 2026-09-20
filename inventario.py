import json


ARCHIVO_INVENTARIO = "datos/inventario.json"


def cargar_inventario():
    try:
        with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_inventario(inventario):
    with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)

def registrar_item():
    inventario = cargar_inventario()

    codigo = input("Ingrese el código del ítem: ").strip()
    titulo = input("Ingrese el título: ").strip()
    autor = input("Ingrese el autor: ").strip()
    categoria = input("Ingrese la categoría: ").strip()
    cantidad = int(input("Ingrese la cantidad total: "))
    ubicacion = input("Ingrese la ubicación: ").strip()

    nuevo_item = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "cantidad_total": cantidad,
        "cantidad_disponible": cantidad,
        "ubicacion": ubicacion
    }

    inventario.append(nuevo_item)
    guardar_inventario(inventario)

    print(f'Ítem "{titulo}" registrado exitosamente. Disponibles: {cantidad}')

def listar_items():
    inventario = cargar_inventario()

    if not inventario:
        print("No hay ítems registrados.")
        return

    print("\n========== INVENTARIO ==========")

    for item in inventario:
        print(f"Código: {item['codigo']}")
        print(f"Título: {item['titulo']}")
        print(f"Autor: {item['autor']}")
        print(f"Categoría: {item['categoria']}")
        print(f"Cantidad total: {item['cantidad_total']}")
        print(f"Cantidad disponible: {item['cantidad_disponible']}")
        print(f"Ubicación: {item['ubicacion']}")
        print("--------------------------------")

        