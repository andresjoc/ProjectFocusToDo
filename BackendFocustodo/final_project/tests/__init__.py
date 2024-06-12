import sys
import unittest
from datetime import datetime, timedelta

from project.user_auth import Authentication, User
from project.subscription import Subscription
from project.report_factory import ClientsReport, ReportFactory, TasksReport
from project.pomodoro import Pomodoro
from project.composite import Component, Folder, Project, Subtask, Task
from project.notification import Notification
from io import StringIO
from unittest.mock import mock_open, patch, Mock


class TestComponentes(unittest.TestCase):
    def setUp(self):
        self.subtask1 = Subtask("Subtask 1")
        self.subtask2 = Subtask("Subtask 2")
        self.task1 = Task("Task 1")
        self.task2 = Task("Task 2")
        self.project1 = Project("Project 1")
        self.folder1 = Folder("folder 1")

    def test_subtask(self):
        self.assertFalse(self.subtask1.get_status())
        self.subtask1.set_as_done()
        self.assertTrue(self.subtask1.get_status())

    def test_task(self):
        self.task1.add_component(self.subtask1)
        self.task1.add_component(self.subtask2)
        self.assertEqual(len(self.task1.subtasks), 2)
        self.task1.set_as_done()
        self.assertTrue(self.task1.get_status())
        self.assertTrue(self.subtask1.get_status())
        self.assertTrue(self.subtask2.get_status())

    def test_project(self):
        self.project1.add_component(self.task1)
        self.project1.add_component(self.task2)
        self.assertEqual(len(self.project1.tasks), 2)
        self.project1.set_as_done()
        self.assertTrue(self.project1.get_status())
        self.assertTrue(self.task1.get_status())
        self.assertTrue(self.task2.get_status())

    def test_folder(self):
        self.folder1.add_project(self.project1)
        self.assertEqual(len(self.folder1.projects), 1)
        proyecto_encontrado = self.folder1.get_project("Project 1")
        self.assertEqual(proyecto_encontrado.get_name(), "Project 1")

    def test_dates(self):
        fecha_actual = datetime.datetime.now().date()
        self.subtask1.set_as_done()
        self.assertEqual(self.subtask1.date, fecha_actual)

        fecha_anterior = fecha_actual - timedelta(days=1)
        self.task1.date = fecha_anterior
        self.task1.set_as_done()
        self.assertEqual(self.task1.date_done, fecha_actual)


class TestNotification(unittest.TestCase):
    def setUp(self):
        self.notification = Notification("usuario_test")

    def test_notification_message(self):
        test_message = "This is a test message"
        captured_output = StringIO()
        sys.stdout = captured_output
        self.notification.show_notification(test_message)
        sys.stdout = sys.__stdout__
        expected_output = f"\nNotification to usuario_test: {test_message}\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


class TestPomodoro(unittest.TestCase):
    def setUp(self):
        self.short_break = 1
        self.long_break = 1
        self.pomodoro_length = 1
        self.long_break_after = 1
        self.notification = Mock()
        self.pomodoro = Pomodoro(
            self.short_break,
            self.long_break,
            self.pomodoro_length,
            self.long_break_after,
        )

    @patch("builtins.input", side_effect=["1", "0"])
    @patch("builtins.print")
    def test_start_pomodoro(self, mock_print, mock_input):
        self.pomodoro.start_pomodoro(self.notification)
        self.notification.show_notification.assert_called_with("\nTime's up!")

    @patch("time.sleep")
    def test_countdown(self, mock_sleep):
        duration = 60
        self.pomodoro.countdown(duration)
        mock_sleep.assert_called_with(0.1)


import datetime
from unittest.mock import Mock


