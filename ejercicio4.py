import time
seller = [[12, 15, 10, 18],
            [8, 14, 16, 12],
            [20, 18, 15, 22]]


def showMenu():
    print(f"""
    ------ MENU DE VENTAS DE LA EMPRESA ------
    1. Ver la información de la empresa.
    2. Cambiar las ventas de un vendedor.
    0. Salir.
    """)
    selectOption()

def selectOption():
    option = int(input("Seleccione una opción: "))
    if option == 1:
        option1()
    elif option == 2:
        option2()
    else: 
        print("Finalizando programa.")
        SystemExit

def option1():
    sellerNum = 0

    print("-------- RESUMEN VENDEDORES --------")
    for line in seller:
        sellerNum += 1
        print(f"Vendedor: {sellerNum}: {line}")
        for week in range(len(line)):
            print(f"Semana {week +1}: {line[week]}")

    sellerNum = 0

    print("--- TOTAL DE VENTAS POR VENDEDOR ---")
    for line in seller:
        sellerNum += 1
        amount = sum(line)
        print(f"Ventas de vendedor {sellerNum}: {amount}")

    amount = 0
    print("---------- VENTAS TOTALES ----------")
    for line in seller:
        amount += sum(line)
    print(f"total de ventas: {amount}")


    print("---------- VENDEDOR CON MÁS VENTAS ----------")
    maxSales = sum(max(seller))
    bestSeller = seller.index(max(seller)) + 1
    print(f"El vendedor {bestSeller} es el vendedor que más vendió con {maxSales} ventas.")

    print("------ SEMANA CON MAYOR VOLUMEN DE VENTAS ------")

    maxVolume = 0
    bestWeek = 0

    for column in range(4):
        total = 0
        for line in range(3):
            total += seller[line][column]
        if total > maxVolume:
            maxVolume = total
            bestWeek = column + 1

    print(f"La semana {bestWeek} fue la semana con mayor volumen de ventas con un total de {maxVolume} ventas.")

    print("---------- PROMEDIO DE VENTAS ----------")   
    average = amount / (len(seller) * len(seller[0]))
    print(f"EL Promedio de ventas es: {average}")

    returnMenu = input("pulse [Enter] para volver al menú principal")
    showMenu()

def option2():
    while True:
        sellerInput = int(input("Seleccione el numero del vendedor (1 a 3): ")) - 1
        if sellerInput >= 0 and sellerInput <= 2:
            print(seller[sellerInput])
            salesInput = int(input("Escriba la posisión de las venta que desea modificar (de 1 a 4)")) - 1
            if salesInput >=0 and salesInput <= 3:
                salesChange = int(input("Ingrese el nuevo valor (solo numero enteros): "))
                seller[sellerInput][salesInput] = salesChange
                print(f"Se cambio el valor correctamente, lista actualizada: {seller[sellerInput]}")
                print("volviendo al menu...")
                time.sleep(3)

                showMenu()
                break
            else: print("Dato invalido, intentelo de nuevo")
        else: 
            print("Dato invalido, intentelo de nuevo")


showMenu()