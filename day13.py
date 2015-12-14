
with open('day13.data', 'r') as f:
  lines = f.readlines()


def get_value(line):
  parts = line.strip().strip('.').split(" ")
  n = parts[0]
  m = parts[-1]
  v = int(parts[3])
  if parts[2] == "lose":
    v = -v
  return [n, m, v]

dist = {'y':{}}

def add_value(n, m, v):
  if dist.has_key(n) == False:
    dist[n] = {'y':0}
    dist['y'][n] = 0
  d = dist[n]
  if d.has_key(m) == False:
    d[m] = 0
  d[m] = d[m] + v

def read_line(line):
  n, m, v = get_value(line)
  add_value(n, m, v)
  add_value(m, n, v)

for line in lines:
  read_line(line)




smallest = lambda l, r: l > r
biggest = lambda l, r: l < r
comp = biggest

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

connections = dist
names = connections.keys()

ex = 0
for name in names:
  n = names[:]
  n.remove(name)
  (d, r) = get_length([name], connections, n)
  d = d + connections[r[0]][r[-1]]
  if ex == 0 or comp(ex, d):
    ex = d
    print ex, r

print ex
