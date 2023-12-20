# It is not necessary to have variable declaration inside the while loop
# Only put in the while loop things that can be executed in cycles or multiple times.

# from functions import get_todos, write_todos

import functions
import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print('It is', now)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:].capitalize() + '\n'
        todos = functions.get_todos('todos.txt')
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        if not todos:
            print("No todos found.")
        else:
            for index, todo in enumerate(todos):
                print(f'{index + 1}. {todo.strip()}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            todos = functions.get_todos()

            if 0 <= number < len(todos):
                new_todo = input("Enter a new todo: ").capitalize() + '\n'
                todos[number] = new_todo

                functions.write_todos(todos)

            else:
                print('Invalid todo number.')

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1

            if 0 <= index < len(todos):
                todo_to_remove = todos[index].strip()
                todos.pop(index)

                functions.write_todos(todos)

                message = f'Todo {todo_to_remove} was removed from the list.'
                print(message)
            else:
                print('Invalid todo number.')

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Command is not valid.')

print('Bye')
