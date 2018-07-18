"""
Given a string, return the count of the number of times
that a substring length 2 appears in the string and
also as the last 2 chars of the string, so "hixxxhi" yields 1
(we won't count the end substring).
"""
def last2(x):
  last2 = x[-2:]
  count = int()
  for i in range(len(x)-2):
    if x[i:i+2] == last2:
      count = count + 1
    else: continue
  return count
