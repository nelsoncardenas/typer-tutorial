import typer


def hello(name: str = typer.Option(...)):
    print(f"Hello {name}!")


if __name__ == "__main__":
    typer.run(hello)
