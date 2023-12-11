import time
from logging import Logger

logger = Logger(__name__)


def get_even_numbers(my_list: list[int]) -> list:
    """
    write a python code that takes in a list of integers and
    retuns a new list containing only the even numbers
    """
    return list(filter(lambda x: x % 2 == 0, my_list))


def my_decorator(func):
    """Log decorator"""

    def wrapper(*args, **kwargs):
        init = time.time()
        func()
        end = time.time()
        logger.info("Execution time: %s", end - init)

    return wrapper


def get_both_elements(list1, list2) -> list:
    """write a python function that takes in two lists and
    returns a new list containing only the elements that appear in both list
    """
    return list(set(list1).intersection(set(list2)))


def get_count_char(my_string: str) -> dict:
    """write a python function that takes in a string and
    returns a dictionary containing the number of times
    each character appears in the string
    """
    return {letter: my_string.count(letter) for letter in my_string}
