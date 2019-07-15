routes = [row.rstrip().split(',') for row in open("routes.csv",mode='r',encoding='utf-8-sig')]
stops = [row.split(',')[0] for row in open("coordinates.csv",mode='r',encoding='utf-8-sig')]

graph = {}
for line in stops:
    tempdict = {}
    curbus = int(routes[0][0].split()[0])
    graph[line] = {}
    for i in range(len(routes)-1):
        if not routes[i][1] and routes[i+1][1]:
            curbus = int(routes[i][0].split()[0])
        if line==routes[i][0] and routes[i+1][0]:
            if routes[i+1][0] in graph[line]:
                graph[line][routes[i+1][0]].append(curbus)
            else:
                tempdict[routes[i+1][0]]=[int(routes[i][1]),curbus]
                graph[line] = tempdict
walk = []
for line in open("walk.csv",mode='r',encoding='utf-8-sig'):
    walk.append(line.rstrip().split(','))

for line in walk:
    if line[0] not in graph[line[1]]:
        graph[line[1]][line[0]]=[int(line[2]),-1]
    else:
        graph[line[1]][line[0]].append(-1)
    if line[1] not in graph[line[0]]:
        graph[line[0]][line[1]]=[int(line[2]),-1]
    else:
        graph[line[0]][line[1]].append(-1)

print(graph)
