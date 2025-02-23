from collections import deque

mango_sellers = ["thom", "alice"]
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def find_nearest_mango_seller(name):
    search_queue = deque()
    search_queue += graph[name]   
    searched = set()                       
    while search_queue:
        person = search_queue.popleft()  
        if not person in searched:            
            if person in mango_sellers:
                return person
            else:
                search_queue += graph[person]   
                searched.add(person)


mango_seller = find_nearest_mango_seller('you')
print(f'{mango_seller} is a mango seller!'.capitalize())
