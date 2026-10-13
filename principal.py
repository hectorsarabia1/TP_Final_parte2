from validaciones import validar_rango, es_par, es_primo, es_multiplo

usuario_autenticado = False

while not usuario_autenticado:
    print("--- INICIO DE SESIÓN / REGISTRO ---")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. Salir")

    opcion_ingreso = input("Seleccione una opción (1-3): ")

    if opcion_ingreso == "1":
        usuario = input("Ingrese su nombre de usuario: ")
        clave = input("Ingrese su contraseña: ")

        print("Inicio de sesión exitoso.")
        usuario_autenticado = True

    elif opcion_ingreso == "2":
        nuevo_usuario = input("Ingrese un nuevo nombre de usuario: ")
        nueva_clave = input("Ingrese una contraseña: ")

        print("Registro completado con éxito.")
        usuario_autenticado = True

    elif opcion_ingreso == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, reintente.\n")


ejecutando_menu = usuario_autenticado

proyecto = ""
tabla = ""
variable = ""

cantidad = 0
suma = 0
maximo = 0
minimo = 0 

while ejecutando_menu:
    print("\n--- MENÚ PRINCIPAL ---")
    print("a) Proyectos")
    print("b) Tablas")
    print("c) Variables")
    print("d) Mostrar")
    print("e) Estadística")
    print("f) Salir")

    opcion_menu = input("Seleccione una opción: ")

    if opcion_menu == "a":
        print("\n --- PROYECTOS ---")
        print("1 - Crear proyectos.")
        print("2 - Mostrar proyectos.")
        print("3 - Volver.")
        opcion_proyecto = input("Seleccione una opcion: ")
        if opcion_proyecto == "1":
            proyecto = input("Ingrese el nombre del proyecto: ")
            print("Proyecto creado correctamente.")
        elif opcion_proyecto == "2":
            if proyecto == "":
                print("No hay ningun proyecto creado.")
            else:
                print("Proyecto", proyecto)
        elif opcion_proyecto == "3":
            print("Volviendo al menu principal...")
        else:
            print("Opcion invalida. Ingrese una opcion correcta.")

    elif opcion_menu == "b":
        print("\n --- TABLAS ---")
        print("1 - Crear tabla.")
        print("2 - Mostrar tabla.")
        print("3 - Volver.")
        opcion_tabla = input("Seleccion una opcion: ")
        if opcion_tabla == "1":
            if proyecto == "":
                print("Primero debe crear un proyecto.")
            else:
                tabla = input("Ingrese el nombre de la tabla: ")
                print("Tabla creada correctamente")
        elif opcion_tabla == "2":
            if tabla == "":
                print("No hay ninguna tabla creada.")
            else:
                print("Tabla: ", tabla)
        elif opcion_tabla == "3":
            print("Volviendo al menu principal...")
        else:
            print("Opcion invalida. Ingrese una opcion correcta.")

    elif opcion_menu == "c":
        print("\n --- Variables ---")
        
    elif opcion_menu == "d":
        print("\n --- MOSTRAR INFORMACIÓN ---")
        if proyecto == "":
            print("No hay ningún proyecto creado.")
        elif tabla == "":
            print("Proyecto activo:", proyecto)
            print("No hay ninguna tabla creada para este proyecto.")
        elif variable == "":
            print("Proyecto:", proyecto)
            print("Tabla:", tabla)
            print("No hay ninguna variable cargada en esta tabla.")
        else:
            print("Proyecto:", proyecto)
            
    elif opcion_menu == "e":
        print("Entrando a Estadística...")
        
    elif opcion_menu == "f":
        print("Saliendo del programa...")
        ejecutando_menu = False
    else:
        print("Opción inválida. Por favor, reintente.")
