f = open('day3.data', 'r')

def move(position, c):
  if c == '^':
    return (position[0], position[1] + 1)
  elif c == 'v':
    return (position[0], position[1] - 1)
  elif c == '<':
    return (position[0] - 1, position[1])
  elif c == '>':
    return (position[0] + 1, position[1])
  else:
    return position


data = f.read()

points = {}
pts2 = {}
position = (0, 0)
santa = (0, 0)
robot = (0, 0)
points[position] = 1
pts2[position] = 1
print len(data)
other = 0
for ix in range(len(data)):
  c = data[ix]
  position = move(position, c)
  if (ix % 2) == 0:
    santa = move(santa, c)
  else:
    robot = move(robot, c)
  pts2[santa] = 1
  pts2[robot] = 1
  points[position] = 1
print len(points)
print len(pts2)
print other
