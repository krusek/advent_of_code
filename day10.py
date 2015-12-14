i = "1113222113"

def process(s):
  l = ""
  count = 0
  r = ""
  for c in s:
    if c == l:
      count = count + 1
    elif count >= 0:
      if count > 0:
        r = r + "%d%s" % (count, l)
      count = 1
      l = c
  return r + "%d%s" % (count, l)

print process("1")
print process("11")
print process("21")
print process("1211")
print process("111221")

for ix in range(50):
  i = process(i)
print len(i)
