"""
This module has the main function of the application. It allows the user to interact with system.
Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>
"""

# pylint: disable= import-error
import sys
from project import user_auth
from project import subscription
from project import notification
from project import client as cliente


def login():
    """This function allows the user to log in the system."""
    username = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    auth = user_auth.Authentication(username, password)

    if auth.authenticate():
        return auth.userdata()
    return None


# pylint: disable=line-too-long
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# That was disabled because we need to have a lot of branches and statements to have a good menu.
def main():
    """This is the main function of the application. It allows the user to interact with the system."""
    user = None
    print("Bienvenido a la aplicación FocusToDo\n")
    print("Le informamos que para utilizar la aplicación debe iniciar sesión\n")

    user = login()
    while user is None:
        print("Usuario o contraseña incorrectos, intente de nuevo.")
        user = login()

    client = cliente.Client()
    subscription_instance = subscription.Subscription(
        user.get_username()
    )  # Instantiate the class

    # pylint: disable=invalid-name
    # We disabled that warning because we are following the convention of the class name

    OPTIONS = """
    x = Salir
    1. Crear Tarea
    2. Mostrar Tareas
    3. Eliminar Tarea
    4. Crear Subtarea
    5. Eliminar Subtarea
    6. Crear Proyecto
    7. Agregar Tarea a Proyecto
    8. Eliminar Proyecto
    9. Mostrar Proyectos
    10. Iniciar Pomodoro
    11. Marcar Tarea como Realizada
    12. Marcar Subtarea como Realizada
    13. Marcar Proyecto como Realizado
    14. Personalizar Pomodoro
    15. Ver Planes de Suscripción
    16. Pagar Suscripción
    """

    OPTIONS_PREMIUM = """
    OPCIONES PREMIUM:
    18. Ver Estadísticas de Productividad
    19. Crear Carpeta
    20. Asignar Proyecto a Carpeta
    21. Ver Carpetas
    """

    if client.premium is True:
        print(OPTIONS + OPTIONS_PREMIUM)
    else:
        print(OPTIONS)

    # Menú de opciones
    # pylint: disable=too-many-nested-blocks
    # We disabled that warning because we need to nest to have a good Menu

    while True:

        option = input(
            "\nPor favor seleccione una opción: (Escriba 0 si desea ver las opciones nuevamente): "
        )

        if option == "1":
            print("\n==========Creando Tarea===========")
            task_name = input("Ingrese el nombre de la tarea: ")
            # Si retorna False, la tarea ya existe
            if client.create_task(task_name) is False:
                print("La tarea " + task_name + " ya existe, intente con otro nombre.")
            else:
                print("Tarea: " + task_name + " creada con éxito")

        elif option == "0":
            if (
                client.premium is True
            ):  # Si el usuario es premium, se muestran todas las opciones
                print(OPTIONS + OPTIONS_PREMIUM)
            else:
                print(OPTIONS)

        elif option == "2":
            print("\n==========Mostrando Tareas===========")
            client.view_tasks()

        elif option == "3":
            print("\n==========Eliminando Tarea===========")
            task_name = input("Ingrese el nombre de la tarea a eliminar: ")
            # Si retorna False, la tarea no existe
            if client.delete_task(task_name) is False:
                print("La tarea " + task_name + " no existe")
            else:
                print("Tarea eliminada")

        elif option == "4":
            print("\n==========Creando Subtarea===========")
            exist = False
            exist_task = False
            task_super = input(
                "Escriba el nombre de la tarea a la que pertenece la subtarea: "
            )
            # Verificar si la tarea a la que se quiere añadir la subtarea existe
            for task in client.tasks:
                if task_super == task.get_name():
                    exist_task = True
                    subtask = input("Ingrese el nombre de la subtarea: ")
                    # Verificar si la subtarea ya existe
                    for sub in task.subtasks:
                        if subtask == sub.get_name():
                            exist = True
                    # Si la subtarea no existe, se crea
                    if exist is False:
                        task.add_component(client.create_subtask(subtask))
                        print("Subtarea: " + subtask + " creada con éxito")
                        break
                    print(f"La subtarea {subtask} ya existe, intente con otro nombre.")
                    break
            # Si la tarea no existe, se avisa al usuario
            if exist_task is False:
                print(
                    f"La tarea {task_super} no existe, cree la tarea primero y luego añade la subtarea"
                )

        elif option == "5":
            print("\n==========Eliminando Subtarea===========")
            exist = False
            exist_task = False
            task_super = input(
                "Escriba el nombre de la tarea a la que pertenece la subtarea a eliminar: "
            )
            # Verificar si la tarea a la que se quiere añadir la subtarea existe
            for task in client.tasks:
                if task_super == task.get_name():
                    exist_task = True
                    # Verificar si la subtarea a eliminar existe
                    subtask = input("Ingrese el nombre de la subtarea a eliminar: ")
                    for sub in task.subtasks:
                        if subtask == sub.get_name():
                            exist = True
                            task.remove_component(subtask)
                            print("Subtarea: " + subtask + " eliminada con éxito")
                            break
                    # Si la subtarea no existe, se avisa al usuario
                    if exist is False:
                        print(f"La subtarea {subtask} no existe.")
                        break
            # Si la tarea no existe, se avisa al usuario
            if exist_task is False:
                print(f"La tarea {task_super} no existe, intente con otro nombre.")

        elif option == "6":
            print("\n==========Creando Proyecto===========")
            project_name = input("Ingrese el nombre del proyecto: ")
            # Si recibe False, significa que el proyecto ya existe
            if client.create_project(project_name) is False:
                print(
                    "El proyecto "
                    + project_name
                    + " ya existe, intente con otro nombre."
                )
            else:
                print("Proyecto: " + project_name + " creado con éxito")

        elif option == "7":
            print("\n==========Agregando Tarea a Proyecto===========")
            exist = False
            exist_in_project = False
            exist_project = False
            project_name = input("Ingrese el nombre del proyecto: ")
            task_name = input("Ingrese el nombre de la tarea a agregar al proyecto: ")
            # Verificar si la tarea existe
            for task in client.tasks:
                if task_name == task.get_name():
                    exist = True
                    # Verificar si el proyecto existe
                    for project in client.projects:
                        if project_name == project.get_name():
                            exist_project = True
                            # Para evitar que se agregue la misma tarea al proyecto
                            for task in project.tasks:
                                if task_name == task.get_name():
                                    exist_in_project = True
                                    print("La tarea ya existe en el proyecto.")
                                    break
                            # Si la tarea no existe en el proyecto, se agrega
                            if exist_in_project is False:
                                project.add_component(task)
                                print(
                                    f"La tarea {task_name} fue agregada al proyecto {project_name} con éxito."
                                )
                                break
            if exist_project is False:
                print("El proyecto no existe, cree uno y luego podrá agregar tareas.")
            if exist is False:
                print("La tarea que quiere agregar no existe.")

        elif option == "8":
            project_name = input("Ingrese el nombre del proyecto a eliminar: ")
            # Si retorna false no se puede eliminar porque no existe
            if client.delete_project(project_name) is False:
                print("El proyecto " + project_name + " no existe.")
            else:
                print("Proyecto " + project_name + " eliminado")

        elif option == "9":
            print("\n==========Mostrando Proyectos===========")
            client.view_projects()

        elif option == "10":
            print("\n==========Iniciando Pomodoro===========")
            # Se le envía notificación para que pueda enviar mensajes al usuario
            client.start_pomodoro(notification.Notification(user.get_username()))

        elif option == "11":
            print("\n==========Marcando Tarea como Realizada===========")
            task_name = input("Ingrese el nombre de la tarea a marcar como realizada: ")
            if client.set_task_as_done(task_name) is False:
                print("La tarea " + task_name + " no existe")
            else:
                print("Tarea " + task_name + " marcada como hecha")

        elif option == "12":
            print("\n==========Marcando Subtarea como Realizada===========")
            exist = False
            exist_task = False
            task_super = input(
                "Escriba el nombre de la tarea a la que pertenece la subtarea a marcar: "
            )
            # Verificar si la tarea a la que se quiere añadir la subtarea existe
            for task in client.tasks:
                if task_super == task.get_name():
                    exist_task = True
                    subtask = input("Ingrese el nombre de la subtarea a marcar: ")
                    # Verificar si la subtarea a marcar existe
                    for sub in task.subtasks:
                        if subtask == sub.get_name():
                            exist = True
                            sub.set_as_done()
                            print("Subtarea: " + subtask + " marcada con éxito")
                            break
                    if exist is False:
                        print(f"La subtarea {subtask} no existe.")
                        break
            if exist_task is False:
                print(f"La tarea {task_super} no existe, intente con otro nombre.")

        elif option == "13":
            print("\n==========Marcando Proyecto como Realizado===========")
            project_name = input(
                "Ingrese el nombre del proyecto a marcar como realizado: "
            )
            if client.set_project_as_done(project_name) is False:
                print("El proyecto " + project_name + " no existe")
            else:
                print("El proyecto " + project_name + " fue marcado como realizado")

        elif option == "14":
            print("\n==========Personalizando Pomodoro===========")
            client.custom_pomodoro()

        elif option == "15":
            print("\n==========Mostrando Planes de Suscripción===========")
            client.view_plans(subscription_instance)

        elif option == "16":
            if client.pay_for_subscription(subscription_instance) is True:
                print("\n============Pagando Suscripción=============")
                client = cliente.PremiumDecorator(client)
                client.premium = True
                print("Suscripción pagada con éxito")
            else:  # En caso de que el usuario ya sea premium
                print("\n============Mostrando Estado=============")
                print("Ya eres usuario premium")

        elif option == "17":
            print("\n==========Mostrando Reporte de Clientes===========")
            # client.view_clients_report()

        # Opciones que solo pueden ejecutar los usuarios premium
        elif option == "18":
            if client.premium is False:
                print("Opción no disponible")
            else:
                print("\n==========Mostrando Estadísticas de Productividad===========")
                print(client.view_productivity_stats())

        elif option == "19":
            if client.premium is False:
                print("Opción no disponible")
            else:
                print("\n==========Creando Carpeta===========")
                folder_name = input("Ingrese el nombre de la carpeta: ")
                client.create_folder(folder_name)

        elif option == "20":
            if client.premium is False:
                print("Opción no disponible")
            else:
                print("\n==========Asignando Proyecto a Carpeta===========")
                exist_project = False
                exist_folder = False
                project_name = input(
                    "Ingrese el nombre del proyecto a agregar a la carpeta: "
                )

                # Verificar si el proyecto existe
                for project in client.projects:
                    if project_name == project.get_name():
                        exist_project = True

                folder_name = input("Ingrese el nombre de la carpeta: ")
                # Verificar si la carpeta existe
                for folder in client.folders:
                    if folder_name == folder.get_name():
                        exist_folder = True

                # Para evitar que se agregue el mismo proyecto a la carpeta
                # pylint: disable=undefined-loop-variable
                # That isn't a undefined loop variable because with its if statement it's defined as just one
                if exist_project is True and exist_folder is True:
                    for folder in client.folders:
                        if folder_name == folder.get_name():
                            if folder.get_project(project_name) is None:
                                folder.add_project(project)
                                print(
                                    f"El proyecto {project_name} fue agregado a la carpeta {folder_name} con éxito."
                                )
                            else:
                                print("El proyecto ya existe en la carpeta.")
                                break

                if exist_project is False:
                    print(
                        f"\nEl proyecto {project_name} no existe, cree uno y luego podrá agregarlo a una carpeta."
                    )

                if exist_folder is False:
                    print(
                        f"\nLa carpeta {folder_name} no existe, cree una y luego podrá agregar proyectos."
                    )

        # Impresión con ciclos anidados
        elif option == "21":
            if client.premium is False:
                print("Opción no disponible")
            else:
                print("\n==========Mostrando Carpetas===========")
                for folder in client.folders:
                    print("Carpeta: " + folder.get_name())
                    for project in folder.projects:
                        print("     Proyecto: " + project.get_name())
                        for task in project.tasks:
                            print("         Tarea: " + task.get_name())
                            for subtask in task.subtasks:
                                print("             Subtarea: " + subtask.get_name())

        elif option == "x":
            print("Saliendo de la aplicación...")
            print(
                "Si desea enviar feedback, por favor envíe un correo a focustodo@udistrital.edu.co"
            )
            sys.exit()

        else:
            print("Opción inválida. Por favor seleccione una opción válida.")


if __name__ == "__main__":
    main()
