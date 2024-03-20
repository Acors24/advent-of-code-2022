from pprint import pprint


with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def mkdir(name, parent):
    return {
        'name': name,
        'size': 0,
        'parent': parent,
        'children': {},
        'files': {}
    }


root = mkdir('/', None)

current = None
for line in lines:
    match line.split():
        case ['$', 'cd', '/']:
            current = root
        case ['$', 'cd', '..']:
            current = current['parent']
        case ['$', 'cd', dir_name]:
            if dir_name not in current['children']:
                current['children'][dir_name] = mkdir(dir_name, current)
            current = current['children'][dir_name]
        case ['$', 'ls']:
            pass
        case ['dir', dir_name]:
            if dir_name not in current['children']:
                current['children'][dir_name] = mkdir(dir_name, current)
        case [size, filename]:
            if filename not in current['files']:
                current['files'][filename] = int(size)
        case _:
            print('???')


def calculate_size(dir: dict):
    for child_dir in dir['children'].values():
        calculate_size(child_dir)
        dir['size'] += child_dir['size']

    for filesize in dir['files'].values():
        dir['size'] += filesize


calculate_size(root)


def get_total_size_if_less_than_100k(dir: dict):
    total = 0
    for child_dir in dir['children'].values():
        total += get_total_size_if_less_than_100k(child_dir)

    if dir['size'] <= 100_000:
        total += dir['size']
    return total


# print(get_total_size_if_less_than_100k(root))

total_size = 70_000_000
needed_size = 30_000_000 - total_size + root['size']
from math import inf


def find_to_delete(dir: dict, needed_size: int) -> list:
    if dir['size'] < needed_size:
        return

    best_name, best_size = (None, inf)
    if needed_size <= dir['size'] < best_size:
        best_name, best_size = (dir['name'], dir['size'])

    for child_dir in dir['children'].values():
        if child_dir['size'] >= needed_size:
            res_name, res_size = find_to_delete(child_dir, needed_size)
            if needed_size <= res_size < best_size:
                best_name, best_size = (res_name, res_size)

    return best_name, best_size


print(find_to_delete(root, needed_size))
