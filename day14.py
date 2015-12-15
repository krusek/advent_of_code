
with open('day14.data', 'r') as f:
  lines = f.readlines()

d = {}

def read_line(line):
  parts = line.strip().split(' ')
  d[parts[0]] = [(int(parts[3]), int(parts[6])), (0, int(parts[-2]))]

def one_distance(speed, distance, time):
  if time <= 0:
    return (distance, 0)
  if time <= speed[1]:
    return (distance + speed[0]*time, 0)
  return (distance + speed[0]*speed[1], time - speed[1])

def distance(data, time):
  (d, t) = one_distance(data[0], 0, time)
  ix = 1
  while t > 0:
    (d, t) = one_distance(data[ix % len(data)], d, t)
    ix = ix + 1
  return (d, t)

for line in lines:
  read_line(line)

points = {}
for k in d.keys():
  points[k] = 0

for ix in range(1, 2504):
  dist = {}
  for k in d.keys():
    data = d[k]
    dist[k] = distance(data, ix)
  v = max(dist.values())
  for k in dist.keys():
    if dist[k] == v:
      points[k] = points[k] + 1

print points

for k in d.keys():
  data = d[k]
  print k, distance(data, 2503)


