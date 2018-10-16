# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  highestEval = 0
  sizeOfports = len(portfolios)
  for i in range(sizeOfports):
    for j in range(i+1,sizeOfports):
      eval = int(bin(portfolios[i] ^ portfolios[j]),2)
      if eval > highestEval:
        highestEval = eval    
  answer = highestEval
  return answer