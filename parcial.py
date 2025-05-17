# listas paralelas
nombres = []
cantidades = []

# Menú principal
salir = False

while not salir:
    print("\n Menú:")
    print("1 agregar producto")
    print("2 ver productos agotados")
    print("3 actualizar stock")
    print("4 ver todos los productos")
    print("5 salir")

    opcion = input("Elegir una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto a agregar: ")
        cantidad = int(input("Ingrese la cantidad: "))
        nombres.append(nombre)
        cantidades.append(cantidad)
        print("el producto fue agregado con exito")

    elif opcion == "2":
        print("productos agotados:")
        agotados = False
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print(f"- {nombres[i]}")
                agotados = True
        if not agotados:
            print("No hay productos agotados, todos los productos tienen stock")

    elif opcion == "3":
        producto = input("ingresar el nombre del producto a actualizar: ")
        if producto in nombres:
            index = nombres.index(producto)
            nueva_cantidad = int(input("ingresar el nuevo stock: "))
            cantidades[index] = nueva_cantidad
            print("Stock actualizado.")

    elif opcion == "4":
        print("Listado de productos:")
        for i in range(len(nombres)):
            print(f"{nombres[i]} : {cantidades[i]} unidades")

    elif opcion == "5":
        print("Muchas gracias! vuelva prontos")
        salir = True

    else:
        print("Opción invalida. Intente nuevamente con una opcion del 1 al 5")
