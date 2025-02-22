from collections import deque


def nearest_mango_seller(graph):
    search_queue = deque()
    search_queue.extend(graph['you'])
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched and person in mango_sellers:
            print(person)
            return True
        search_queue.extend(graph[person])
        searched.add(person)

    return False


mango_sellers = ['thom', 'bob']

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

nearest_mango_seller(graph)
