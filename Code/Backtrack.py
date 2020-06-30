

## DFS is the same

result = []
def backtrack(path, choices):
    if end:
        result.add(path)
        return

    if pruning():
        return

    for choice in choices:
        make(choice)
        backtrack(new_path, choices)
        delete(choice)