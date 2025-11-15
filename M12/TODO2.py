class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        """
        Calcula el punto medio y lo devuelve como un objeto Point.
        """
        # Calcular el promedio de las coordenadas X e Y
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2

        # Crear y devolver el nuevo objeto Point
        return Point(mid_x, mid_y)