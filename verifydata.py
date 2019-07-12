import collections

# creates lists for stop names and stop coordinates, from coordinates.csv
coords = open("coordinates.csv",mode='r',encoding='utf-8-sig')
coordslist = [row.split(',')[0] for row in coords]
coords.seek(0)
latlnglist = [row.split(',',1)[1].strip() for row in coords]
coords.close()

# creates list of all unique stop names listed in routes.csv
routes = open("routes.csv",mode='r',encoding='utf-8-sig')
fullrouteslist = routes.read().splitlines()
routenames = []
for i in fullrouteslist: # removes blanklines and route names
    if i.split(',')[1].isnumeric():
        routenames.append(i.split(',')[0])
routeslist = list(dict.fromkeys(routenames)) # removes duplicates from list
routes.close()

print("Found only in routes.csv:",(set(routeslist).difference(coordslist)))
print("Found only in coordinates.csv:",(set(coordslist).difference(routeslist)))
print("Duplicates in coordinates.csv:",[item for item, count in list(collections.Counter(latlnglist).items()) if count > 1])
