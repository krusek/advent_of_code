f = open('day24.data')
lines = f.readlines()
lines.reverse()
f.close()

sizes = map(lambda l: int(l.strip()), lines)

total = sum(sizes)
print total

compartments = 4
weight = total / compartments
mlen = float("inf")
arrangements = []

def get_arrangements(current, ix):
  global mlen
  if ix >= len(sizes):
    return
  if len(current) > mlen:
    return
  get_arrangements(current[:], ix + 1)
  current.append(sizes[ix])
  s = sum(current)
  if s == weight:
    arrangements.append(current)
    mlen = min(mlen, len(current))
    return
  elif s > weight:
    return
  get_arrangements(current, ix + 1)

get_arrangements([], 0)
ms = filter(lambda m: len(m) == mlen, arrangements)

def prod(l):
  return reduce(lambda x, y: x * y, l, 1)

ps = map(lambda l: prod(l), ms)
print min(ps)
