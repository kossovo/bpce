from src.part1 import get_both_elements, get_even_numbers, my_decorator, get_count_char


def test_get_both_elements():
    """test the get even numbers function"""
    list1 = ["a", "b", "c", 1, 2, 3]
    list2 = [1, 2, 3, 4, 5, 6]

    assert get_both_elements(list1, list2) == [1, 2, 3]


def test_get_even_numbers():
    """test the get even numbers function"""

    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


@my_decorator
def test_my_decorator():
    """test the my_decorator function"""
    pass


def test_get_count_char():
    """test the function get_count_char"""
    assert get_count_char("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
