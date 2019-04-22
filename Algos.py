import Queue

#Breadth First Search

def BFS(start,end):
    queue = [[start]]
    visited = set()

    while queue:

        path = queue.pop(0)
        v = path[-1]

        if v == end:
            return path

        elif v not in visited:
            for neighbor in v.neighbors():
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(v)

    return None