states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

solution = []

while states_needed:
    max_states_coverd = 0
    for station, states in stations.items():
        states_covered = states_needed & states
        if len(states_covered) > max_states_coverd:
            max_states_coverd = len(states_covered)
            best_station = station
    if max_states_coverd == 0:
        print('There are states in states_needed that cannot be covered by all stations!')
        break
    solution.append(best_station)
    states_needed -= stations.pop(best_station)

print(solution)
