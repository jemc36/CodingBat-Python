"""
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
The string length will be at least 2.
"""
def left2(x):
  fst2 = x[0:2]
  rest = x[2:]
  if len(x) < 3:
    return x
  else:
    return rest+fst2
