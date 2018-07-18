"""
Given a string, return a new string where the first and last chars have been exchanged.
"""
def front_back(x):
  if len(x) <= 1:
    return x
  mid = x[1:len(x)-1]
  return x[-1] + mid + x[0]
  
