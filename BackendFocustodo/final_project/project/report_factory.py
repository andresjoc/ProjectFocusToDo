import datetime

"""
This module contains the Report class and its subclasses. This class is used to represent the report information.
Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>

"""


class Report:
    """This class represents the report information."""

    def __init__(self, type: str):
        self.__title = " "
        self.__description = " "
        self.__date = " "
        self.__type = type
        self.__content = " "

    def create_report(self):
        """This method is an abstract definition of a possible general behavior for all reports"""


class TasksReport(Report):
    """This class represents a report of the tasks completed by the user"""

    def __init__(self, report_type: str, done_tasks: list):
        super().__init__(report_type)
        self.__total_completed_tasks = len(done_tasks)
        self.__weekly_completed_tasks = 0
        self.__today_completed_tasks = 0

        # Counting the number of tasks completed today
        for task in done_tasks:
            if task.date_done == datetime.datetime.now():
                self.__today_completed_tasks += 1

        # Counting the number of tasks completed in the last week
        for task in done_tasks:
            if task.date_done >= datetime.datetime.now() - datetime.timedelta(days=7):
                self.__weekly_completed_tasks += 1

    def create_report(self):
        """This method creates the report of the tasks completed by the user"""
        self.__title = f"{self.__type} Report"
        self.__description = (
            "This report shows the tasks that you completed and how was your ."
        )
        self.__date = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )  # Para mostrar la fecha actual
        self.__content = f"""
        Total completed tasks: {self.__total_completed_tasks}\n
        Weekly completed tasks: {self.__weekly_completed_tasks}\n
        Today completed tasks: {self.__today_completed_tasks}\n
        """
        return f"{self.__title}\n{self.__description}\n{self.__date}\n{self.__content}"


class ClientsReport(Report):
    def __init__(self, report_type: str, number_clients: list):
        super().__init__(report_type)
        self.__number_of_clients = number_clients
        self.__number_of_premium_clients = 0

        # Counting the number of premium clients
        for client in self.__number_of_clients:
            if client.premium is True:
                self.__number_of_premium_clients += 1

    def create_report(self):
        """This method creates the report of the clients registered in the system"""
        self.__title = f"{self.__type} Report"
        self.__description = (
            "This report shows the number of clients and how many of them are premium."
        )
        self.__date = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )  # Para mostrar la fecha actual
        self.__content = f"""
        Number of clients: {len(self.__number_of_clients)}\n
        Number of premium clients: {self.__number_of_premium_clients}\n
        """
        return f"{self.__title}\n{self.__description}\n{self.__date}\n{self.__content}"


class ReportFactory:
    """This class represents the factory that creates the reports."""

    def create_report(self, report_type: str, list: list) -> Report:
        if report_type == "Tasks":
            return TasksReport(report_type, list)
        elif report_type == "Clients":
            return ClientsReport(report_type, list)
        return None
