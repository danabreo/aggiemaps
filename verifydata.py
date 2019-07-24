import collections

# creates lists for stop names and stop coordinates, from coordinates.csv
coordslist = [row.rstrip().split(',')[0] for row in open("coordinates.csv",mode='r',encoding='utf-8-sig')]
latlnglist = [row.rstrip().split(',',1)[1].strip() for row in open("coordinates.csv",mode='r',encoding='utf-8-sig')]

# creates list of all unique stop names listed in routes.csv
routeslist = open("routes.csv",mode='r',encoding='utf-8-sig').read().splitlines()
routenames = []
for i in routeslist: # removes blanklines and route names
    if i.split(',')[1].isnumeric():
        routenames.append(i.split(',')[0])
routeslist = list(dict.fromkeys(routenames)) # removes duplicates from list

print("Found only in routes.csv:",(set(routeslist).difference(coordslist)))
print("Found only in coordinates.csv:",(set(coordslist).difference(routeslist)))
print("Duplicates in coordinates.csv:",[item for item, count in list(collections.Counter(latlnglist).items()) if count > 1])
