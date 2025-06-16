#zapatilla 

reservas = {}
clave_reserva = "EstoyEnListaDeReserva"
stock_total = 20
stock_reservado = 0

def mostrar_menu():
    print(" 1.- Hacer reserva")
    print("2.- Buscar reserva")
    print("3.- Cancelar reserva")
    print(" 4.- Salir ")


def hacer_reserva():
    global stock_total, stock_reservado, reservas

    if stock_total < 1:
        print("No hay más stock disponible. Cerrando sistema.")
        exit()

    while True:
        nombre_cliente = input("Ingrese su nombre para la reserva: ").strip()
        if nombre_cliente.isalpha():
            break
        else:
            print("Nombre no válido. Ingrese solo letras.")

    if nombre_cliente in reservas:
        print("Ya tiene una reserva registrada. Cerrando sistema.")
        exit()

    clave = input("Ingrese la clave de confirmación: ")
    if clave == clave_reserva:
        print(f"Reserva confirmada para {nombre_cliente}")
        reservas[nombre_cliente] = {"pares": 1}
        stock_total -= 1
        stock_reservado += 1
    else:
        print("Clave incorrecta. No se pudo completar la reserva.")

def buscar_reserva():
    global stock_total, stock_reservado, reservas

    if not reservas:
        print("No hay reservas registradas.")
        return

    buscar_nombre = input("Ingrese el nombre a buscar: ").strip()
    if buscar_nombre in reservas:
        info = reservas[buscar_nombre]
        print(f"Reserva encontrada para {buscar_nombre}")
        print(f"Pares reservados: {info['pares']}")

        extra = input("¿Desea agregar 1 par extra como VIP? (s/n): ").lower()
        if extra == "s":
            if info["pares"] == 2:
                print("Ya ha reservado el máximo de pares permitidos.")
            elif stock_total > 0:
                info["pares"] = 2
                stock_total -= 1
                stock_reservado += 1
                print("Reserva VIP confirmada. Ahora tiene 2 pares.")
            else:
                print("No hay más stock disponible para VIP.")
        else:
            print("No se modificó la reserva.")
    else:
        print("No se encontró una reserva con ese nombre.")

def cancelar_reserva():
    global stock_total, stock_reservado, reservas

    if not reservas:
        print("No hay reservas registradas.")
        return

    nombre = input("Ingrese el nombre de la reserva a cancelar: ").strip()
    if nombre in reservas:
        cantidad = reservas[nombre]["pares"]
        del reservas[nombre]
        stock_total += cantidad
        stock_reservado -= cantidad
        print(f"Reserva de {nombre} cancelada. Se liberaron {cantidad} pares.")
    else:
        print("No se encontró una reserva con ese nombre.")

def seleccionar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = seleccionar_opcion()
        if opcion == 1:
            hacer_reserva()
        elif opcion == 2:
            buscar_reserva()
        elif opcion == 3:
            cancelar_reserva()
        elif opcion == 4:
            print("Gracias por usar el sistema. Cerrando...")
            exit()

ejecutar_programa()
