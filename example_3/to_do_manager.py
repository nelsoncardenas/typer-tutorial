import typer
import json

app = typer.Typer()


@app.command()
def add(task: str):
    """Adds a task to the to-do list."""
    with open("todo.json") as f:
        todo = json.load(f)

    # append the new task to the list
    todo.append(task)

    # save the to-do list to the file
    with open("todo.json", "w") as f:
        json.dump(todo, f)


@app.command()
def list():
    """Lists all tasks in the to-do list."""
    with open("todo.json") as f:
        todo = json.load(f)

    # print the tasks in the list
    print("Tasks:")
    for task in todo:
        typer.echo(f"- {task}")


@app.command()
def remove(task: str):
    """Removes a task from the to-do list."""
    with open("todo.json") as f:
        todo = json.load(f)

    if task not in todo:
        print(f"Task '{task}' not found.")
        return None

    # remove the task from the list
    todo.remove(task)

    # save the to-do list to the file
    with open("todo.json", "w") as f:
        json.dump(todo, f)


if __name__ == "__main__":
    app()
