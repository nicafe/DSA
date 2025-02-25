import math


def dijkstra(graph):
    # Use a copied graph to keep the original one unchanged.
    copied_graph = graph.copy()
    # Initiate result.
    res = {}
    for node, cost in copied_graph.pop('start').items():
        res[node] = (cost, 'start')
    for node in copied_graph:
        if node not in res:
            res[node] = (math.inf, None)
    
    while copied_graph:
        # Find the lowest cost node among the remaining nodes.
        lowest_cost = math.inf
        for node in copied_graph:
            if res[node][0] < lowest_cost:
                lowest_cost = res[node][0]
                lowest_cost_node = node
        # Update its neighbors' costs.
        for neighbor, cost in copied_graph[lowest_cost_node].items():
            new_cost = lowest_cost + cost
            if new_cost < res[neighbor][0]:
                res[neighbor] = (new_cost, lowest_cost_node)
        # Remove the node just processed.
        copied_graph.pop(lowest_cost_node)
    
    return res


def print_path(target, res, entry=True):
    if target == 'start':
        print('The shortest path: start', end='')
    else:
        print_path(res[target][1], res, False)
        print(f' -> {target}', end='')
    if entry:
        print()
    

# Build the graph.
graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph["start"]["b"] = 2

graph['a'] = {}
graph['a']['end'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

graph['end'] = {}

# Print the result.
res = dijkstra(graph)
print('The result dictionary:')
for k, v in res.items():
    print(k, v)
print()
print(f"The total length of the shortest path: {res['end'][0]}")
print_path('end', res)
