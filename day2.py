

f = open("day2.data")
lines = f.readlines()
print len(lines)
c = 0
e = 0
for line in lines:
  line = line.strip()
  if line == "":
    continue
  d = line.split('x')
  d = map(lambda x: int(x), d)
  d = sorted(d)
  c = c + 3*d[0]*d[1] + 2*d[0]*d[2] + 2*d[1]*d[2]
  e = e + d[0]*d[1]*d[2] + 2*(d[0] + d[1])

print c
print e

