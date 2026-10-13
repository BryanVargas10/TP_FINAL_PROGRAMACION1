
def menu_proyectos(lista_proyectos):

    opcion = ""

    while opcion != "3":

        print("PROYECTOS")
        print("1- Crear proyecto")
        print("2- Mostrar proyectos")
        print("3 - Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            proyecto = input("Ingrese el nombre del proyecto: ")

            if proyecto != "":
                lista_proyectos = lista_proyectos + [proyecto]
                print("Proyecto creado correctamente.")
            else:
                print("El nombre no puede estar vacio.")

        elif opcion == "2":

            if len(lista_proyectos) == 0:
                print("No hay proyectos creados.")
            else:
                for i in range(len(lista_proyectos)):
                    print(i + 1, "-", lista_proyectos[i])

        elif opcion == "3":
            print("Volviendo al menu principal.")

        else:
            print("Opcion incorrecta.")

    return lista_proyectos
