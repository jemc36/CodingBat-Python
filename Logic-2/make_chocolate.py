"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and
big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars
before small bars. Return -1 if it can't be done.
"""
def make_chocolate(small, big, goal):
# Fail 1: not enough bricks
  if goal > (small + big*5):
    return -1
# Fail 2: not enough small bricks
  elif (goal % 5) > small:
    return -1
# Success 1: only use big bricks
  elif (small + big*5) >= goal and big*5 == goal:
    return 0
# Success 2: big bricks less than goal
  elif big*5 <= goal:
    return (goal - big*5)
# Success 3: big bricks more than goal
  elif big*5 > goal:
    return goal % 5
