import argparse


def hello(name: str):
    print(f"Hello {name}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    hello(args.name)
