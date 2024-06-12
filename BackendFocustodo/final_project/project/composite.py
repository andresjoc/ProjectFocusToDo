"""
This module contains the classes that represent the composite pattern. With task, project and subtask

Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>

"""

from abc import ABC, abstractmethod
from datetime import datetime


class Component(ABC):
    """
    This class is used to create the components of the composite pattern.
    """

    def __init__(self, name):
        self.name = name
        self.status = False
        self.date = datetime.now().date()
        self.date_done = None

    @abstractmethod
    def add_component(self, componenteAgregado):
        pass

    @abstractmethod
    def remove_component(self, indice):
        pass

    @abstractmethod
    def set_as_done(self):
        pass

    @abstractmethod
    def get_component(self, name):
        pass

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status


class Project(Component):
    """
    This class represents a project, which is a composite component.
    """

    def __init__(self, name):
        super().__init__(name)
        self.tasks = []

    def add_component(self, componenteAgregado):
        self.tasks.append(componenteAgregado)

    def remove_component(self, indice):
        return self.tasks.pop(indice)

    def set_as_done(self):
        self.status = True
        for tarea in self.tasks:
            tarea.set_as_done()

    def get_component(self, name):
        tareaEncontrada = None
        for tarea in self.tasks:
            if name == tarea.get_name():
                tareaEncontrada = tarea
        return tareaEncontrada


class Task(Component):
    """
    This class represents a task, which is a composite component.
    """

    def __init__(self, name):
        super().__init__(name)
        self.subtasks = []
        self.tag = "General"

    def add_component(self, componenteAgregado):
        self.subtasks.append(componenteAgregado)

    def remove_component(self, subtask_name):
        for subtask in self.subtasks:
            if subtask_name == subtask.get_name():
                return self.subtasks.remove(subtask)
        return False

    def set_as_done(self):
        self.status = True
        self.date_done = datetime.now().date()
        for subtarea in self.subtasks:
            subtarea.set_as_done()

    def set_tag(self, tag):
        self.tag = tag

    def get_component(self, name):
        subtareaEncontrada = None
        for subtarea in self.subtasks:
            if name == subtarea.get_name():
                subtareaEncontrada = subtarea
        return subtareaEncontrada


class Subtask(Component):
    """
    This class represents a subtask, which is a leaf component.
    """

    def __init__(self, name):
        super().__init__(name)

    def add_component(self, componenteAgregado):
        pass

    def remove_component(self, indice):
        return None

    def set_as_done(self):
        self.status = True

    def get_component(self, name):
        return None


class Folder:
    """
    This class represents a folder, which is used to organize projects.
    """

    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, componenteAgregado):
        self.projects.append(componenteAgregado)

    def remove_project(self, indice):
        return self.projects.pop(indice)

    def get_name(self):
        return self.name

    def get_project(self, name):
        proyectoEncontrado = None
        for proyecto in self.projects:
            if name == proyecto.get_name():
                proyectoEncontrado = proyecto
        return proyectoEncontrado
