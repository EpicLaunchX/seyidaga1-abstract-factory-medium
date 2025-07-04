import pytest

from src.pytemplate.domain.models import City


def test_city():
    City.name = "Baku"
    City.country = "Azerbaijan"
    City.population = 10000000

    assert City.name == "Baku"
    assert City.country == "Azerbaijan"
    assert City.population == 10000000


def test_is_very_big_city():
    assert City(name="Tokyo", country="Japan", population=51000000).is_very_big_city()
    assert not City(name="Baku", country="Azerbaijan", population=2300000).is_very_big_city()


def test_is_big_city():
    assert City(name="Tokyo", country="Japan", population=37000000).is_big_city()
    assert not City(name="Baku", country="Azerbaijan", population=2300000).is_big_city()


def test_is_medium_city():
    assert City(name="Tokyo", country="Japan", population=23000000).is_medium_city()
    assert not City(name="Baku", country="Azerbaijan", population=9000000).is_medium_city()


def test_is_small_city():
    assert City(name="Tokyo", country="Japan", population=9000000).is_small_city()
    assert not City(name="Baku", country="Azerbaijan", population=23000000).is_small_city()


def test_city_name_with_number():
    with pytest.raises(ValueError):
        City(name="Baku123", country="Azerbaijan", population=100000)


def test_city_negative_population():
    with pytest.raises(ValueError):
        City(name="Baku", country="Azerbaijan", population=-100)


def test_city_invalid_population_type():
    with pytest.raises(ValueError):
        City(name="Baku", country="Azerbaijan", population="many")


def test_city_invalid_name():
    with pytest.raises(ValueError):
        City(name="", country="Azerbaijan", population=100000)


def test_city_invalid_country():
    with pytest.raises(ValueError):
        City(name="Baku", country="", population=100000)
