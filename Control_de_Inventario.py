############################# Mensaje de bienvenida ###############################
print("")
print("=" * 60)
print("     Bienvenido al sistema de control de inventario 📦​")
print("=" * 60)
######################################################################################


# Definición de funciones.

def validacion_de_entrada(mensaje, tipo): # Función que valida la entrada de los datos, nombre del producto, precio y cantidad, sirve para datos tipo strings, flotantes y enteros.
    while True:
        try:
            if tipo == "str":
                entrada = input(mensaje).strip().lower()
                if not entrada:
                    print("\n¡Error! ⚠️. El nombre del producto no puede estar vacío.")
                else:                   
                    return entrada
            elif tipo == "float":
                entrada = input(mensaje)
                entrada = float(entrada)
                if entrada <= 0:
                    print("\n¡Error! ⚠️. El precio del producto debe ser mayor a 0.")
                else:                   
                    return entrada
            elif tipo == "int":
                entrada = input(mensaje)
                entrada = int(entrada)
                if entrada <= 0:
                    print("\n¡Error! ⚠️. La cantidad del producto debe ser mayor a 0.")
                else:
                    return entrada
        except ValueError:
            print("\n¡Error! ⚠️. El Precio del producto y la cantidad deben ser números mayores a cero.")


def agregar_producto(nombre, precio, cantidad): # Función que agrega un producto al inventario, si el producto ya existe, no lo agrega y manda un mensaje amigable.
    for producto in productos:
        if list(producto.keys())[0] == nombre:
            print(f"\nEl producto '{nombre}' ya existe en el invetario ☝️​.​")
            return        

    producto = {f"{nombre}": (precio,cantidad)}
    productos.append(producto)
    print(f"\nProducto '{nombre}' añadido correctamente 👍​.")


def consultar_producto(nombre): # Función que consulta un producto en el inventario, si el producto no existe, manda un mensaje amigable.
    for producto in productos:
        if list(producto.keys())[0] == nombre:
            print(f"\nNombre = {list(producto.keys())[0]}")
            print(f"Precio = ${list(producto.values())[0][0]}")
            print(f"Cantidad = {list(producto.values())[0][1]}")
            return
    
    print(f"\nEl producto '{nombre}' no se encuentra en la lista de productos almacenados 😥.​")


def actualizar_precio(nombre, precio): # Función que actualiza el precio de un producto en el inventario, si el producto no existe, manda un mensaje amigable.
    for producto in productos:
        if list(producto.keys())[0] == nombre:
            cantidad = list(producto.values())[0][1]
            productos.remove(producto)
            producto = {f"{nombre}": (precio,cantidad)}
            productos.append(producto)
            print("\nPrecio actualizado correctamente 👍​.")
            return
    print(f"\nEl producto '{nombre}' no se encuentra en la lista de productos almacenados 😥.​")


def eliminar_producto(nombre): # Función que elimina un producto del inventario, si el producto no existe, manda un mensaje amigable.
    for producto in productos:
        if list(producto.keys())[0] == nombre:
            productos.remove(producto)
            print(f"\nProducto '{nombre}' eliminado correctamente 👍​.")
            return
        
    print(f"\nEl producto '{nombre}' no se encuentra en la lista de productos almacenados 😥.​")


total_del_inventario = lambda: sum(list(producto.values())[0][0] * list(producto.values())[0][1] for producto in productos) # Función lambda que calcula el costo total del inventario, multiplicando el precio por la cantidad de cada producto y sumando todos los productos.


productos = [] # Lista vacía que almacena los productos, cada producto es un diccionario con el nombre del producto como clave y una tupla con el precio y la cantidad como valor.


opcion = " "
while opcion != "6": # Ciclo while que se ejecuta hasta que el usuario ingresa la opción 6 para salir del programa.
    
    # Menú de opciones
    print("\n1. Añadir producto 📦​")
    print("2. Consultar producto 🔎")
    print("3. Actualizar precio 💲")
    print("4. Eliminar producto 🗑️")
    print("5. Calcular valor total del inventario 📋")
    print("6. Salir 🏃🚪")

    opcion = input("\nIngrese una opción según la acción que desea realizar: ").strip()

    match opcion:

        case "1": # Agregar producto

            nombre = validacion_de_entrada("\nIngrese el nombre del producto: ", "str")
            precio = validacion_de_entrada("\nIngrese el precio del producto 💲: ", "float")
            cantidad = validacion_de_entrada("\nIngrese la cantidad del producto: ", "int")
            
            agregar_producto(nombre, precio, cantidad)

        case "2": # Consultar producto
            
            nombre = validacion_de_entrada("\nIngrese el nombre del producto que desea consultar 🔎: ", "str")
            
            consultar_producto(nombre)

        case "3": # Actualizar precio

            nombre = validacion_de_entrada("\nIngrese el nombre del producto que desea actualizar: ", "str")
            precio = validacion_de_entrada("\nIngrese el precio actualizado del producto 💲: ", "float")
            
            actualizar_precio(nombre, precio)

        case "4": # Eliminar producto
            
            nombre = validacion_de_entrada("\nIngrese el nombre del producto que desea eliminar 🗑️: ", "str")
            
            eliminar_producto(nombre)

        case "5": # Calcular valor total del inventario

            if not productos:
                print("\nNo hay productos en el inventario aún. 😥​")
            else:
                print(f"\n{"Nombre":<20} {"Precio":<20} {"Cantidad":<20}")
                print("-" * 60)
                for producto in productos:
                    print(f"{list(producto.keys())[0]:<20} {list(producto.values())[0][0]:<20.2f} {list(producto.values())[0][1]:<20}")

                print(f"\nEl total del costo del inventario es: ${total_del_inventario():.2f}")

        case "6": # Salir del programa
            print("\n✅ ​Gracias por usar nuesto sistema de control de inventario ✅​\n")
        case _: # En caso de que el usuario elija una opción que no está disponible, el programa muestra un mensaje amigable, indicándole su error.
            print("\n¡Error! ⚠️. Ingrese un número entre 1 y 6 segun la opción que desea")