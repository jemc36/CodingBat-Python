"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""

def string_splosion(x):
  all = str()
  for i in range(len(x)):
    all = all + x[0:i+1]
  return all
