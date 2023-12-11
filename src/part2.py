from abc import ABC, abstractmethod


class Vehicule(ABC):
    """Reprensent a vehicule"""

    @abstractmethod
    def drive(self):
        """Drive the vehicule"""
        raise NotImplementedError


class Car(Vehicule):
    """Reprensent a car"""

    def drive(self):
        """override drive method"""
        print("Driving a car")


class Person:
    """Represent a person"""

    def __init__(self, called_name: str, age: int) -> None:
        self._called_name = called_name
        self._age = age

    def get_called_name(self) -> str:
        """Return the called name"""
        return self._called_name

    def get_age(self) -> int:
        """Return the age"""
        return self._age

    def set_called_name(self, called_name: str) -> None:
        """Set the called name"""
        self._called_name = called_name

    def set_age(self, age: int) -> None:
        """Set the age"""
        self._age = age


class Animal(ABC):
    """Represent an animal"""

    @abstractmethod
    def called_speak(self):
        """Called speak method"""
        raise NotImplementedError


class Dog(Animal):
    """Reprensent a dog"""

    def called_speak(self):
        """override called speak method"""
        print("Wouaf")


class Cat(Animal):
    """Represent a Cat"""

    def called_speak(self):
        """override called speak method"""
        print("Miaou")


class Singleton:
    """Represent a singleton"""

    __instance = None

    @staticmethod
    def get_instance():
        """Return the instance"""
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
