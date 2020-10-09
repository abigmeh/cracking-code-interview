
'''
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

'''

# whether there is a road
def exist_path(graph, start, end):
    if start == end:
        return True
    path = []
    path.append(start)
    visted =[]
    while path:
        u = path.pop()
        visted.append(u)
        if u is not None:
            for node in graph[u]:
                if node not in visted:
                    if node == end:
                        return True
                    else:
                        path.append(node)
    return False

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
y = exist_path(graph, 'A', 'B')
print(y)


'''
bonus, find the path
'''
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

x = find_path(graph, 'A', 'B')
print(x)