cstring = '''43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38'''

target = 150

containers = map(lambda s: int(s), cstring.split('\n'))

goods = {}

def ensure_key(n):
  if not goods.has_key(n):
    goods[n] = 0

def number_of_good_sets(include, ix, options):
  s = sum(include)
  if s == 150:
    i = len(include)
    ensure_key(i)
    goods[i] += 1
    return 1
  if s > 150:
    return 0

  if ix >= len(options):
    return 0

  v = number_of_good_sets(include, ix + 1, options)
  item = options[ix]
  i = include[:]
  i.append(item)
  v = v + number_of_good_sets(i, ix + 1, options)
  return v

n = number_of_good_sets([], 0, containers)
