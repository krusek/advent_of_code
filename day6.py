f = open("day6.data", "r")

lines = f.readlines()

lts = {}
for ix in range(1000):
  for iy in range(1000):
    lts[(ix, iy)] = 0

lts2 = {}
for ix in range(1000):
  for iy in range(1000):
    lts2[(ix, iy)] = 0

def turn_on(p):
  lts[p] = True
  lts2[p] = lts2[p] + 1

def turn_off(p):
  lts[p] = False
  lts2[p] = max(lts2[p] - 1, 0)

def toggle(p):
  lts[p] = not(lts[p])
  lts2[p] = lts2[p] + 2

operations = {
  "turn on ":  turn_on,
  "turn off ": turn_off,
  "toggle ": toggle }

def get_operation(line):
  for key in operations.keys():
    if line.startswith(key):
      return (line.replace(key, ""), operations[key])

def get_point(pt):
  p = pt.split(",")
  return (int(p[0]), int(p[1]))

def get_points(line):
  pts = line.split(" ")
  pts = [pts[0], pts[2]]
  return (get_point(pts[0]), get_point(pts[1]))
       

for line in lines:
  line, operation = get_operation(line)   
  pts = get_points(line)
  for ix in range(pts[0][0], pts[1][0]+1):
    for iy in range(pts[0][1], pts[1][1]+1):
      operation((ix, iy))


f = filter(lambda y: y, lts.values())
print len(f)  
print sum(lts2.values())
