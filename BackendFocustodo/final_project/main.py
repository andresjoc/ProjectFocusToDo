"""
This module has some classes related to users and authentication.
Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>
"""

from project import user_auth
from project import composite
from project import pomodoro
from project import subscription
from project import report_factory
from abc import ABC, abstractmethod


def login():
    """This function allows the user to log in the system."""
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    auth = user_auth.Authentication(username, password)

    if auth.authenticate():
        return auth.userdata()
    return None


# Abstract class for the decorator pattern
class ClientABC(ABC):

    def create_task(self, name: str):
        """This method creates a task."""
        pass

    def view_tasks(self):
        """This method shows all the tasks."""
        pass

    def delete_task(self, name: str):
        """This method deletes a task."""
        pass

    def create_subtask(self, name: str):
        """This method creates a subtask."""
        pass

    def delete_subtask(self, name: str):
        """This method deletes a subtask."""
        pass

    def view_subtasks(self):
        """This method shows all the subtasks."""
        pass

    def create_project(self, name: str):
        """This method creates a project."""
        pass

    def delete_project(self, name: str):
        """This method deletes a project."""
        pass

    def view_projects(self):
        """This method shows all the projects."""
        pass

    def start_pomodoro(self):
        """This method starts the pomodoro timer."""
        pass

    def set_task_as_done(self, name: str):
        """This method sets a task as done."""
        pass

    def set_subtask_as_done(self, name: str):
        """This method sets a subtask as done."""
        pass

    def set_project_as_done(self, name: str):
        """This method sets a project as done."""
        pass

    def custom_pomodoro(self):
        """This method allows the user to set custom values for the pomodoro timer."""
        pass

    def view_plans(self):
        """This method shows all the plans."""
        pass

    def pay_for_suscription(self):
        """This method allows the user to pay for a subscription."""
        pass

    def create_report(self, type_report: str):
        """This method shows the clients report."""
        pass


class Client(ClientABC):
    """This class represents the client of the application. It has all the methods to manage the tasks, subtasks, projects, pomodoro timer, etc."""

    def __init__(self):
        self.tasks = []
        self.projects = []
        self.short_break = 5
        self.long_break = 15
        self.pomodoro_length = 25
        self.long_break_after = 4
        self.plans = []
        self.premium = False
        self.user = None
        self.done_tasks = []
        self.clients = []

    def create_task(self, name: str):
        """This method creates a task."""
        for tarea in self.tasks:
            if name == tarea.get_name():
                return False
        tarea = composite.Task(name)
        self.tasks.append(tarea)
        return True

    def view_tasks(self):
        """This method shows all the tasks."""
        for tarea in self.tasks:
            if tarea.status is False:
                print("Tarea: " + tarea.get_name())
                for subtarea in tarea.subtasks:
                    if subtarea.status is False:
                        print("     Subtarea: " + subtarea.get_name() + "\n")

    def delete_task(self, name: str):
        """This method deletes a task."""
        for tarea in self.tasks:
            if name == tarea.get_name():
                self.tasks.remove(tarea)
                return True
        return False

    def create_subtask(self, name: str):
        """This method creates a subtask."""
        subtarea = composite.Subtask(name)
        return subtarea

    def create_project(self, name: str):
        """This method creates a project."""
        for project in self.projects:
            if name == project.get_name():
                return False
        project = composite.Project(name)
        self.projects.append(project)
        return True

    def delete_project(self, name: str):
        """This method deletes a project."""
        for project in self.projects:
            if name == project.get_name():
                self.projects.remove(project)
                return True
        return False

    def view_projects(self):
        """This method shows all the projects."""
        for project in self.projects:
            if project.status is False:
                print("Proyecto: " + project.get_name())
                if len(project.tasks) > 0:
                    for tarea in project.tasks:
                        if tarea.status is False:
                            print("     Tarea: " + tarea.get_name())
                            for subtarea in tarea.subtasks:
                                if subtarea.status is False:
                                    print(
                                        "         Subtarea: "
                                        + subtarea.get_name()
                                        + "\n"
                                    )

    def start_pomodoro(self):
        """This method starts the pomodoro timer."""
        pomodoro_timer = pomodoro.Pomodoro(
            self.short_break,
            self.long_break,
            self.pomodoro_length,
            self.long_break_after,
        )
        pomodoro_timer.start_pomodoro()

    def set_task_as_done(self, name: str):
        """This method sets a task as done."""
        for task in self.tasks:
            if name == task.get_name():
                self.done_tasks.append(task)
                task.set_as_done()
                return True
        return False

    def set_subtask_as_done(self, name: str):
        """This method sets a subtask as done."""
        for subtask in self.tasks:
            if name == subtask.get_name():
                subtask.set_as_done()
                break

    def set_project_as_done(self, name: str):
        """This method sets a project as done."""
        for project in self.projects:
            if name == project.get_name():
                project.set_as_done()
                return True
        return False

    def custom_pomodoro(self):
        """This method allows the user to set custom values for the pomodoro timer."""
        self.short_break = int(
            input("Ingrese la duración de la pausa corta en minutos: ")
        )
        self.long_break = int(
            input("Ingrese la duración de la pausa larga en minutos: ")
        )
        self.pomodoro_length = int(
            input("Ingrese la duración del pomodoro en minutos: ")
        )
        self.long_break_after = int(
            input("Ingrese el número de pomodoros antes de una pausa larga: ")
        )

    def view_plans(self, username: str):
        """This method shows all the plans."""
        subscription.Subscription.get_plans(username)

    def pay_for_suscription(self, username):
        """This method allows the user to pay for a subscription."""
        subscription.Subscription.add_client(username)

    def view_clients_report(self):
        """This method shows the clients report."""
        factory = report_factory.ReportFactory()
        factory.create_report("Clients", self.clients)


