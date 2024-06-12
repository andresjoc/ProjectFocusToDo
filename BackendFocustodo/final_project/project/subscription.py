"""
This module contains the Subscription class, which allows the Admin to add and remove clients, and get all the plans.
Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>

"""


class Plan:
    """This class represents the plans that the Admin can create."""

    def __init__(self, id_plan: int, name: str, price: float, description: str):
        self.id_plan = id_plan
        self.name = name
        self.price = price
        self.description = description


class Subscription:
    """This class represents the Subscription class, which allows the Admin to add and remove clients, and get all the plans."""

    def __init__(self, username: str):
        self.username = username
        self.clients = []
        self.plans = []

    def add_client(self):
        """This method allows the Admin to add a client."""
        self.clients.append(self.username)

    def remove_client(self):
        """This method allows the Admin to remove a client."""
        self.clients.remove(self.username)

    def get_plans(self):
        """This method shows all the plans."""
        # Agregar planes default
        plan = Plan(1, "Plan básico", 10000, "1 mes")
        plan2 = Plan(2, "Plan anual", 30000, "12 meses")

        print(
            f"Plan: {plan.name} - Precio: {plan.price} - Descripción: {plan.description}"
        )
        print(
            f"Plan: {plan2.name} - Precio: {plan2.price} - Descripción: {plan2.description}"
        )
