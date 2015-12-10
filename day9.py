f = open('day9.data', 'r')
lines = f.readlines()

smallest = lambda l, r: l > r
biggest = lambda l, r: l > r
comp = smallest

connections = {}
for line in lines:
  parts = line.strip().split(" ")
  n1 = parts[0]
  n2 = parts[2]
  v = int(parts[-1])
  if connections.has_key(n1) == False:
    connections[n1] = {}
  if connections.has_key(n2) == False:
    connections[n2] = {}
  connections[n1][n2] = v
  connections[n2][n1] = v

def get_length(route, connections, names):
  last = route[-1]
  mlen = 0
  mrt = route
  for name in names:
    if connections[last].has_key(name) == False:
      continue
    n = names[:]
    r = route[:]
    r.append(name)
    n.remove(name)
    dd = connections[last][name]
    (d, rr) = get_length(r, connections, n) 
    d = d + dd
    if mlen == 0 or comp(mlen, d):
      mlen = d
      mrt = rr
  return (mlen, mrt)
    
names = connections.keys()

ex = 0
for name in names:
  n = names[:]
  n.remove(name)
  (d, r) = get_length([name], connections, n)
  if ex == 0 or comp(ex, d):
    ex = d

print ex
