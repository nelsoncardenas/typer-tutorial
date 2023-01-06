import argparse


def add(number1: int = 21, number2: int = 21):
    """Adds two numbers together and prints the result."""
    print(number1 + number2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", type=int, nargs="?", default=21)
    parser.add_argument("number2", type=int, nargs="?", default=21)
    args = parser.parse_args()

    add(args.number1, args.number2)
