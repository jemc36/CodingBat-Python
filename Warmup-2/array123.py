"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
"""
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i:i+3]== [1,2,3]:
      return True
    else:continue
  return False
