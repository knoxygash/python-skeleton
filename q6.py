# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  shortestPath = 1000000
  routes = paths(numServers,targetServer)
  for route in routes:
    short = 0
    for i in range(len(route)-1):
      short += times[int(route[i])][int(route[i+1])]
    if short < shortestPath:
      shortestPath = short 
  answer = shortestPath
  return answer

def paths(numServers,targetServer):
  remServers = range(numServers)    
  ss = '0'
  ts = str(targetServer)
  routes = [ss+ts]
  remServers.remove(0)
  remServers.remove(targetServer)
  while remServers != []:
    for i in range(len(remServers)):
      routes.append(ss + str(remServers[i]) + ts)
    ss += str(remServers[0])
    remServers.remove(remServers[0])
  return routes
