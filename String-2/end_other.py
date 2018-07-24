"""
Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.
"""
def end_other(a, b):
  alow = a.lower()
  blow = b.lower()
  if len(a) > len(b) and blow == alow[-(len(b)):]:
    return True
  if len(b) > len(a) and alow == blow[-(len(a)):]:
    return True
  if alow == blow:
    return True
  else:
    return False
