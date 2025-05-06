

def validacion_de_entrada(mensaje, tipo):
    while True:
        try:
            if tipo == "str":
                entrada = input(mensaje).strip().lower()
                if not entrada:
                    print("\nError. El nombre del producto no puede estar vacío.")
                else:                   
                    return entrada
            elif tipo == "float":
                entrada = input(mensaje)
                entrada = float(entrada)
                if entrada <= 0:
                    print("\nError. El precio del producto debe ser mayor a 0.")
                else:                   
                    return entrada
            elif tipo == "int":
                entrada = input(mensaje)
                entrada = int(entrada)
                if entrada <= 0:
                    print("\nError. La cantidad del producto debe ser mayor a 0.")
                else:
                    return entrada
        except ValueError:
            print("\nError. El Precio del producto y la cantidad deben ser números mayores a cero.")


def agregar_producto(nombre, precio, cantidad):
    for producto in productos:
        if list(producto.keys())[0] == nombre:
            print(f"\nEl producto '{nombre}' ya existe en el invetario")
            return        

    producto = {f"{nombre}": (precio,cantidad)}
    productos.append(producto)
    print(f"\nProducto '{nombre}' añadido correctamente.")


def consultar_producto(nombre):
    for producto in productos:
        if list(producto.keys())[0] == nombre:
            print(f"\nNombre = {list(producto.keys())[0]}")
            print(f"Precio = {list(producto.values())[0][0]}")
            print(f"Cantidad = {list(producto.values())[0][1]}")
            return
    
    print(f"\nError. El producto '{nombre}' no se encuentra en la lista de productos almacenados.")


def actualizar_precio(nombre, precio):
    for producto in productos:
        if list(producto.keys())[0] == nombre:
            cantidad = list(producto.values())[0][1]
            productos.remove(producto)
            producto = {f"{nombre}": (precio,cantidad)}
            productos.append(producto)
            print("\nPrecio actualizado correctamente.")
            return
    print(f"\nError. El producto '{nombre}' no se encuentra en la lista de productos almacenados.")


def eliminar_producto(nombre):
    for producto in productos:
        if list(producto.keys())[0] == nombre:
            productos.remove(producto)
            print(f"\nProducto '{nombre}' eliminado correctamente.")
            return
        
    print(f"\nError. El producto '{nombre}' no se encuentra en la lista de productos almacenados.")


total_del_inventario = lambda: sum(list(producto.values())[0][0] * list(producto.values())[0][1] for producto in productos)


productos = []


opcion = " "
while opcion != "6":
    
    print("\n1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")

    opcion = input("\nIngrese una opción: ").strip()

    match opcion:

        case "1":

            nombre = validacion_de_entrada("\nIngrese el nombre del producto: ", "str")
            precio = validacion_de_entrada("\nIngrese el precio del producto: ", "float")
            cantidad = validacion_de_entrada("\nIngrese la cantidad del producto: ", "int")
            
            agregar_producto(nombre, precio, cantidad)

        case "2":
            
            nombre = validacion_de_entrada("\nIngrese el nombre del producto: ", "str")
            
            consultar_producto(nombre)

        case "3":

            nombre = validacion_de_entrada("\nIngrese el nombre del producto: ", "str")
            precio = validacion_de_entrada("\nIngrese el precio actualizado del producto: ", "float")
            
            actualizar_precio(nombre, precio)

        case "4":
            
            nombre = validacion_de_entrada("\nIngrese el nombre del producto: ", "str")
            
            eliminar_producto(nombre)

        case "5":

            if not productos:
                print("\nNo hay productos en el inventario.")
            else:
                print(f"\n{"Nombre":<20} {"Precio":<20} {"Cantidad":<20}")
                print("-" * 60)
                for producto in productos:
                    print(f"{list(producto.keys())[0]:<20} {list(producto.values())[0][0]:<20.2f} {list(producto.values())[0][1]:<20}")

                print(f"\nEl total del costo del inventario es: ${total_del_inventario():.2f}")

        case "6":
            print("\nGracias por usar nuesto sistema de control de inventario\n")
        case _:
            print("\nError. Ingrese un número entre 1 y 6 segun la opción que desea")