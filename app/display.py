from abc import ABC, abstractmethod


class Display(ABC):
    @staticmethod
    @abstractmethod
    def display_content(book):
        pass


class ConsoleDisplay(Display):
    @staticmethod
    def display_content(book):
        print(book.content)


class ReverseDisplay(Display):
    @staticmethod
    def display_content(book):
        print(book.content[::-1])
