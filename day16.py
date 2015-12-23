f = open('day16.data', 'r')
lines = f.readlines()

sue = {
  "children": lambda x: x == 3,
  "cats": lambda x: x > 7,
  "samoyeds": lambda x: x == 2,
  "pomeranians": lambda x: x < 3,
  "akitas": lambda x: x == 0,
  "vizslas": lambda x: x == 0,
  "goldfish": lambda x: x < 5,
  "trees": lambda x: x > 3,
  "cars": lambda x: x == 2,
  "perfumes": lambda x: x == 1
}

def read_line(line):
  l = line.strip()
  l = l[l.find(":")+1:]
  sue = {}
  parts = l.split(",")
  for part in parts:
    ps = part.strip().split(":")
    sue[ps[0]] = int(ps[1])
  return sue

sues = map(lambda line: read_line(line), lines)

def matches(s):
  global sue
  for key in s.iterkeys():
    if not sue.has_key(key):
      continue
    if not sue[key](s[key]):
      return False
  return True

for s in sues:
  if matches(s):
    print s, sues.index(s)
