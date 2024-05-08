# Steepest Hill Climb

# import copy
#
#
# q = []
# visited = []
#
#
# def find_pos(s):
#     for i in range(3):
#         for j in range(3):
#             if s[i][j] == 0:
#                 return [i, j]
#
#
# def up(s, pos):
#     i = pos[0]
#     j = pos[1]
#
#     if i > 0:
#         temp = copy.deepcopy(s)
#         temp[i][j] = temp[i-1][j]
#         temp[i-1][j] = 0
#         return temp
#     else:
#         return s
#
#
# def down(s, pos):
#     i = pos[0]
#     j = pos[1]
#
#     if i < 2:
#         temp = copy.deepcopy(s)
#         temp[i][j] = temp[i+1][j]
#         temp[i+1][j] = 0
#         return temp
#     else:
#         return s
#
#
# def right(s, pos):
#     i = pos[0]
#     j = pos[1]
#
#     if j < 2:
#         temp = copy.deepcopy(s)
#         temp[i][j] = temp[i][j+1]
#         temp[i][j+1] = 0
#         return temp
#     else:
#         return s
#
#
# def left(s, pos):
#     i = pos[0]
#     j = pos[1]
#
#     if j > 0:
#         temp = copy.deepcopy(s)
#         temp[i][j] = temp[i][j-1]
#         temp[i][j-1] = 0
#         return temp
#     else:
#         return s
#
#
# def enqueue(s, val):
#     global q
#     q = q + [(val, s)]
#
#
# def heuristic(s, g):
#     d = 0
#     for i in range(3):
#         for j in range(3):
#             if s[i][j] != g[i][j]:
#                 d += 1
#     return d
#
#
# def dequeue():
#     global q
#     global visited
#
#     q.sort()
#     visited = visited + [q[0][1]]
#
#     elem = q[0][1]
#     q = []
#     return elem
#
#
# def search(s, g):
#     curr_state = copy.deepcopy(s)
#     if s == g:
#         return
#
#     global visited
#
#     while True:
#         pos = find_pos(curr_state)
#
#         new = up(curr_state, pos)
#         if new != curr_state:
#             if new == g:
#                 print("Found!")
#                 print("The intermediate states are:")
#                 visited = visited + [g]
#                 for i in range(len(visited)):
#                     print(visited[i])
#                 return
#             else:
#                 if new not in visited:
#                     enqueue(new, heuristic(new, g))
#
#         new = down(curr_state, pos)
#         if new != curr_state:
#             if new == g:
#                 print("Found!")
#                 print("The intermediate states are:")
#                 visited = visited + [g]
#                 for i in range(len(visited)):
#                     print(visited[i])
#                 return
#             else:
#                 if new not in visited:
#                     enqueue(new, heuristic(new, g))
#
#         new = left(curr_state, pos)
#         if new != curr_state:
#             if new == g:
#                 print("Found!")
#                 print("The intermediate states are:")
#                 visited = visited + [g]
#                 for i in range(len(visited)):
#                     print(visited[i])
#                 return
#             else:
#                 if new not in visited:
#                     enqueue(new, heuristic(new, g))
#
#         new = right(curr_state, pos)
#         if new != curr_state:
#             if new == g:
#                 print("Found!")
#                 print("The intermediate states are:")
#                 visited = visited + [g]
#                 for i in range(len(visited)):
#                     print(visited[i])
#                 return
#             else:
#                 if new not in visited:
#                     enqueue(new, heuristic(new, g))
#
#         if len(q) > 0:
#             curr_state = dequeue()
#         else:
#             print("not found")
#             return
#
#
# def main():
#     s = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
#     g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
#     global q
#     global visited
#     q = q
#     visited = visited + [s]
#     search(s, g)
#
#
# if __name__ == "__main__":
#     main()


# Simple Hill Climb

import copy


visited = []


def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return [i, j]


def up(s, pos):
    i = pos[0]
    j = pos[1]

    if i > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i-1][j]
        temp[i-1][j] = 0
        return temp
    else:
        return s


def down(s, pos):
    i = pos[0]
    j = pos[1]

    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0
        return temp
    else:
        return s


def right(s, pos):
    i = pos[0]
    j = pos[1]

    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0
        return temp
    else:
        return s


def left(s, pos):
    i = pos[0]
    j = pos[1]

    if j > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0
        return temp
    else:
        return s


def heuristic(s, g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    return d


def search(s, g):
    curr_state = copy.deepcopy(s)
    if s == g:
        return

    h = heuristic(s, g)

    global visited

    while True:
        visited = visited + [curr_state]
        pos = find_pos(curr_state)

        new = left(curr_state, pos)
        print(new)
        if new != curr_state:
            if new == g:
                print("Found!")
                print("The intermediate states are:")
                visited = visited + [g]
                for i in range(len(visited)):
                    print(visited[i])
                return
            else:
                if new not in visited:
                    h1 = heuristic(new, g)
                    if h1 < h:
                        curr_state = new
                        h = h1
                        # print(new)
                        continue

        new = right(curr_state, pos)
        print(new)
        if new != curr_state:
            if new == g:
                print("Found!")
                print("The intermediate states are:")
                visited = visited + [g]
                for i in range(len(visited)):
                    print(visited[i])
                return
            else:
                if new not in visited:
                    h1 = heuristic(new, g)
                    if h1 < h:
                        curr_state = new
                        h = h1
                        # print(new)
                        continue

        new = up(curr_state, pos)
        print(new)
        if new != curr_state:
            if new == g:
                print("Found!")
                print("The intermediate states are:")
                visited = visited + [g]
                for i in range(len(visited)):
                    print(visited[i])
                return
            else:
                if new not in visited:
                    h1 = heuristic(new, g)
                    if h1 < h:
                        curr_state = new
                        h = h1
                        # print(new)
                        continue

        new = down(curr_state, pos)
        print(new)
        if new != curr_state:
            if new == g:
                print("Found!")
                print("The intermediate states are:")
                visited = visited + [g]
                for i in range(len(visited)):
                    print(visited[i])
                return
            else:
                if new not in visited:
                    h1 = heuristic(new, g)
                    if h1 < h:
                        curr_state = new
                        h = h1
                        print(new)
                        continue

        print("not found")
        return


def main():
    s = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    search(s, g)


if __name__ == "__main__":
    main()
