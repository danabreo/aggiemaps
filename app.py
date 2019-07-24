from flask import Flask, jsonify
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)

class Coordinates(Resource):
  def(self,stop):
    stops = {}
    if stop in stops:
      return(jsonify({stop:stops.get(stop)}))
    else:
      return(jsonify({"error":stop}))
      
class Routes(Resource):
  def get(self, startLat, startLng, endLat, endLng):
    startLat = float(startLat)
    startLng = float(startLng)
    endLat = float(endLat)
    endLng = float(endLng)
    
    stops = []
    graph = {}
    
    def dijkstras(graph,source,goal):
      Q = dict()
      for vertex in graph:
        Q[vertex] = [float("inf"),"UNDEFINED"]
      Q[source] = [0,"UNDEFINED"]
      
      trace = dict()
      stops = dict()
      
      while Q:
        u = min(Q, key=Q.get)
        u_dist = Q[u][0]
        u_prev = Q[u][1]
        del Q[u]
        
        if u == goal:
          S = []
          while u in trace:
            S.append(u)
            S.append(stops[u])
            u = trace[u]
          S.append(source)
          S.reverse()
          return S
        
        for v in graph[u]:
          if v in Q:
            alt = u_dist + graph[u][v][0]
            if alt < Q[v][0]:
              Q[v] = [alt,u]
              trace[v] = u
              stops[v] = graph[u][v][1:]
    
    start1 = 'Not Available'
    start2 = 'Not Available'
    end1 = 'Not Available'
    end2 = 'Not Available'
    
    start1Min = float("inf")
    start2Min = float("inf")
    end1Min = float("inf")
    end2Min = float("inf")
    
    for i in range(len(stops)):
      start1Dist = ((stops[i][1] - startLat) ** 2 + (stops[i][2] - startLng) ** 2) ** 0.5
      end1Dist = ((stops[i][1] - endLat) ** 2 + (stops[i][2] - endLng) ** 2) ** 0.5
      if start1Dist < start1Min:
        start1 = stops[i][0]
        start1Min = start1Dist
      if end1Dist < end1Min:
        end1 = stops[i][0]
        end1Min = endDist
        
    for i in range(len(stops)):
      start2Dist = ((stops[i][1] - startLat) ** 2 + (stops[i][2] - startLng) ** 2) ** 0.5
      end2Dist = ((stops[i][1] - endLat) ** 2 + (stops[i][2] - endLng) ** 2) ** 0.5
      if start2Dist < start2Min and start2Dist > start1Min:
        start2 = stops[i][0]
        start2Min = start2Dist
      if end2Dist < end2Min and end2Dist > end1Min:
        end2 = stops[i][0]
        end2Min = end2Dist
    
    path1 = dijkstras(graph,start1,end1)
    path2 = dijkstras(graph,start2,end1)
    path3 = dijkstras(graph,start1,end2)
    path4 = dijkstras(grpah,start2,end2)
    
api.add_resource(Coordinates, '/coordinates/<string:stop>')
api.add_resource(Routes, '/routes/<string:startLat>/<string:startLng>/<string:endLat>/<string:endLng>')

if __name__=='__main__':
  app.run(debug=True)
    