class PremiumDecorator(ClientABC):
    """This class adds the premium functionality to the client. Using the decorator pattern."""

    # Envuelve un objeto Client y delega todas las llamadas de métodos al objeto envuelto.
    def __init__(self, client):
        self.client = client
        self.client.premium = True

    def create_task(self, name: str):
        """This method creates a task."""
        self.client.create_task(name)

    def view_tasks(self):
        """This method shows all the tasks."""
        self.client.view_tasks()

    def delete_task(self, name: str):
        """This method deletes a task."""
        self.client.delete_task(name)

    def create_subtask(self, name: str):
        """This method creates a subtask."""
        self.client.create_subtask(name)

    def view_subtasks(self):
        """This method shows all the subtasks."""
        self.client.view_subtasks()

    def create_project(self, name: str):
        """This method creates a project."""
        self.client.create_project(name)

    def delete_project(self, name: str):
        """This method deletes a project."""
        self.client.delete_project(name)

    def view_projects(self):
        """This method shows all the projects."""
        self.client.view_projects()

    def start_pomodoro(self):
        """This method starts the pomodoro timer."""
        self.client.start_pomodoro()

    def set_task_as_done(self, name: str):
        """This method sets a task as done."""
        self.client.set_task_as_done(name)

    def set_subtask_as_done(self, name: str):
        """This method sets a subtask as done."""
        self.client.set_subtask_as_done(name)

    def set_project_as_done(self, name: str):
        """This method sets a project as done."""
        self.client.set_project_as_done(name)

    def custom_pomodoro(self):
        """This method allows the user to set custom values for the pomodoro timer."""
        self.client.custom_pomodoro()

    def view_plans(self):
        """This method shows all the plans."""
        self.client.view_plans()

    def pay_for_suscription(self):
        """This method allows the user to pay for a subscription."""
        self.client.pay_for_suscription()

    def create_report_clients(self):
        """This method shows the clients report."""
        self.client.create_report_clients()

    def view_productivity_stats(self):
        """This method shows the productivity stats."""
        factory = report_factory.ReportFactory()
        factory.create_report("Tasks", self.client.done_tasks)

    def create_folder(self, name: str):
        """This method creates a folder."""
        self.client.create_folder(name)

    def set_tag(self, name: str, tag: str):
        """This method sets a tag to a task."""
        for task in self.client.tasks:
            if name == task.get_name():
                task.set_tag(tag)
                break


