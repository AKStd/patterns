from abc import ABC


class Shape:
    def __init__(self, render: 'Renderer'):
        self.name = None
        self.render = render

    def __str__(self):
        return f'Drawing {self.name} as {self.render.what_to_render_as}'


class Triangle(Shape):
    def __init__(self, render: 'Renderer'):
        super().__init__(render)
        self.name = 'Triangle'


class Square(Shape):
    def __init__(self, render: 'Renderer'):
        super().__init__(render)
        self.name = 'Square'


class Renderer(ABC):
    render_name = None
    render_name_plural = None

    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):

    @property
    def what_to_render_as(self):
        return 'lines'


class RasterRenderer(Renderer):

    @property
    def what_to_render_as(self):
        return 'pixels'


# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer

# код ниже руками не трогать
sq = Square(VectorRenderer())
tr = Triangle(RasterRenderer())

print(f'{str(sq)} {str(tr)}')
