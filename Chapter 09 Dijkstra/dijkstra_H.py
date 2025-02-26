from math import inf

graph = {}

graph['book'] = {}
graph['book']['LP'] = 5
graph['book']['poster'] = 0
graph['poster'] = {}
graph['poster']['drums'] = 35
graph['poster']['bass'] = 30
graph['LP'] = {}
graph['LP']['drums'] = 20
graph['LP']['bass'] = 15
graph['bass'] = {}
graph['bass']['piano'] = 20
graph['drums'] = {}
graph['drums']['piano'] = 10
graph['piano'] = {}
start = 'book'
target = 'piano'

res = {}
for node in graph:
    res[node] = (inf, None)
res[start] = (0, None)
    
copied_graph = graph.copy()
    
while copied_graph:
    lowest_cost = inf
    for node in copied_graph:
        if res[node][0] < lowest_cost:
            lowest_cost = res[node][0]
            lowest_cost_node = node
    for neighbor, cost in copied_graph[lowest_cost_node].items():
        new_cost = lowest_cost + cost
        if new_cost < res[neighbor][0]:
            res[neighbor] = (new_cost, lowest_cost_node)
    copied_graph.pop(lowest_cost_node)

items = sorted(res.items(), key=lambda x: x[1][0])
i = list(res.keys()).index(target)
for item in items[:i]:
    print(f'{item[0]} → ', end='')
    
print(items[i][0])
