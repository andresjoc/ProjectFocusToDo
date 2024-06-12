"""
This module contains the classes that represent the composite pattern. 
With task, project and subtask

Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>

"""

from abc import ABC, abstractmethod
import datetime


class Component(ABC):
    """
    This class is used to create the components of the composite pattern.
    """

    def __init__(self, name):
        """
        Initializes a new instance of the Component class.

        Parameters:
        - name (str): The name of the component.
        """
        self.name = name
        self.status = False
        self.date = datetime.datetime.now().date()
        self.date_done = None

    @abstractmethod
    def add_component(self, componente_agregado):
        """
        Adds a component to the current component.

        Parameters:
        - componenteAgregado (Component): The component to be added.
        """

    @abstractmethod
    def remove_component(self, indice):
        """
        Removes a component from the current component.

        Parameters:
        - indice (int): The index of the component to be removed.
        """

    @abstractmethod
    def set_as_done(self):
        """
        Sets the current component as done.
        """

    @abstractmethod
    def get_component(self, name):
        """
        Gets a component with the specified name from the current component.

        Parameters:
        - name (str): The name of the component to retrieve.

        Returns:
        - Component: The component with the specified name, or None if not found.
        """

    def get_name(self):
        """
        Gets the name of the current component.

        Returns:
        - str: The name of the component.
        """
        return self.name

    def get_status(self):
        """
        Gets the status of the current component.

        Returns:
        - bool: The status of the component.
        """
        return self.status


class Project(Component):
    """
    This class represents a project, which is a composite component.
    """

    def __init__(self, name):
        super().__init__(name)
        self.tasks = []

    def add_component(self, componente_agregado):
        self.tasks.append(componente_agregado)

    def remove_component(self, indice):
        return self.tasks.pop(indice)

    def set_as_done(self):
        self.status = True
        for tarea in self.tasks:
            tarea.set_as_done()

    def get_component(self, name):
        tarea_encontrada = None
        for tarea in self.tasks:
            if name == tarea.get_name():
                tarea_encontrada = tarea
        return tarea_encontrada


class Task(Component):
    """
    This class represents a task, which is a composite component.

    Attributes:
        name (str): The name of the task.
        subtasks (list): A list of subtasks that belong to this task.
        tag (str): The tag associated with the task.

    Methods:
        add_component(componenteAgregado): Adds a subtask to the task.
        remove_component(subtask_name): Removes a subtask from the task.
        set_as_done(): Sets the task as done.
        set_tag(tag): Sets the tag for the task.
        get_component(name): Retrieves a subtask by its name.
    """

    def __init__(self, name):
        super().__init__(name)
        self.subtasks = []
        self.tag = "General"

    def add_component(self, componente_agregado):
        """
        Adds a subtask to the task.

        Args:
            componenteAgregado (Component): The subtask to be added.

        Returns:
            None
        """
        self.subtasks.append(componente_agregado)

    def remove_component(self, indice):
        """
        Removes a subtask from the task.

        Args:
            indice (str): The name of the subtask to be removed.

        Returns:
            bool: True if the subtask was successfully removed, False otherwise.
        """
        for subtask in self.subtasks:
            if indice == subtask.get_name():
                return self.subtasks.remove(subtask)
        return False

    def set_as_done(self):
        """
        Sets the task as done.

        This method sets the status of the task to True and updates the date_done attribute.
        It also sets all the subtasks of the task as done.

        Returns:
            None
        """
        self.status = True
        self.date_done = datetime.datetime.now().date()
        for subtarea in self.subtasks:
            subtarea.set_as_done()

    def set_tag(self, tag):
        """
        Sets the tag for the task.

        Args:
            tag (str): The tag to be set for the task.

        Returns:
            None
        """
        self.tag = tag

    def get_component(self, name):
        """
        Retrieves a subtask by its name.

        Args:
            name (str): The name of the subtask to be retrieved.

        Returns:
            Component: The subtask with the specified name, or None if not found.
        """
        subtarea_encontrada = None
        for subtarea in self.subtasks:
            if name == subtarea.get_name():
                subtarea_encontrada = subtarea
        return subtarea_encontrada


class Subtask(Component):
    """
    This class represents a subtask, which is a leaf component.

    Attributes:
        name (str): The name of the subtask.
        status (bool): The status of the subtask (True if done, False otherwise).

    Methods:
        __init__(self, name): Initializes a new instance of the Subtask class.
        add_component(self, componenteAgregado): Adds a component to the subtask.
        remove_component(self, indice): Removes a component from the subtask.
        set_as_done(self): Sets the subtask as done.
        get_component(self, name): Retrieves a component from the subtask.
    """

    # pylint: disable=useless-super-delegation
    # It is necessary to call the constructor of the parent class
    def __init__(self, name):
        """
        Initializes a new instance of the Subtask class.

        Args:
            name (str): The name of the subtask.
        """
        super().__init__(name)

    def add_component(self, componente_agregado):
        """
        Adds a component to the subtask (not applicable for leaf components).

        Args:
            componente_agregado: The component to be added.
        """

    def remove_component(self, indice):
        """
        Removes a component from the subtask (not applicable for leaf components).

        Args:
            indice: The index of the component to be removed.

        Returns:
            None
        """
        return None

    def set_as_done(self):
        """
        Sets the subtask as done.
        """
        self.status = True

    def get_component(self, name):
        """
        Retrieves a component from the subtask (not applicable for leaf components).

        Args:
            name: The name of the component to be retrieved.

        Returns:
            None
        """
        return None


class Folder:
    """
    This class represents a folder, which is used to organize projects.

    Attributes:
        name (str): The name of the folder.
        projects (list): A list of projects that belong to this folder.

    Methods:
        add_project(componenteAgregado): Adds a project to the folder.
        remove_project(indice): Removes a project from the folder.
        get_name(): Gets the name of the folder.
        get_project(name): Gets a project from the folder by its name.
    """

    def __init__(self, name):
        """
        Initializes a new instance of the Folder class.

        Parameters:
        - name (str): The name of the folder.
        """
        self.name = name
        self.projects = []

    def add_project(self, componente_agregado):
        """
        Adds a project to the folder.

        Parameters:
        - componenteAgregado (Project): The project to be added.
        """
        self.projects.append(componente_agregado)

    def remove_project(self, indice):
        """
        Removes a project from the folder.

        Parameters:
        - indice (int): The index of the project to be removed.

        Returns:
        - Project: The removed project.
        """
        return self.projects.pop(indice)

    def get_name(self):
        """
        Gets the name of the folder.

        Returns:
        - str: The name of the folder.
        """
        return self.name

    def get_project(self, name):
        """
        Gets a project from the folder by its name.

        Parameters:
        - name (str): The name of the project to be retrieved.

        Returns:
        - Project: The project with the specified name, or None if not found.
        """
        proyecto_encontrado = None
        for proyecto in self.projects:
            if name == proyecto.get_name():
                proyecto_encontrado = proyecto
        return proyecto_encontrado
