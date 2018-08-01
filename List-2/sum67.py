"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
"""
# based on online answer
# create a flag
def sum67(nums):
        state=0
        s=0
        for n in nums:
                if state == 0:
                        if n == 6:
                                state=1
                        else:
                                s+=n
                else:
                        if n == 7:
                                state=0 # else: s = s
        return s
