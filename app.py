todos = []


def add_todo(title):
    if not title.strip():
        raise ValueError("Todo title cannot be empty")

    todo = {
        "id": len(todos) + 1,
        "title": title,
        "completed": False,
    }

    todos.append(todo)
    return todo


def get_todos():
    return todos