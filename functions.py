
FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    This function reads a text file and returns a list of
    to-do items
    :param filepath:
    :return todos:
    """
    with open(filepath, 'r') as f:
        all_todos = f.readlines()
    return all_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """
    This function writes the to-do list to a text file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)
if __name__ == '__main__':
    print(get_todos())
