"""
Given a string and a non-negative int n,
return a larger string that is n copies of the original string.
"""
def string_times(x, n):
  allstr = str()
  for i in range(n):
    allstr = allstr + x
  return allstr
