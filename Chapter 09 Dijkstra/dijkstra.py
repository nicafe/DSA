import math


def dijkstra(graph, start='start'):
    # Initiate a result dictionary where res[node] = (cost, parent).
    res = {}
    for node in graph:
        res[node] = (math.inf, None)
    res[start] = (0, None)
    
    # Use a copied graph to keep the original one unchanged.
    copied_graph = graph.copy()
    
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


def print_path(res, target='end', entry=True):
    parent = res[target][1]
    if parent is None:
        print(f'The shortest path: {target}', end='')
    else:
        print_path(res, parent, False)
        print(f' -> {target}', end='')
    if entry:
        print()
    

# Build the graph.
graph = {}

# Start to End.
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}
start = 'start'
target = 'end'

# # Book to Piano.
# graph['book'] = {}
# graph['book']['LP'] = 5
# graph['book']['poster'] = 0
# graph['poster'] = {}
# graph['poster']['drums'] = 35
# graph['poster']['bass'] = 30
# graph['LP'] = {}
# graph['LP']['drums'] = 20
# graph['LP']['bass'] = 15
# graph['bass'] = {}
# graph['bass']['piano'] = 20
# graph['drums'] = {}
# graph['drums']['piano'] = 10
# graph['piano'] = {}
# start = 'book'
# target = 'piano'

# Print the result.
res = dijkstra(graph, start)
print('The result dictionary:')
for k, v in res.items():
    print(k, v)
print()
print(f"The total length of the shortest path: {res[target][0]}")
print_path(res, target)
