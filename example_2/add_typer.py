import typer


def add_two_numbers(number1: int = 21, number2: int = 21):
    """Adds two numbers together and prints the result."""
    print(number1 + number2)


if __name__ == "__main__":
    typer.run(add_two_numbers)
