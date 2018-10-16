# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):
  # modify and then return the variable below
  from sets import Set  
  nodeElememts = Set([i[0] for i in edgeList])
  edgeElements = Set([i[1] for i in edgeList])
  
  if nodeElememts.intersection(edgeElements)==Set([]):
    answer = len(edgeElements)-len(nodeElememts)
  else:
    answer = len(edgeList)-len(nodeElememts.intersection(edgeElements))
  return answer
