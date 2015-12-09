f = open("day1.data")
d = f.read()

s = 0
for ix in range(len(d)):
  c = d[ix]
  if c == "(":
    s = s + 1
  elif c == ")":
    s = s - 1
  if s == -1:
    print (ix + 1)

print s
