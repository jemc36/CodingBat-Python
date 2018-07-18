"""
Given an array of ints, return the number of 9's in the array.
"""
def array_count9(nums):
  count9 = int()
  for i in nums:
    if i == 9:
      count9 = count9 + 1
    else: continue
  return count9
