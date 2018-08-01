"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each)
and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the
given bricks. This is a little harder than it looks and can be done without any loops.
"""
def make_bricks(small, big, goal):
# 1. not enough bricks
  if goal > (small + big*5):
    return False
# 2. not enough small bricks
  if (goal % 5) > small:
    return False
  else:
    return True
