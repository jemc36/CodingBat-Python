"""
Return the number of times that the string "hi" appears anywhere in the given string.
"""
def count_hi(x):
  count = 0
  for i in range(len(x)-1):
    if x[i:i+2] == 'hi':
      count = count + 1
    else:
      count = count
  return count
