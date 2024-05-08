def calculate_fitness(chromosome):
    tw = 0
    tp = 0
    for x in range(len(chromosome)):
        if chromosome[x] == 1:
            tw += weight[x]
            tp += profit[x]
    return tw, tp


def crossover():
    crossover_point = int(n / 2)
    c1 = parent1[:crossover_point] + parent2[crossover_point:]
    c2 = parent2[:crossover_point] + parent1[crossover_point:]
    return c1, c2


def mutate(chromosome):
    mutation_point = mp[k]
    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0
    return chromosome


def sort_pop():
    result = []
    for chromosome in population:
        cw, cp = calculate_fitness(chromosome)
        if cw > max_weight:
            cp = -1
        result.append([cp, chromosome])
        # if cw <= max_weight:
        #     result.append([cp, chromosome])
    result = sorted(result, reverse=True)
    r = []
    for z in result:
        if z[1] not in r:
            r.append(z[1])
    return r


# Main
weight = [2, 3, 4, 5]
profit = [3, 5, 7, 9]

print("Weight", weight)
print("Profit", profit)

max_weight = 9
n = 4
population = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
generations = 10
print(population)
mp = [2, 0, 3, 1]
k = 0
for i in range(generations):
    population = sort_pop()
    print(population)
    parent1 = population[3]
    parent2 = population[2]
    # parent1 = population[2]
    # parent2 = population[3]

    child1, child2 = crossover()

    child1 = mutate(child1)
    # child2 = mutate(child2)
    k = k + 1
    if k == 4:
        k = 0

    population.append(child1)
    population.append(child2)

population = sort_pop()
w, p = calculate_fitness(population[0])
print("\nThe best solution:")
print(population[0])
print("Weight:", w)
print("Value:", p)
