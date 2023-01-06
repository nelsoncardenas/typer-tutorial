import typer


def hello(
    name: str = typer.Argument("Andrew", help="The name of the user to greet"),
    lastname: str = typer.Option("Ng", help="The last name of the user to greet"),
):
    "Say hi to `name` `lastname` very gently."
    print(f"Hello {name} {lastname}!")


if __name__ == "__main__":
    typer.run(hello)
