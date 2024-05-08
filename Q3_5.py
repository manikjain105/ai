import math
import random


def heuristic(sol):
    h1 = 0
    a, b, c, d = sol
    f = [[not a or d], [c or b], [not c or not d], [not d or not b], [not a or not d]]
    for i in f:
        if i[0]:
            h1 = h1 + 1
    return h1


def generate_new(sol):
    index = random.randint(0, 3)
    if sol[index] == 1:
        sol[index] = 0
    else:
        sol[index] = 1
    return sol


initial = [1, 1, 1, 1]
t = 500
s = initial
ho = heuristic(s)
# r = [0.655, 0.254, 0.432]
k = 0
print(s, ho)
while t > 0:
    s1 = generate_new(s)
    hn = heuristic(s1)
    e = hn - ho
    if hn > ho:
        s = s1
    else:
        p = 1/(1 + math.e**(-e/t))
        if p >= 0.5:
            s = s1
    print(s1, hn)
    ho = hn
    t = t - 50
