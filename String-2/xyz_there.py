"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded
by a period (.). So "xxyz" counts but "x.xyz" does not.
"""
def xyz_there(x):
  if x.count('xyz') == 0:
    return False
  elif x.count('.xyz') != 0:
    y = x.replace('.xyz','')
    if y.count('xyz') > 0:
      return True
    return False
  else:
    return True
  
