"""
This module contains the Notification class, which is used to show 
notifications to an specific user.
Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>
"""


# pylint: disable= too-few-public-methods
class Notification:
    """
    This class represents a notification that is shown in the console.

    Attributes:
        username (str): The username associated with the notification.

    Methods:
        show_notification(message: str): Displays the notification message in the console.
    """

    def __init__(self, username):
        """
        Initializes a new instance of the Notification class.

        Args:
            username (str): The username associated with the notification.
        """
        self.username = username

    def show_notification(self, message: str):
        """
        Displays the notification message in the console.

        Args:
            message (str): The message to be displayed in the notification.
        """
        print(f"\nNotification to {self.username}: {message}")
