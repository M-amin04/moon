todos = []


def add_todo(title):
    todo = {
        "id": len(todos) + 1,
        "title": title,
        "completed": False,
    }

    todos.append(todo)
    return todo

def get_todos():
    return todos