class TestReport(unittest.TestCase):
    def setUp(self):
        self.report_type = "Tasks"
        now = datetime.datetime.now()
        three_days_ago = now - datetime.timedelta(days=3)
        ten_days_ago = now - datetime.timedelta(days=10)

        self.done_tasks = [
            Mock(date_done=now),
            Mock(date_done=three_days_ago),
            Mock(date_done=ten_days_ago),
        ]

    def test_tasks_report(self):
        tasks_report = TasksReport(self.report_type, self.done_tasks)
        report_content = tasks_report.create_report()
        self.assertIn("Tasks Report", report_content)
        self.assertIn(f"Today completed tasks: 1", report_content)
        self.assertIn(f"Weekly completed tasks: 2", report_content)
        self.assertIn(f"Total completed tasks: 3", report_content)

    def test_clients_report(self):
        clients = [Mock(premium=True), Mock(premium=False), Mock(premium=True)]
        clients_report = ClientsReport("Clients", clients)
        report_content = clients_report.create_report()
        self.assertIn("Clients Report", report_content)
        self.assertIn("Number of clients: 3", report_content)
        self.assertIn("Number of premium clients: 2", report_content)

    def test_report_factory(self):
        factory = ReportFactory()
        tasks_report = factory.create_report("Tasks", self.done_tasks)
        self.assertIsInstance(tasks_report, TasksReport)
        clients_report = factory.create_report("Clients", [])
        self.assertIsInstance(clients_report, ClientsReport)
        invalid_report = factory.create_report("Invalid", [])
        self.assertIsNone(invalid_report)


class TestSubscription(unittest.TestCase):
    def setUp(self):
        self.username = "testuser"
        self.subscription = Subscription(self.username)

    def test_add_client(self):
        self.assertTrue(self.subscription.add_client())
        self.assertIn(self.username, self.subscription.clients)
        self.assertFalse(
            self.subscription.add_client()
        )  # Intentar agregar el mismo cliente

    def test_remove_client(self):
        self.subscription.add_client()
        self.subscription.remove_client()
        self.assertNotIn(self.username, self.subscription.clients)

    def test_get_clients(self):
        self.subscription.add_client()
        with patch("builtins.print") as mock_print:
            self.subscription.get_clients()
            mock_print.assert_called_with(f"Cliente: {self.username}")

    def test_set_plans(self):
        self.subscription.set_plans()
        self.assertEqual(len(self.subscription.plans), 2)
        self.assertEqual(self.subscription.plans[0].id_plan, 1)
        self.assertEqual(self.subscription.plans[0].name, "basic plan")
        self.assertEqual(self.subscription.plans[0].price, 10000)
        self.assertEqual(self.subscription.plans[0].description, "one month")

    def test_get_plans(self):
        with patch("builtins.print") as mock_print:
            self.subscription.get_plans()
            expected_output = [
                f"Plan: basic plan - Precio: 10000 - Descripción: one month",
                f"Plan: year plan - Precio: 30000 - Descripción: twelve months",
            ]
            mock_print.assert_has_calls(
                [unittest.mock.call(output) for output in expected_output]
            )


class TestUser(unittest.TestCase):
    def setUp(self):
        self.username = "testuser"
        self.grants = {"admin": True, "user": True, "unknown": False}
        self.user = User(self.username, self.grants)

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), self.username)

    def test_is_grant(self):
        self.assertTrue(self.user.is_grant("admin"))
        self.assertTrue(self.user.is_grant("user"))
        self.assertFalse(self.user.is_grant("unknown"))


class TestAuthentication(unittest.TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.authentication = Authentication(self.username, self.password)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"username": "testuser", "password": "testpassword", "grants": {"admin": true, "user": true}}]',
    )
    def test_authenticate(self, mock_file):
        self.assertTrue(self.authentication.authenticate())
        self.assertEqual(self.authentication.userdata().get_username(), self.username)
        self.assertTrue(self.authentication.userdata().is_grant("admin"))
        self.assertTrue(self.authentication.userdata().is_grant("user"))

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"username": "otheruser", "password": "otherpassword", "grants": {"user": true}}]',
    )
    def test_authenticate_failure(self, mock_file):
        self.assertFalse(self.authentication.authenticate())


if __name__ == "__main__":
    unittest.main()
