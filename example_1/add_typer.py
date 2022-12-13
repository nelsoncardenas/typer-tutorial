import typer


def add(number1: int, number2: int):
    """Adds two numbers together and prints the result."""
    print(number1 + number2)


if __name__ == "__main__":
    typer.run(add)
