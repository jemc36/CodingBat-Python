"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.
"""
def array_front9(nums):
  num4 = list()
  if len(nums) < 4:
    for i in nums:
      if i !=9:continue
      return True
  else:
    num4 = nums[0:4]
    for j in num4:
      if j !=9: continue
      return True
  return False
