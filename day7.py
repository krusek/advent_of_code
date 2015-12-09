# <value> AND|OR|LSHIFT|RSHIFT <value> -> <variable>
# <value> = <number>|<variable>
# NOT <value> -> <variable>
# <value> -> <variable>

wires = {}

operations = {
  "AND" : lambda l, r: l & r,
  "OR" : lambda l, r: l | r,
  "LSHIFT" : lambda l, r: l << r,
  "RSHIFT" : lambda l, r: l >> r,
  "NOT" : lambda l: (~l) & 65535
}

def evaluate_value(value):
  if wires.has_key(value):
    return wires[value]
  return int(value)

def binary_operation(parts):
  left = evaluate_value(parts[0])
  right = evaluate_value(parts[2])
  return operations[parts[1]](left, right)

def unary_operation(parts):
  v = evaluate_value(parts[1])
  return operations[parts[0]](v)

def assign(value, variable):
  wires[variable] = value

def can_evaluate(value):
  return wires.has_key(value) or value.isdigit()

def is_line_ready(parts):
  if parts[1] == "->":
    return can_evaluate(parts[0])
  if parts[2] == "->":
    return can_evaluate(parts[1])
  if parts[3] == "->":
    return can_evaluate(parts[0]) and can_evaluate(parts[2])

def evaluate_line(parts):
  value = 0
  variable = parts[-1].strip()
  if parts[1] == "->":
    value = evaluate_value(parts[0])
  elif parts[2] == "->":
    value = unary_operation(parts)
  elif parts[3] == "->":
    value = binary_operation(parts)
  assign(value, variable)


f = open("day7.data", "r")
lines = f.readlines()
all_parts = map(lambda line: line.split(" "), lines)

def evaluate_all_parts(parts):
  all_parts = parts[:]
  new_count = len(all_parts)
  count = new_count + 1
  while count != new_count and len(all_parts) > 0:
    count = len(all_parts)
    remove = filter(lambda parts: is_line_ready(parts), all_parts)
    map(lambda r: evaluate_line(r), remove)
    map(lambda r: all_parts.remove(r), remove)
    new_count = len(all_parts)

evaluate_all_parts(all_parts)
print wires["a"]

v = wires["a"]
wires = {}

remove = filter(lambda parts: parts[-1] == "b\n", all_parts)
new_parts = filter(lambda parts: not(parts in remove), all_parts)
s = "%d -> b" % v
new_parts.append(s.split(" "))

evaluate_all_parts(new_parts)

print wires["a"]
