"""
Given a string, return a string where for every char in the original, there are two chars.
"""

def double_char(x):
  all = str()
  for i in x:
    all = all + i + i
  return all
