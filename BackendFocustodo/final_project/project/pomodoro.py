import time

"""
This module contains the Pomodoro class, which is used to create a Pomodoro timer.
"""


class Pomodoro:
    """This class is used to create a Pomodoro timer."""

    def __init__(self, short_break, long_break, pomodoro_length, long_break_after):
        self.short_break = short_break * 60
        self.long_break = long_break * 60
        self.pomodoro_length = pomodoro_length * 60
        self.long_break_after = long_break_after
        self.seconds = self.pomodoro_length

    def start_pomodoro(self):
        """This method starts the Pomodoro timer."""
        pomodoro_count = 0
        while True:
            print(f"Pomodoro timer started for {self.pomodoro_length // 60} minutes.")
            self.countdown(self.pomodoro_length)

            print("Time's up!")
            pomodoro_count += 1

            if pomodoro_count % self.long_break_after == 0:
                print(f"It's time for a long break of {self.long_break // 60} minutes.")
                choice = input("Enter 1 to take the break or 0 to skip: ")
                if choice == "1":
                    self.countdown(self.long_break)
                elif choice == "0":
                    print("Skipping the long break.")
                else:
                    print("Invalid choice. Skipping the long break.")
            else:
                print(
                    f"It's time for a short break of {self.short_break // 60} minutes."
                )
                choice = input("Enter 1 to take the break or 0 to skip: ")
                if choice == "1":
                    self.countdown(self.short_break)
                elif choice == "0":
                    print("Skipping the short break.")
                else:
                    print("Invalid choice. Skipping the short break.")

            choice = input("Enter 1 to continue or 0 to stop: ")
            if choice == "0":
                print("Pomodoro timer stopped.")
                break
            elif choice == "1":
                self.seconds = self.pomodoro_length
            else:
                print("Invalid choice. Exiting.")
                break

    def countdown(self, duration):
        """Countdown in minutes and seconds."""
        self.seconds = duration
        while self.seconds > 0:
            mins, secs = divmod(self.seconds, 60)
            timeformat = "{:02d}:{:02d}".format(mins, secs)
            print(timeformat, end="\r")
            time.sleep(0.1)
            self.seconds -= 1
