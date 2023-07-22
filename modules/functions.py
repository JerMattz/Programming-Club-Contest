FILEPATH = 'Files/todos.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


intro_text = '''
TODO APP
Make your life easy and efficient.
'''
print(intro_text)

# print(__name__)
if __name__ == "__main__":
    print(get_todos())
