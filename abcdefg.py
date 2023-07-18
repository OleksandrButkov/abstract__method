from abc import ABC, abstractmethod


class UI(ABC):
    @abstractmethod
    def print_menu(self):
        pass

    @abstractmethod
    def print_contact(self, contact):
        pass

    @abstractmethod
    def print_message(self, message):
        pass

    @abstractmethod
    def get_input(self, prompt):
        pass


class ConsoleUI(UI):
    def print_menu(self):
        print("1. Add contact")
        print("2. Change phone")
        print("3. Change email")

    def print_contact(self, contact):
        print(contact)

    def print_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)


