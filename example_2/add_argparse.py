import argparse


def add_two_numbers(number1: int = 21, number2: int = 21):
    """Adds two numbers together and prints the result."""
    print(number1 + number2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", type=int)
    parser.add_argument("number2", type=int)
    args = parser.parse_args()

    add_two_numbers(args.number1, args.number2)
