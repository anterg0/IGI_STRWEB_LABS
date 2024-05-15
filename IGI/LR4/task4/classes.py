from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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
    
class Mixin():
    def getName(self):
        print(str(type(self).__name__))

class Rectangle(GeometricFigure, Mixin):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def calculate_area(self):
        return self.width * self.height

    def get_info(self):
        return f"Rectangle {self.color.color} with width {self.width}, height {self.height}, and area {self.calculate_area()}"

class Pentagon(GeometricFigure, Mixin):
    def __init__(self, side_length, color):
        super().__init__()
        self.side_length = side_length
        self.color = Color(color)

    def calculate_area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length**2

    def get_info(self):
        return f"Pentagon {self.color.color} with side length {self.side_length} and area {self.calculate_area()}"
    def draw(self):
        center = (0, 0)  # Center of the pentagon
        radius = self.side_length / (2 * math.sin(math.pi / 5))  # Radius of the circumscribed circle
        theta = math.pi / 2  # Initial angle
        vertices = []
        for _ in range(5):
            x = center[0] + radius * math.cos(theta)
            y = center[1] + radius * math.sin(theta)
            vertices.append((x, y))
            theta += 2 * math.pi / 5

        # Create a matplotlib Polygon object
        polygon = Polygon(vertices, closed=True, facecolor=self.color.color)

        # Create a figure and axes
        fig, ax = plt.subplots()

        # Add the polygon to the axes
        ax.add_patch(polygon)

        # Set the aspect ratio of the axes to equal
        ax.set_aspect('equal')

        # Set the limits of the axes
        ax.set_xlim(-radius, radius)
        ax.set_ylim(-radius, radius)

        # Show the plot
        plt.show()