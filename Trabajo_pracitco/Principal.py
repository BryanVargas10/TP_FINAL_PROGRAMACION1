usuario_registrado = ""
contrasenia_registrada = ""

opcion = ""

while opcion != "3":

   
    print(" sistema de procesamiento")
    print("1 - iniciar sesion")
    print("2 - registrarse")
    print("3 - Salir")

    opcion = input("Ingrese una opcion ")

    if opcion == "1":

        print("iniciar seseion")

        usuario = input("Ingrese su usuario: ")
        contrasenia = input("Ingrese su contraseña: ")

        if usuario == usuario_registrado and contrasenia == contrasenia_registrada:
            
            print("Inicio de sesion correcto.")

            opcion_menu = ""

            while opcion_menu != "f":

                print("MENU ")
                print("a - Proyectos")
                print("b - Tablas")
                print("c - Variables")
                print("d - Mostrar")
                print("e - Estadistica")
                print("f - Salir")
                

                opcion_menu = input("Seleccione una opcion: ")

                if opcion_menu == "a":
                    print("PROYECTOS ")
                    print("1 - Crear proyecto")
                    print("2 - Mostrar proyectos")

                    opcion_proyecto = input("Seleccione una opcion: ")

                    if opcion_proyecto == "1":
                        proyecto = input("Ingrese el nombre del proyecto: ")

                        if proyecto != "":
                            print("Proyecto creado correctamente")
                        else:
                            print("El nombre no puede estar vacio.")

                    elif opcion_proyecto == "2":
                        print("proyectos disponibles.")

                    else:
                        print("Opción incorrecta.")

                elif opcion_menu == "b":
                    print(" TABLAS ")
                    print("1 - Crear tabla")
                    print("2 - Modificar tabla")

                    opcion_tabla = input("Seleccione una opcion: ")

                    if opcion_tabla == "1":
                        print("Tabla creada correctamete ")

                    elif opcion_tabla == "2":
                        print("Tabla modificada correctamente ")

                    else:
                        print("Opción incorrecta.")

                elif opcion_menu == "c":
                    print("\n--- VARIABLES ---")
                    print("1 - Crear variable")
                    print("2 - Cargar variable")
                    print("3 - Modificar variable")

                    opcion_variable = input("Seleccione una opcion: ")

                    if opcion_variable == "1":
                        print("Variable creada correctamente.")

                    elif opcion_variable == "2":
                        print("Variable cargada correctamente.")

                    elif opcion_variable == "3":
                        print("Variable modificada correctamente.")

                    else:
                        print("Opción incorrecta.")

                elif opcion_menu == "d":
                    print(" MOSTRAR ")
                    print("Mostrar información disponible en una tabla.")

                elif opcion_menu == "e":
                    print(" ESTADÍSTICA ")
                    print("1 - Conteos y frecuencias")
                    print("2 - Máximos y mínimos")
                    print("3 - Promedio")
                    print("4 - Dispersión")
                    print("5 - Posición")

                    opcion_estadistica = input("Seleccione una opcion: ")

                    if opcion_estadistica == "1":
                        print("Conteos y frecuencias.")

                    elif opcion_estadistica == "2":
                        print("Máximos y mínimos.")

                    elif opcion_estadistica == "3":
                        print("Promedio.")

                    elif opcion_estadistica == "4":
                        print("Medidas de dispersión.")

                    elif opcion_estadistica == "5":
                        print("Medidas de posición.")

                    else:
                        print("Opción incorrecta.")

                elif opcion_menu == "f":
                    print("\nCerrando sesión...")

                else:
                    print("\nOpción incorrecta.")

        else:
            print("\nUsuario o contraseña incorrectos.")

    elif opcion == "2":

        print("registro")

        usuario_registrado = input("Ingrese un nombre de usuario: ")
        contrasenia_registrada = input("Ingrese una contraseña: ")

        if usuario_registrado == "" or contrasenia_registrada == "":
            print("El usuario y la contraseña no pueden estar vacíos.")
            usuario_registrado = ""
            contrasenia_registrada = ""

        else:
            print("Usuario registrado correctamente.")

    elif opcion == "3":
        print("Programa finalizado.")

    else:
        print("Opción incorrecta.")
        
