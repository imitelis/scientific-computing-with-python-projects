import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **kwargs):
    self.contents = []
    for c,n in kwargs.items():
      for i in range(0, n):
        self.contents.append(c)

    self.initial_contents = copy.copy(self.contents)

  def reset(self):
    self.contents = copy.copy(self.initial_contents)

  def draw(self, count):
    try:
      drawed = random.sample(self.contents, count)
    except ValueError:
      drawed = copy.copy(self.contents)

    for i in drawed:
      self.contents.remove(i)

    if 0 == len(self.contents):
      self.contents = copy.copy(self.initial_contents)

    return drawed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expect_count = 0
  
  for k in range(num_experiments):
    expected_balls_count = copy.copy(expected_balls)
    hat.reset()
    returned_balls_count = hat.draw(num_balls_drawn)
    for balls_color, balls_count in expected_balls.items():
      for h in range(0, balls_count):
        if balls_color in returned_balls_count:
          returned_balls_count.remove(balls_color)
          expected_balls_count[balls_color] -= 1

    if sum(n for n in expected_balls_count.values() ) == 0:
      expect_count += 1

  approx_prob = expect_count / num_experiments

  return approx_prob