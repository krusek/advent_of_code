f = open('day23.data')
lines = f.readlines()

var = {"a" : 1, "b" : 0}

simple = {
  "hlf " : lambda r: var[r] / 2,
  "tpl " : lambda r: 3 * var[r],
  "inc " : lambda r: var[r] + 1,
}

comp = {
  "jie " : lambda r: var[r] % 2 == 0,
  "jio " : lambda r: var[r] == 1
}

def read_offset(offset):
  if offset[0] == "+":
    return int(offset[1:])
  else:
    return int(offset)

ix = 0
while ix < len(lines):
  line = lines[ix].strip()
  command = line[0:4]
  extra = line[4:]
  old_ix = ix
  if simple.has_key(command):
    var[extra] = simple[command](extra)
    ix += 1
  elif comp.has_key(command):
    parts = extra.split(',')
    r = parts[0].strip()
    offset = read_offset(parts[1].strip())
    if not comp[command](r):
      offset = 1
    ix += offset
  else:
    offset = read_offset(extra.strip())
    ix += offset
  print old_ix, var, line