def main():
    """This is the main function of the application. It allows the user to interact with the system."""
    user = None
    print("Bienvenido a la aplicación FocusToDo\n")
    print("Le informamos que para utilizar la aplicación debe iniciar sesión\n")

    user = login()
    while user is None:
        print("Usuario o contraseña incorrectos, intente de nuevo.")
        user = login()

    client = Client()

    OPTIONS = """
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
    """

    print(OPTIONS)

    # Menú de opciones
    while True:
        option = input(
            "\nPor favor seleccione una opción: (Escriba 0 si desea ver las opciones nuevamente): "
        )

        if option == "1":
            print("\n==========Creando Tarea===========")
            task_name = input("Ingrese el nombre de la tarea: ")
            if client.create_task(task_name) is False:
                print("La tarea " + task_name + " ya existe, intente con otro nombre.")
            else:
                print("Tarea: " + task_name + " creada con éxito")
        elif option == "0":
            print(OPTIONS)
        elif option == "2":
            print("\n==========Mostrando Tareas===========")
            client.view_tasks()
        elif option == "3":
            print("\n==========Eliminando Tarea===========")
            task_name = input("Ingrese el nombre de la tarea a eliminar: ")
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
            for task in client.tasks:
                if task_super == task.get_name():
                    exist_task = True
                    subtask = input("Ingrese el nombre de la subtarea: ")
                    for sub in task.subtasks:
                        if subtask == sub.get_name():
                            exist = True
                    if exist is False:
                        task.add_component(client.create_subtask(subtask))
                        print("Subtarea: " + subtask + " creada con éxito")
                        break
                    else:
                        print(
                            f"La subtarea {subtask} ya existe, intente con otro nombre."
                        )
                        break

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
            for task in client.tasks:
                if task_super == task.get_name():
                    exist_task = True
                    subtask = input("Ingrese el nombre de la subtarea a eliminar: ")
                    for sub in task.subtasks:
                        if subtask == sub.get_name():
                            exist = True
                            task.remove_component(subtask)
                            print("Subtarea: " + subtask + " eliminada con éxito")
                            break
                    if exist is False:
                        print(f"La subtarea {subtask} no existe.")
                        break
            if exist_task is False:
                print(f"La tarea {task_super} no existe, intente con otro nombre.")

        elif option == "6":
            print("\n==========Creando Proyecto===========")
            project_name = input("Ingrese el nombre del proyecto: ")
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
            for task in client.tasks:
                if task_name == task.get_name():
                    exist = True
                    for project in client.projects:
                        if project_name == project.get_name():
                            exist_project = True
                            # Para evitar que se agregue la misma tarea al proyecto
                            for project in project.tasks:
                                if task_name == project.get_name():
                                    exist_in_project = True
                                    print("La tarea ya existe en el proyecto.")
                                    break
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
            if client.delete_project(project_name) is False:
                print("El proyecto " + project_name + " no existe.")
            else:
                print("Proyecto " + project_name + " eliminado")
        elif option == "9":
            print("\n==========Mostrando Proyectos===========")
            client.view_projects()
        elif option == "10":
            print("\n==========Iniciando Pomodoro===========")
            client.start_pomodoro()
        elif option == "11":
            print("\n==========Marcando Tarea como Realizada===========")
            task_name = input("Ingrese el nombre de la tarea a marcar como realizada: ")
            if client.set_task_as_done(task_name) is False:
                print("La tarea " + task_name + " no existe")
            else:
                print("Tarea " + task_name + "marcada como hecha")
        elif option == "12":
            print("\n==========Marcando Subtarea como Realizada===========")
            exist = False
            exist_task = False
            task_super = input(
                "Escriba el nombre de la tarea a la que pertenece la subtarea a marcar: "
            )
            for task in client.tasks:
                if task_super == task.get_name():
                    exist_task = True
                    subtask = input("Ingrese el nombre de la subtarea a marcar: ")
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
            client.view_plans(user.get_username)
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")


main()
