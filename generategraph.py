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
    if line[0] not in graph[line[1]]:
        graph[line[1]][line[0]] = [int(line[2]), -1]
    if line[1] not in graph[line[0]]:
        graph[line[0]][line[1]] = [int(line[2]), -1]

# adds connections within each bus route
i = 0
while i < (len(routes)-1):
    if not routes[i][1] and routes[i+1][1]:
        stopList = []
        curBus = int(routes[i][0].split()[0])
        while routes[i+1][1]:
            stopList.append((routes[i+1][0],routes[i+1][1]))
            i += 1
        toAdd = {}
        j = 0
        while j < len(stopList):
            k = (j+1)%len(stopList)
            curTotal = int(stopList[j][1])-1
            toAdd[stopList[j][0]] = {}
            while stopList[j] != stopList[k]:
                toAdd[stopList[j][0]][stopList[k][0]] = [curTotal,curBus]
                if curTotal > 1:
                    curTotal += int(stopList[k][1])-1 # favors staying on the same bus
                else:
                    curTotal += int(stopList[k][1])
                k  = (k+1)%len(connections)
            j += 1
        for stop in toAdd:
            for connection in toAdd[stop]:
                if connection not in graph[stop]:
                    graph[stop][connection] = toAdd[stop][connection]
    else:
        i += 1
  
print(graph)
