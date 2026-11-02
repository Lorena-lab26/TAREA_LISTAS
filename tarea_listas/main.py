from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython


lista1 = MiLista(10)
lista2 = ListaPython()


# ---------------- FUNCIONES DE APOYO ----------------

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero.")


def leer_pasajero():
    print("\n--- DATOS DEL PASAJERO ---")

    numero = leer_entero("  Número de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()

    return Pasajero(
        numero, nombre, cedula, edad, fecha, destino, asiento
    )


def cargar_datos_prueba(lista):
    lista.añadir(
        Pasajero(1005, "Diana", "0923456789", 22,
                 "2026-11-15", "Quito", "12A")
    )

    lista.añadir(
        Pasajero(1002, "Ana", "0912345678", 28,
                 "2026-11-15", "Lima", "03C")
    )

    lista.añadir(
        Pasajero(1009, "Luis", "0987654321", 35,
                 "2026-11-20", "Bogotá", "18F")
    )

    lista.añadir(
        Pasajero(1004, "Beto", "0934567890", 16,
                 "2026-11-20", "Quito", "07B")
    )

    lista.añadir(
        Pasajero(1001, "Elena", "0901234567", 41,
                 "2026-11-22", "Lima", "01A")
    )

    print("  Datos de prueba cargados.")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")

    print(" 1. Añadir")
    print(" 2. Listar")
    print(" 3. Insertar en posición")
    print(" 4. Buscar (lineal)")
    print(" 5. Buscar (binaria)")
    print(" 6. Modificar")
    print(" 7. Eliminar por posición")
    print(" 8. Eliminar por número")
    print(" 9. Ordenar ascendente")
    print("10. Ordenar descendente")
    print("11. Reversar")
    print("12. Copiar")
    print("13. Longitud")

    if extras:
        print("14. Filtrar por destino")
        print("15. Mayores de edad")

    print(" C. Cargar datos de prueba")
    print(" 0. Volver")


# ---------------- MENÚ 1: MiLista ----------------

def menu_lista1():

    while True:
        mostrar_opciones("MENÚ 1 - MiLista")

        op = input("Seleccione una opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()

            if lista1.añadir(pasajero):
                print("  Pasajero añadido correctamente.")

        elif op == "2":
            lista1.listar()

        elif op == "3":
            posicion = leer_entero("  Posición donde insertar: ")
            pasajero = leer_pasajero()

            if lista1.insertar(posicion, pasajero):
                print("  Pasajero insertado correctamente.")
            else:
                print("  No se pudo insertar el pasajero.")

        elif op == "4":
            numero = leer_entero("  Número de pasajero a buscar: ")

            posicion = lista1.buscar(numero)

            if posicion != -1:
                print(f"  Encontrado en [{posicion}]:")
                print(" ", lista1.datos[posicion])
            else:
                print("  El pasajero no existe.")

        elif op == "5":
            numero = leer_entero("  Número de pasajero a buscar: ")

            lista1.ordenar_asc()
            posicion = lista1.buscar_binaria(numero)

            if posicion != -1:
                print(f"  Encontrado en [{posicion}]:")
                print(" ", lista1.datos[posicion])
            else:
                print("  El pasajero no existe.")

        elif op == "6":
            numero = leer_entero("  Número de pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()

            if lista1.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  El pasajero no existe.")

        elif op == "7":
            posicion = leer_entero("  Posición que desea eliminar: ")

            pasajero = lista1.eliminar_por_posicion(posicion)

            if pasajero is not None:
                print("  Pasajero eliminado:")
                print(" ", pasajero)
            else:
                print("  Posición no válida.")

        elif op == "8":
            numero = leer_entero("  Número de pasajero: ")

            if lista1.eliminar_por_valor(numero):
                print("  Pasajero eliminado correctamente.")
            else:
                print("  El pasajero no existe.")

        elif op == "9":
            lista1.ordenar_asc()
            print("  Lista ordenada de menor a mayor.")
            lista1.listar()

        elif op == "10":
            lista1.ordenar_desc()
            print("  Lista ordenada de mayor a menor.")
            lista1.listar()

        elif op == "11":
            lista1.reversar()
            print("  Lista reversada.")
            lista1.listar()

        elif op == "12":
            copia = lista1.copiar()

            print("  Copia de la lista:")
            copia.listar()

        elif op == "13":
            print("  Cantidad de pasajeros:", lista1.longitud())

        elif op == "C":
            cargar_datos_prueba(lista1)

        elif op == "0":
            break

        else:
            print("  Opción no válida.")


# ---------------- MENÚ 2: ListaPython ----------------

def menu_lista2():

    while True:
        mostrar_opciones("MENÚ 2 - Lista de Python", extras=True)

        op = input("Seleccione una opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()

            if lista2.añadir(pasajero):
                print("  Pasajero añadido correctamente.")

        elif op == "2":
            lista2.listar()

        elif op == "3":
            posicion = leer_entero("  Posición donde insertar: ")
            pasajero = leer_pasajero()

            if lista2.insertar(posicion, pasajero):
                print("  Pasajero insertado correctamente.")
            else:
                print("  No se pudo insertar el pasajero.")

        elif op == "4":
            numero = leer_entero("  Número de pasajero a buscar: ")

            posicion = lista2.buscar(numero)

            if posicion != -1:
                print(f"  Encontrado en [{posicion}]:")
                print(" ", lista2.pasajeros[posicion])
            else:
                print("  El pasajero no existe.")

        elif op == "5":
            numero = leer_entero("  Número de pasajero a buscar: ")

            lista2.ordenar_asc()
            posicion = lista2.buscar_binaria(numero)

            if posicion != -1:
                print(f"  Encontrado en [{posicion}]:")
                print(" ", lista2.pasajeros[posicion])
            else:
                print("  El pasajero no existe.")

        elif op == "6":
            numero = leer_entero("  Número de pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()

            if lista2.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  El pasajero no existe.")

        elif op == "7":
            posicion = leer_entero("  Posición que desea eliminar: ")

            pasajero = lista2.eliminar_por_posicion(posicion)

            if pasajero is not None:
                print("  Pasajero eliminado:")
                print(" ", pasajero)
            else:
                print("  Posición no válida.")

        elif op == "8":
            numero = leer_entero("  Número de pasajero: ")

            if lista2.eliminar_por_valor(numero):
                print("  Pasajero eliminado correctamente.")
            else:
                print("  El pasajero no existe.")

        elif op == "9":
            lista2.ordenar_asc()
            print("  Lista ordenada de menor a mayor.")
            lista2.listar()

        elif op == "10":
            lista2.ordenar_desc()
            print("  Lista ordenada de mayor a menor.")
            lista2.listar()

        elif op == "11":
            lista2.reversar()
            print("  Lista reversada.")
            lista2.listar()

        elif op == "12":
            copia = lista2.copiar()

            print("  Copia de la lista:")
            copia.listar()

        elif op == "13":
            print("  Cantidad de pasajeros:", lista2.longitud())

        elif op == "14":
            destino = input("  Ingrese el destino: ").strip()

            pasajeros = lista2.filtrar_por_destino(destino)

            if pasajeros:
                print("  Pasajeros con destino a", destino)

                for p in pasajeros:
                    print(" ", p)
            else:
                print("  No hay pasajeros con ese destino.")

        elif op == "15":
            pasajeros = lista2.mayores_de_edad()

            if pasajeros:
                print("  Pasajeros mayores de edad:")

                for p in pasajeros:
                    print(" ", p)
            else:
                print("  No hay pasajeros mayores de edad.")

        elif op == "C":
            cargar_datos_prueba(lista2)

        elif op == "0":
            break

        else:
            print("  Opción no válida.")


# ---------------- MENÚ PRINCIPAL ----------------

def main():

    while True:
        print("\n===== SISTEMA DE PASAJEROS =====")
        print("1. Menú 1 - MiLista")
        print("2. Menú 2 - Lista de Python")
        print("3. Salir")

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            menu_lista1()

        elif op == "2":
            menu_lista2()

        elif op == "3":
            print("¡Hasta pronto!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()