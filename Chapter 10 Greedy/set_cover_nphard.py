def find(states_needed, keys, res=[]):
    global min_station_count
    
    if keys == []:
        return
    key = keys.pop()
    # Don't select stations[key].
    find(states_needed.copy(), keys.copy(), res.copy())
    # Select stations[key].
    states_needed -= stations[key]
    res += [key]
    if states_needed == set():
        station_count = len(res)
        if station_count < min_station_count:
            min_station_count = station_count
            solutions.clear()
            solutions.append(res)
        elif station_count == min_station_count:
            solutions.append(res)
        return
    find(states_needed, keys, res)


states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

keys = list(stations.keys())
solutions = []
min_station_count = len(stations)

find(states_needed, keys)
print(min_station_count)
print(solutions)
