import typer

app = typer.Typer()


@app.command()
def create():
    print("Creating user: Yugi Muto")


@app.command()
def delete():
    print("Deleting user: Yugi Muto")


if __name__ == "__main__":
    app()
