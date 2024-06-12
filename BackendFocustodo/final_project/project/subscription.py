"""
This module contains the Subscription class, which allows to add and remove clients, 
and get all the plans.
Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>

"""


# pylint: disable= too-few-public-methods
# This class just represent the plans that could be created, it's a guide to create a plan
class Plan:
    """This class represents the plans that could be created."""

    def __init__(self, id_plan: int, name: str, price: float, description: str):
        self.id_plan = id_plan
        self.name = name
        self.price = price
        self.description = description


class Subscription:
    """This class represents the Subscription class, which allows the Admin to add and
    remove clients, and get all the plans."""

    def __init__(self, username: str):
        self.username = username
        self.clients = []
        self.plans = []

    def add_client(self):
        """This method allows the Admin to add a client."""
        if self.username in self.clients:  # Verificar si el cliente ya está registrado
            return False
        self.clients.append(self.username)
        return True

    def get_clients(self):
        """This method shows all the clients."""
        for client in self.clients:
            print(f"Cliente: {client}")

    def remove_client(self):
        """This method allows the Admin to remove a client."""
        self.clients.remove(self.username)

    def set_plans(self):
        """This method allows to create a plan."""
        # Agregar planes default
        plan = Plan(1, "Plan básico", 10000, "1 mes")
        plan2 = Plan(2, "Plan anual", 30000, "12 meses")
        self.plans.append(plan)
        self.plans.append(plan2)

    def get_plans(self):
        """This method shows all the plans."""
        self.set_plans()
        for plan in self.plans:
            print(
                f"Plan: {plan.name} - Precio: {plan.price} - Descripción: {plan.description}"
            )
