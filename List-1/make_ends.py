"""
Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
The original array will be length 1 or more.
"""
def make_ends(nums):
  if len(nums) == 1:
    return [nums[0], nums[0]]
  if len(nums) > 1:
    return [nums[0],nums[-1]]
  
