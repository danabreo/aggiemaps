# creates lists of stops in route order
routes=[row.rstrip().split(',') for row in open("routes.csv",mode='r',encoding='utf-8-sig')]

# creates list of all stops
stops=[row.split(',')[0] for row in open("coordinates.csv",mode='r',encoding='utf-8-sig')]

# creates list all walking connections
walk=[row.rstrip().split(',') for row in open("walk.csv",mode='r',encoding='utf-8-sig')]

# creates list of all stop coordinates
print([[row.rstrip().split(',')[0],float(row.rstrip().split(',')[1]),float(row.rstrip().split(',')[2])] for row in open("coordinates.csv",mode='r',encoding='utf-8-sig')])

graph={}
for line in stops:
    currentbus=0
    graph[line]={}
    for i in range(len(routes)-1):
        if not routes[i][1] and routes[i+1][1]: # checks and stores bus number of current route
            currentbus=int(routes[i][0].split()[0])
        if line==routes[i][0] and routes[i+1][0]:
            if routes[i+1][0] in graph[line]: # adds time and bus number to graph
                graph[line][routes[i+1][0]].append(currentbus)
            else: # adds only bus number to existing time and bus number
                graph[line][routes[i+1][0]]=[int(routes[i][1]),currentbus]

# adds walking connections between bus stops
for line in walk:
    if line[0] in graph[line[1]]:
        graph[line[1]][line[0]].append(-1)
    else:
        graph[line[1]][line[0]] = [int(line[2]), -1]
    if line[1] in graph[line[0]]:
        graph[line[0]][line[1]].append(-1)
    else:
        graph[line[0]][line[1]] = [int(line[2]), -1]

print(graph)
