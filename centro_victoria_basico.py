# PROTOTIPO BASICO: Registro de ingresos y salidas
# Centro Victoria
# Los datos usados para la demostracion deben ser ficticios.

ARCHIVO = "registros_centro_victoria.txt"


def cargar_registros():
    registros = []
    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
        for linea in archivo:
            datos = linea.strip().split("|")
            if len(datos) == 5:
                registros.append(datos)
        archivo.close()
    except FileNotFoundError:
        archivo = open(ARCHIVO, "w", encoding="utf-8")
        archivo.close()
    return registros


def guardar_registros(registros):
    archivo = open(ARCHIVO, "w", encoding="utf-8")
    for registro in registros:
        linea = "|".join(registro)
        archivo.write(linea + "\n")
    archivo.close()


def registrar_ingreso(registros):
    nombre = input("Nombre ficticio: ").strip()
    responsable = input("Responsable ficticio: ").strip()

    if nombre == "" or responsable == "":
        print("Error: debe completar los dos campos.")
    else:
        codigo = "CV-" + str(len(registros) + 1).zfill(4)
        registro = [codigo, nombre, responsable, "INGRESADO", "-"]
        registros.append(registro)
        guardar_registros(registros)
        print("Ingreso registrado. Codigo:", codigo)


def buscar_registro(registros):
    codigo = input("Ingrese el codigo: ").strip().upper()
    encontrado = False

    for registro in registros:
        if registro[0] == codigo:
            print("Codigo:", registro[0])
            print("Nombre:", registro[1])
            print("Responsable:", registro[2])
            print("Estado:", registro[3])
            print("Fecha de salida:", registro[4])
            encontrado = True

    if encontrado == False:
        print("No se encontro el registro.")


def registrar_salida(registros):
    codigo = input("Codigo del registro: ").strip().upper()
    encontrado = False

    for registro in registros:
        if registro[0] == codigo:
            encontrado = True
            if registro[3] == "INGRESADO":
                fecha = input("Fecha de salida (DD/MM/AAAA): ").strip()
                if fecha == "":
                    print("Debe ingresar la fecha.")
                else:
                    registro[3] = "SALIDA REGISTRADA"
                    registro[4] = fecha
                    guardar_registros(registros)
                    print("Salida registrada correctamente.")
            else:
                print("Este registro ya tiene salida.")

    if encontrado == False:
        print("No se encontro el codigo.")


def mostrar_registros(registros):
    if len(registros) == 0:
        print("No hay registros guardados.")
    else:
        registros.sort()
        for registro in registros:
            print(registro[0], "|", registro[1], "|", registro[2], "|", registro[3], "|", registro[4])


def menu():
    registros = cargar_registros()
    opcion = ""

    while opcion != "0":
        print("\n=== CENTRO VICTORIA ===")
        print("1. Registrar ingreso")
        print("2. Registrar salida")
        print("3. Buscar registro")
        print("4. Mostrar registros ordenados")
        print("0. Salir")
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            registrar_ingreso(registros)
        elif opcion == "2":
            registrar_salida(registros)
        elif opcion == "3":
            buscar_registro(registros)
        elif opcion == "4":
            mostrar_registros(registros)
        elif opcion == "0":
            print("Fin del programa.")
        else:
            print("Opcion incorrecta. Intente nuevamente.")


menu()
