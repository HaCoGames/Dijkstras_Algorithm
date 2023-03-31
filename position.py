import math

class Position:
    def __init__(self, name):
        self.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self.name + other.name

    def __sub__(self, other):
        return self.name - other.name

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name
