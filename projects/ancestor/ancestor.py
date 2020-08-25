
def build_dict(people):
    dict = {}
    for person in people:
        if person[1] in dict:
            dict[person[1]].add(person[0])
        else:
            dict[person[1]] = set()
            dict[person[1]].add(person[0])

    return dict


# Ancestors is a list of Tuples.
def earliest_ancestor(ancestors, starting_node):
    people = build_dict(ancestors)

    if starting_node not in people:
        return -1

    queue = []
    queue.append([starting_node])
    path = []
    visited = set()

    while len(queue) > 0:
        current_path = queue.pop()
        vertex = current_path[-1]

        if vertex not in visited:

            if len(path) == 0:
                path = current_path
            elif len(current_path) > len(path):
                path = current_path
            elif len(current_path) == len(path) and current_path[-1] < path[-1]:
                path = current_path

            visited.add(vertex)

            ancestors = None
            if vertex in people:
                ancestors = people[vertex]

            if ancestors is not None:
                for person in ancestors:
                    new_path = list(current_path)
                    new_path.append(person)
                    queue.append(new_path)

    return path[-1]
