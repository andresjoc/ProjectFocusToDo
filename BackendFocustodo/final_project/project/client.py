"""
This module contains the classes Client and PremiumDecorator.

Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>
"""

# pylint: disable = line-too-long
# pylint: disable= import-error
from abc import ABC, abstractmethod
from project import composite
from project import pomodoro
from project import report_factory
from project import notification


# Abstract class for the decorator pattern
class ClientABC(ABC):
    """
    This class is an abstract class that defines the methods that the client should have.
    """

    @abstractmethod
    def create_task(self, name: str):
        """This method creates a task."""

    @abstractmethod
    def view_tasks(self):
        """This method shows all the tasks."""

    @abstractmethod
    def delete_task(self, name: str):
        """This method deletes a task."""

    @abstractmethod
    def create_subtask(self, name: str):
        """This method creates a subtask."""

    @abstractmethod
    def create_project(self, name: str):
        """This method creates a project."""

    @abstractmethod
    def delete_project(self, name: str):
        """This method deletes a project."""

    @abstractmethod
    def view_projects(self):
        """This method shows all the projects."""

    # pylint: disable = redefined-outer-name
    @abstractmethod
    def start_pomodoro(self, notification):
        """This method starts the pomodoro timer."""

    @abstractmethod
    def set_task_as_done(self, name: str):
        """This method sets a task as done."""

    @abstractmethod
    def set_subtask_as_done(self, name: str):
        """This method sets a subtask as done."""

    @abstractmethod
    def set_project_as_done(self, name: str):
        """This method sets a project as done."""

    @abstractmethod
    def custom_pomodoro(self):
        """This method allows the user to set custom values for the pomodoro timer."""

    @abstractmethod
    def view_plans(self, subscription):
        """This method shows all the plans."""

    @abstractmethod
    def pay_for_subscription(self, subscription):
        """This method allows the user to pay for a subscription."""

    @abstractmethod
    def view_clients_report(self, type_report: str):
        """This method shows the clients report."""


# pylint: disable=too-many-instance-attributes
# That are necessary for the class
class Client(ClientABC):
    """This class represents the client of the application. It has all the methods to manage the tasks,
    subtasks, projects, pomodoro timer, etc."""

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

    # pylint: disable=too-many-nested-blocks
    # That nested blocks are necessary because of the structure of the tasks, subtasks and projects
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

    # pylint: disable = redefined-outer-name
    def start_pomodoro(self, notification):
        """This method starts the pomodoro timer."""
        pomodoro_timer = pomodoro.Pomodoro(
            self.short_break,
            self.long_break,
            self.pomodoro_length,
            self.long_break_after,
        )
        pomodoro_timer.start_pomodoro(notification)

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

    def view_plans(self, subscription):
        """This method shows all the plans."""
        subscription.get_plans()

    def pay_for_subscription(self, subscription):
        """This method allows the user to pay for a subscription."""
        if subscription.add_client() is False:
            return False  # En caso de que el usuario ya sea premium
        return True  # En caso de que el usuario no sea premium

    def view_clients_report(self, type_report: str):
        """This method shows the clients report."""
        factory = report_factory.ReportFactory()
        print(factory.create_report("Clients", self.clients))

    def send_notification(self, message: str):
        """This method sends a notification."""
        noti = notification.Notification(message, self.user)
        noti.show_notification()


class PremiumDecorator(ClientABC):
    """This class adds the premium functionality to the client. Using the decorator pattern."""

    def __init__(self, client):
        self.client = client
        self.premium = client.premium
        self.tasks = client.tasks
        self.done_tasks = client.done_tasks
        self.folders = []
        self.projects = client.projects

    def create_task(self, name: str):
        """This method creates a task."""
        return self.client.create_task(name)

    def view_tasks(self):
        """This method shows all the tasks."""
        return self.client.view_tasks()

    def delete_task(self, name: str):
        """This method deletes a task."""
        return self.client.delete_task(name)

    def create_subtask(self, name: str):
        """This method creates a subtask."""
        return self.client.create_subtask(name)

    def view_subtasks(self):
        """This method shows all the subtasks."""
        return self.client.view_subtasks()

    def delete_subtask(self, name: str):
        """This method deletes a subtask."""
        return self.client.delete_subtask(name)

    def create_project(self, name: str):
        """This method creates a project."""
        return self.client.create_project(name)

    def delete_project(self, name: str):
        """This method deletes a project."""
        return self.client.delete_project(name)

    def view_projects(self):
        """This method shows all the projects."""
        return self.client.view_projects()

    # pylint: disable = redefined-outer-name
    def start_pomodoro(self, notification):
        """This method starts the pomodoro timer."""
        return self.client.start_pomodoro(notification)

    def set_task_as_done(self, name: str):
        """This method sets a task as done."""
        return self.client.set_task_as_done(name)

    def set_subtask_as_done(self, name: str):
        """This method sets a subtask as done."""
        return self.client.set_subtask_as_done(name)

    def set_project_as_done(self, name: str):
        """This method sets a project as done."""
        return self.client.set_project_as_done(name)

    def custom_pomodoro(self):
        """This method allows the user to set custom values for the pomodoro timer."""
        return self.client.custom_pomodoro()

    def view_plans(self, subscription):
        """This method shows all the plans."""
        return self.client.view_plans(subscription)

    def pay_for_subscription(self, subscription):
        """This method allows the user to pay for a subscription."""
        self.client.pay_for_subscription(subscription)

    def view_clients_report(self, type_report: str):
        """This method shows the clients report."""
        self.client.create_report(type_report)

    def view_productivity_stats(self):
        """This method shows the productivity stats."""
        factory = report_factory.ReportFactory()
        return factory.create_report("Tasks", self.done_tasks)

    def create_folder(self, folder_name: str):
        """This method creates a folder."""
        folder = composite.Folder(folder_name)
        self.folders.append(folder)

    def set_tag(self, task_name: str, tag: str):
        """This method sets a tag to a task."""
        for task in self.client.tasks:
            if task_name == task.get_name():
                task.set_tag(tag)
                break
