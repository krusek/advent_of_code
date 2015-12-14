import json

with open('day12.data', 'r') as f:
  d = json.loads(f.read())

def get_value(e):
  c = 0
  if isinstance(e, dict):
    if "red" in e.values():
      return 0
    for key in e.keys():
      c = c + get_value(e[key])
  elif isinstance(e, list):
    for k in e:
      c = c + get_value(k)
  elif isinstance(e, int):
    c = e
  return c


