# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  # modify and then return the variable below
  lowest = -1
  for row in rows:
    rowLen = len(row)
    for j in range(rowLen-numberMachines):
      try:
        lowest = sum(row[j:j+numberMachines])
      except TypeError:
        continue
  answer = lowest
  return answer

