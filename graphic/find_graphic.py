import sys

cost = [0 for x in range(66)]
next = [-1 for x in range(66)]

def is_num(s):
    try:
        int (s)
        return True
    except ValueError:
        return False
flag = 0
visited = []
way = []

def DFS (u, val, depth, limit):
    global flag
    global visited
    global way
    
    if depth > limit: return

#    print u, hex(val), depth
#    wait = raw_input("")

    if flag == 1: return
    if val == 1984717964:
#        flag = 1
        print "pass", way
        return
    way.append(next[u] + 8)
    DFS (next[u], val ^ cost[next[u]], depth + 1, limit)
    if flag == 1: return
    way = way[:-1]

    way.append(u+2 + 8)
    way.append(next[u+2] + 8)
    DFS (next[u+2], val ^ cost[next[u+2]], depth+1, limit)
    if flag == 1: return
    way = way[:-2]

lines = [line.rstrip(';\n') for line in open('data')]
data = [line.split(' = ') for line in lines]

for pair in data:
    u = int(pair[0][1:]) - 8
    if is_num(pair[1]):
        cost[u-1] = int(pair[1])

    else:
        v = int(pair[1][1:]) - 8
        next [u] = v

#arr = [-1 for x in range(len(cost))]
#Try (0, len(cost), arr)

trace = [1, 10, 19, 28, 31, 34, 46, 52, 58, 64]
way = [8]
visited = []
DFS (0, cost[0], 0, 60)
