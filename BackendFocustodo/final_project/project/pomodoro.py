"""
This module contains the Pomodoro class, which is used to create a Pomodoro timer.
Authors: Andres Acevedo <ajacevedoa@udistrital.edu.co> Javier Murcia <jmurcian@udistrital.edu.co>
"""

import time


class Pomodoro:
    """This class is used to create a Pomodoro timer."""

    def __init__(self, short_break, long_break, pomodoro_length, long_break_after):
        self._short_break = short_break * 60
        self._long_break = long_break * 60
        self._pomodoro_length = pomodoro_length * 60
        self._long_break_after = long_break_after
        self._seconds = self._pomodoro_length
        self._notification = None

    def start_pomodoro(self, notification):
        """This method starts the Pomodoro timer."""
        self._notification = notification
        pomodoro_count = 0
        while True:
            print(
                f"\nPomodoro timer started for {self._pomodoro_length // 60} minutes."
            )
            self.countdown(self._pomodoro_length)

            self._notification.show_notification("Time's up!")
            pomodoro_count += 1

            if pomodoro_count % self._long_break_after == 0:
                print(
                    f"\nIt's time for a long break of {self._long_break // 60} minutes."
                )
                choice = input("\nEnter 1 to take the break or 0 to skip: ")
                if choice == "1":
                    self.countdown(self._long_break)
                elif choice == "0":
                    print("Skipping the long break.")
                else:
                    print("Invalid choice. Skipping the long break.")
            else:
                print(
                    f"\nIt's time for a short break of {self._short_break // 60} minutes."
                )
                choice = input("\nEnter 1 to take the break or 0 to skip: ")
                if choice == "1":
                    self.countdown(self._short_break)
                elif choice == "0":
                    print("\nSkipping the short break.")
                else:
                    print("\nInvalid choice. Skipping the short break.")

            choice = input("\nEnter 1 to continue or 0 to stop: ")
            if choice == "0":
                self._notification.show_notification("\nTime's up!")
                break
            # pylint: disable= attribute-defined-outside-init
            if choice == "1":
                self.seconds = self._pomodoro_length
            else:
                print("\nInvalid choice. Exiting.")
                break

    # pylint: disable= consider-using-f-string
    def countdown(self, duration):
        """Countdown in minutes and seconds."""
        # pylint: disable= attribute-defined-outside-init
        self.seconds = duration
        while self.seconds > -1:
            mins, secs = divmod(self.seconds, 60)
            timeformat = "{:02d}:{:02d}".format(mins, secs)
            print(timeformat, end="\r")
            time.sleep(0.1)
            self.seconds -= 1
