class Point:
    """Clase simple para representar un punto (x, y)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Define la igualdad entre dos objetos Point."""
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    """Clase para representar una línea definida por dos puntos."""
    def __init__(self, p1, p2):
        # p1 y p2 son objetos de la clase Point
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        """
        Devuelve True si los objetos Line se refieren a objetos Point equivalentes,
        en cualquier orden.
        """
        # 1. Verificar si 'other' es una instancia de Line
        if not isinstance(other, Line):
            return NotImplemented

        # 2. Comprobar la igualdad en el orden (p1_self == p1_other Y p2_self == p2_other)
        orden_a = (self.p1 == other.p1 and self.p2 == other.p2)

        # 3. Comprobar la igualdad en orden inverso (p1_self == p2_other Y p2_self == p1_other)
        orden_b = (self.p1 == other.p2 and self.p2 == other.p1)

        # La línea es la misma si se cumple cualquiera de las dos condiciones
        return orden_a or orden_b

    def __repr__(self):
        return f"Line({self.p1!r}, {self.p2!r})"