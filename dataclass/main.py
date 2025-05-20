from dataclasses import dataclass, field, asdict

@dataclass
class Point:
    x: float = field(default=0.0)
    y: float = field(default=0.0)
    z: float = field(default=0.0, init=False)  # Not included in __init__
    _w: str = field(default="-1.0", init=False)  # Not included in __init__

    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError("Coordinates must be non-negative")
        self.z = self.x + self.y  # Example of a computed field

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    @property
    def w(self):
        return self._w
    @w.setter
    def w(self, value):
        if isinstance(value, float):
            self._w = f"{value:.2f}"
        else:
            self._w = str(value)


# * Example usage
p = Point(1.0, 2.0)
print(p)
print("To dict:", asdict(p))  # {'x': 1.0, 'y': 2.0}

# * Default values
p_default = Point()
print("Default Point:", p_default, asdict(p_default))  # Point(0.0, 0.0)

# * invalid example
try:
    p_invalid = Point(-1.0, 2.0)
except ValueError as e:
    print(f"Error: {e}")
