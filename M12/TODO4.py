class Point:
    """Representa un punto (x, y)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def midpoint(self, other):
        """Calcula el punto medio entre este punto y otro."""
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Point(mid_x, mid_y)
        
    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

class Line:
    """Representa una línea definida por dos puntos."""
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_midpoint(self) -> Point:
        """Calcula el punto medio de esta línea."""
        return self.start.midpoint(self.end)

# --- CLASE RECTANGLE CON EL NUEVO MÉTODO ---
class Rectangle:
    """Clase Rectangle con el método make_cross."""

    def make_lines(self) -> list:
        A = Point(0, 10)    # Superior Izquierdo
        B = Point(10, 10)   # Superior Derecho
        C = Point(10, 0)    # Inferior Derecho
        D = Point(0, 0)     # Inferior Izquierdo

        return [
            Line(A, B), # 0: Superior
            Line(B, C), # 1: Derecho
            Line(C, D), # 2: Inferior
            Line(D, A)  # 3: Izquierdo
        ]

    def make_cross(self) -> list:
        """
        Calcula los puntos medios de los lados opuestos y crea dos líneas que forman una cruz.

        Devuelve: Una lista de dos objetos Line ([Línea Vertical, Línea Horizontal]).
        """
        # 1. Obtener los cuatro lados
        sides = self.make_lines()

        # 2. Calcular los cuatro puntos medios
        # midpoints = [Mid_Superior, Mid_Derecho, Mid_Inferior, Mid_Izquierdo]
        midpoints = [line.get_midpoint() for line in sides]

        # 3. Emparejar los puntos medios opuestos
        mid_top = midpoints[0]
        mid_bottom = midpoints[2]
        mid_left = midpoints[3]
        mid_right = midpoints[1]

        # 4. Crear las dos líneas de la cruz
        cross_line_1 = Line(mid_top, mid_bottom) # Línea Vertical
        
        cross_line_2 = Line(mid_left, mid_right) # Línea Horizontal
        return [cross_line_1, cross_line_2]