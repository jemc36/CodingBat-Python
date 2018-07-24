"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""
def cat_dog(x):
  cat = 0
  dog = 0
  for i in range(len(x)-2):
    if x[i:i+3] == 'cat':
      cat = cat + 1
    if x[i:i+3] == 'dog':
      dog = dog + 1
  if dog == cat:
    return True
  else:
    return False
