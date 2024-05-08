def calculate_path_cost(H, condition, weight=1):
    cost = {}
    if 'AND' in condition:
        and_nodes = condition['AND']
        path_a = sum(H[node] + weight for node in and_nodes)
        cost[' AND '.join(and_nodes)] = path_a

    if 'OR' in condition:
        or_nodes = condition['OR']
        path_b = min(H[node] + weight for node in or_nodes)
        cost[' OR '.join(or_nodes)] = path_b
    return cost

def update_cost_and_get_least(conditions, H, weight=1):
    least_cost = {}
    for key in reversed(conditions):
        condition = conditions[key]
        print(f"{key}: {condition} >>> {calculate_path_cost(H, condition, weight)}")
        cost = calculate_path_cost(H, condition, weight)
        H[key] = min(cost.values())
        least_cost[key] = calculate_path_cost(H, condition, weight)
    return least_cost

def get_shortest_path(start, updated_cost, H):
    path = start
    if start in updated_cost:
        min_cost = min(updated_cost[start].values())
        min_key = min(updated_cost[start], key=updated_cost[start].get)
        next_nodes = min_key.split()

        if len(next_nodes) == 1:
            start = next_nodes[0]
            path += '<--' + get_shortest_path(start, updated_cost, H)
        else:
            path += '<--(' + min_key + ') '
            start = next_nodes[0]
            path += '[' + get_shortest_path(start, updated_cost, H) + ' + '
            start = next_nodes[-1]
            path += get_shortest_path(start, updated_cost, H) + ']'
    return path


H = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}

conditions = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}

# weight
weight = 1

# Updated cost
print('Updated Cost:')
updated_cost = update_cost_and_get_least(conditions, H, weight)
print('*' * 75)
print('Shortest Path:\n', get_shortest_path('A', updated_cost, H))
