import typer


def hello(name: str):
    print(f"Hello {name}!")


if __name__ == "__main__":
    typer.run(hello)
