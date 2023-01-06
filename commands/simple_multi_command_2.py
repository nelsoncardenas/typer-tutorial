import typer

app = typer.Typer()


@app.command()
def create(username: str):
    """Creates a user."""
    print(f"Creating user: {username}")


@app.command()
def delete(username: str):
    """Deletes a user."""
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
