from abc import ABC


class Render(ABC):
    def render_circle(self, radius: float):
        ...


class VectorRender(Render):
    def render_circle(self, radius: float):
        print(f"Draw circle with radius {radius}")


class RasterRender(Render):
    def render_circle(self, radius: float):
        print(f"Draw pixels of circle with radius {radius}")


class Shape:
    def __init__(self, render: Render):
        self.render = render

    def draw(self):
        pass

    def resize(self, factor: float):
        pass


class Circle(Shape):
    def __init__(self, render: Render, radius):
        super().__init__(render)
        self.radius = radius

    def draw(self):
        self.render.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRender()
    vector = VectorRender()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
    circle.render = raster
    circle.draw()
    circle.resize(2)
    circle.draw()

import sys
from abc import ABC
