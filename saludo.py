"""Script sencillo de ejemplo: saluda y suma dos números."""


def saludar(nombre: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"¡Hola, {nombre}!"


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


if __name__ == "__main__":
    print(saludar("equipo"))
    print(f"2 + 3 = {sumar(2, 3)}")
