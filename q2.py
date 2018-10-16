# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  # modify and then return the variable below
  from random import randint   
  lowest = 1000
  minSize = len(cashFlowIn) if len(cashFlowIn) < len(cashFlowOut) else len(cashFlowOut)
  randomSetSize = randint(1,minSize) % 100
  while lowest > 5:    
    subIn = [cashFlowIn[randint(0,len(cashFlowIn)-1)] for i in range(randomSetSize)]
    subOut = [cashFlowOut[randint(0,len(cashFlowOut)-1)] for i in range(randomSetSize)]
    eval = abs(sum(subIn)-sum(subOut))
    if eval < lowest:
      lowest = eval
  answer = lowest
  return answer

