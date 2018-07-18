"""
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both are negative.
"""
def pos_neg(a, b, negative):
  if a > 0 and b < 0:
    if negative == False:
      return True
    if negative == True:
      return False
  if a < 0 and b > 0:
    if negative == True:
      return False
    if negative == False:
      return True
  if a < 0 and b < 0 and negative == True:
    return True
  else:
    return False
