"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another
of the values, it does not count towards the sum.
"""
def lone_sum(a, b, c):
  if a == b and b !=c:
    return c
  elif b == c and b !=a:
    return a
  elif c == a and c !=b:
    return b
  elif a == b and b == c:
    return 0
  else:
    return a+b+c
