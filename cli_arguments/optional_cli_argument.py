from typing import Optional

import typer


def hello(name: Optional[str] = typer.Argument(None)):
    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}!")


if __name__ == "__main__":
    typer.run(hello)
