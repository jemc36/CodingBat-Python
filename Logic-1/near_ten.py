"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
"""
def near_ten(num):
  if num % 10 <= 2:
    return True
  elif (10 - num % 10) <=2:
    return True
  return False
