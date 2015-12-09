import hashlib
m = hashlib.md5()

q = 'iwrupvqb'

ix = -1
d = '12345'
while d[:6] != "000000":
  ix = ix + 1
  c = "%s%d" % (q, ix)
  m = hashlib.md5()
  m.update(c)
  d = m.hexdigest()

print ix
