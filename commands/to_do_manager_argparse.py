import argparse
import json


def add(task: str):
    """Adds a task to the to-do list."""
    with open("todo.json") as f:
        todo = json.load(f)

    # append the new task to the list
    todo.append(task)

    # save the to-do list to the file
    with open("todo.json", "w") as f:
        json.dump(todo, f)


def list():
    """Lists all tasks in the to-do list."""
    with open("todo.json") as f:
        todo = json.load(f)
    if len(todo) == 0:
        print("The list is empty!")
        return None
    # print the tasks in the list
    print("Tasks:")
    for task in todo:
        print(f"- {task}")


def delete(task: str):
    """Deletes a task from the to-do list."""
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
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # Create the parser for the "add" command
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("task", type=str, help="Adds a task to the to-do list.")

    # Create the parser for the "list" command
    parser_list = subparsers.add_parser("list")

    # Create the parser for the "delete" command
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument(
        "task", type=str, help="Deletes a task from the to-do list."
    )

    # Parse the arguments
    args = parser.parse_args()

    if args.command == "add":
        add(args.task)
    elif args.command == "list":
        list()
    elif args.command == "delete":
        delete(args.task)
