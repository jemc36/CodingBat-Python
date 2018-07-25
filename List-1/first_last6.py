"""
Given an array of ints, return True if 6 appears as either the first or last element in the array.
The array will be length 1 or more.
"""
def first_last6(nums):
  if nums[0] == 6:
    return True
  if nums[-1] == 6:
    return True
  return False
