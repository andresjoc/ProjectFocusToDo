"""
This module contains the Notification class, which is used to show notifications to an specific user.
Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>
"""


class Notification:
    """
    This class represent a notification that is showen in console
    """

    def __init__(self, message, username):
        self.message = message
        self.username = username

    def __str__(self):
        return self.message

    def show_notification(self):
        print(f"Notification to {self.username}: {self.message}")
