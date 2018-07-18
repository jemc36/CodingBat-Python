"""
Given a string, return a new string made of every other char starting with the first,
so "Hello" yields "Hlo".
"""
def string_bits(x):
  allstr = str()
  for i in range(len(x)):
    if i % 2 == 0:
      allstr = allstr + x[i]
    else:
      allstr = allstr
  return allstr
