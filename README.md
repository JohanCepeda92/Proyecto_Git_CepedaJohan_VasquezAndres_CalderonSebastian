# BiblioStock - Biblioteca Horizonte

## Descripción

BiblioStock es un sistema sencillo de gestión de inventario y préstamos para la Biblioteca Comunitaria Horizonte.

El proyecto fue desarrollado en Python y se ejecuta desde la terminal (CLI).

El sistema permite:

- Registrar ítems.
- Listar los ítems registrados.
- Buscar ítems por código o título.
- Registrar préstamos.
- Registrar devoluciones.
- Actualizar la cantidad disponible de cada ítem.
- Guardar la información mediante archivos JSON.

---

## Integrantes

- Johan Nicolás Cepeda Díaz
- Andrés Felipe Vásquez Velasco
- Sebastián Andrés Calderón Silva

---

## Funcionalidades

### Gestión de inventario

El sistema permite registrar libros y otros materiales indicando:

- Código
- Título
- Autor
- Categoría
- Cantidad total
- Ubicación

También permite listar y buscar los ítems registrados.

### Gestión de préstamos

El sistema permite:

- Registrar un préstamo asociando un ítem con un usuario.
- Validar que el ítem exista.
- Validar que haya ejemplares disponibles.
- Disminuir automáticamente la cantidad disponible.

### Gestión de devoluciones

El sistema permite:

- Registrar la devolución de un ítem.
- Validar que exista un préstamo correspondiente.
- Aumentar nuevamente la cantidad disponible.
- Eliminar el préstamo registrado una vez realizada la devolución.

---

## Estructura del proyecto

```text
BiblioStock/
│
├── datos/
│   ├── inventario.json
│   └── prestamos.json
│
├── inventario.py
├── prestamos.py
├── main.py
├── .gitignore
└── README.md