import typer


def hello(name: str = typer.Argument(...)):
    print(f"Hello {name}!")


if __name__ == "__main__":
    typer.run(hello)
