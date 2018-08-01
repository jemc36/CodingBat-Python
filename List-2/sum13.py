"""
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come immediately
after a 13 also do not count.
"""
def sum13(nums):
  a = [i for i,x in enumerate(nums) if x == 13]
  b = [x+1 for x in a]
  adjb = list()
  allpos = list()
  for i in b:
    if i < (len(nums)-1) or i == (len(nums)-1):
      adjb = adjb + [i]
  allpos = a + adjb
  all = 0
  for i in range(len(nums)):
    if i in allpos: continue
    all = all + nums[i]
  return all
