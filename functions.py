FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return list of existing to-do items."""

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items in the text file."""

    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    """Wird nur ausgeführt, wenn functions direkt ausgeführt wird,
     da es dann "__main__" heißt. Wenn woanders aufgerfufen, ändert sich der Name
     dem Dateinamen entsprechend in __functions__
    """

    print(get_todos())
