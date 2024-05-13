from abc import ABC, abstractmethod


class Printer(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book):
        pass


class ConsolePrinter(Printer):
    @staticmethod
    def print_book(book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    @staticmethod
    def print_book(book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
