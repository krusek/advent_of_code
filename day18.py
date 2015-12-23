f = open("day18.data")

lines = f.readlines()
lines = map(lambda line: line.strip(), lines)

always = [(0,0),(0,99),(99,0),(99,99)]
always = []

def is_on(lights, ix, iy):
  global always
  if (ix, iy) in always:
    return 1
  if ix < 0 or iy < 0:
    return 0
  if iy >= len(lights):
    return 0
  if ix >= len(lights[iy]):
    return 0
  if lights[ix][iy] == "#":
    return 1
  else:
    return 0

def on_neighbors(lights, ix, iy):
  c = 0
  for iix in range(ix - 1, ix + 2):
    for iiy in range(iy - 1, iy + 2):
      if iix == ix and iiy == iy:
        continue
      c += is_on(lights, iix, iiy)
  return c

def next_state(lights, ix, iy):
  ons = on_neighbors(lights, ix, iy)
  if is_on(lights, ix, iy):
    if ons == 2 or ons == 3:
      return "#"
    else:
      return "."
  else:
    if ons == 3:
      return "#"
    else:
      return "."

def next_lights(lights):
  arr = []
  for ix in range(len(lights)):
    s = ""
    for iy in range(len(lights[ix])):
      s = s + next_state(lights, ix, iy)
    arr.append(s)
  return arr

def total_on(lights):
  c = 0
  for ix in range(len(lights)):
    for iy in range(len(lights[ix])):
      c += is_on(lights, ix, iy)
  return c

lights = lines
for ix in range(100):
  lights = next_lights(lights)

print total_on(lights)
