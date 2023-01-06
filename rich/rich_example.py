import typer
from rich import print

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
    "serial_number": "UUGnCeVMNEpzCVgFZvz4uAGqU2SLK8qX8xC4hsf3p7V8FSBIQxNNvLRvpHFNxfa9",
}


def main():
    print("Here's the data")
    print(data)


if __name__ == "__main__":
    typer.run(main)
