"""
Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.
"""
def count_code(x):
  count = 0
  for i in range(len(x)-3):
    if x[i:i+2] == 'co' and x[i+3:i+4] == 'e':
      count = count + 1
    else:
      count = count
  return count
