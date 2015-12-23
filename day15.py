'''Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8'''

values = [[2, 0, 0, 0], [0, 5, 0, -1], [-2, -3, 5, 0], [0, 0, -1, 5]]

arange = [1, 97]
brange = lambda a: [1, 98 - a]
crange = lambda a, b: [(2 * a + 3 * b) / 5, 99 - a - b]
drange = lambda a, b, c: [max(1, c / 5 + 1), 5 * b]

def get_value(a, b, c, d):
  p = 1
  for row in values:
    p = p * (row[0] * a + row[1] * b + row[2] * c + row[3] * d)
  return p

def calories(a, b, c, d):
  return (a * 3 + b * 3 + c * 8 + d * 8)

def bad_calories(a, b, c, d):
  # return False
  return calories(a, b, c, d) > 500

m = 0
for a in range(arange[0], arange[1] + 1):
  bs = brange(a)
  for b in range(bs[0], bs[1] + 1):
    cs = crange(a, b)
    for c in range(cs[0], cs[1] + 1):
      ds = drange(a, b, c)
      d = 100 - a - b - c
      if d < ds[0] or d > ds[1] or bad_calories(a, b, c, d):
        continue
      m = max(get_value(a, b, c, d), m)
