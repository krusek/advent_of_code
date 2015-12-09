f = open("day8.data")
lines = f.readlines()
lines = map(lambda l: l.strip(), lines)
#lines = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']

dlen = 0
l = 0

for line in lines:
  ll = len(line)
  e = "len('%s')" % line[1:-1]
  d = eval(e)
  l = l + ll
  dlen = dlen + d

print l - dlen

d = {
  '"' : '\\"',
  '\\' : '\\\\',
}
p = "\"|\\\\"
print p
pattern = re.compile(p)
l = 0
e = 0
for line in lines:
  line2 = pattern.sub(lambda x: d[x.group()], line)
  print line, line2, len(line), len(line2) + 2
  l = l + len(line)
  e = e + len(line2) + 2

print e - l

