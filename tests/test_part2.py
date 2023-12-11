from src.part2 import Car
from src.part6 import get_address_lit, get_interfaces


def test_drive_car():
    """test the car's drive methos"""
    my_car = Car()
    assert my_car.drive() == "Driving a car"


def test_get_address_lit():
    """test the get_address_lit function"""

    result = get_address_lit()
    assert isinstance(result, list)


def test_get_interfaces():
    """test the get_interfaces function"""

    result = get_interfaces()
    assert isinstance(result, list)
