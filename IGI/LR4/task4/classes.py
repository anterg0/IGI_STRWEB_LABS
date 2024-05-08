from abc import ABC, abstractmethod
import math

class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Color:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def calculate_area(self):
        return self.width * self.height

    def get_info(self):
        return f"Rectangle {self.color.color} with width {self.width}, height {self.height}, and area {self.calculate_area()}"

class Pentagon(GeometricFigure):
    def __init__(self, side_length, color):
        super().__init__()
        self.side_length = side_length
        self.color = Color(color)

    def calculate_area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length**2

    def get_info(self):
        return f"Pentagon {self.color.color} with side length {self.side_length} and area {self.calculate_area()}"