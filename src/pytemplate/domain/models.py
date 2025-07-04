from dataclasses import dataclass


@dataclass
class City:
    name: str
    country: str
    population: int

    def __post_init__(self):
        self._validate_name()
        self._validate_country()
        self._validate_population()

    def _validate_name(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("City name must be a non-empty string.")
        if any(char.isdigit() for char in self.name):
            raise ValueError("City name cannot contain numbers.")

    def _validate_country(self):
        if not self.country or not isinstance(self.country, str):
            raise ValueError("Country must be a non-empty string.")

    def _validate_population(self):
        if not isinstance(self.population, int) or self.population < 0:
            raise ValueError("Population must be a non-negative integer.")

    def is_very_big_city(self):
        return self.population > 50000000

    def is_big_city(self):
        return 30000000 <= self.population <= 50000000

    def is_medium_city(self):
        return 10000000 < self.population < 30000000

    def is_small_city(self):
        return self.population <= 10000000
