f = open("day5.data", 'r')

lines = f.readlines()

def has_vowels(line):
  count = 0
  vowels = 'aeiou'
  for v in vowels:
    count = count + line.count(v)
    if count >= 3:
      return True
  return False

def has_double(line):
  c = 'qwer'
  for l in line:
    if l == c:
      return True
    c = l
  return False

def has_wrong(line):
  return line.count('ab') + line.count('cd') + line.count('pq') + line.count('xy')

def has_two(line):
  for ix in range(len(line) - 1):
    s = line[ix:ix+2]
    if line[ix+2:].find(s) >= 0:
      return True
  return False

def has_other_two(line):
  for ix in range(len(line) - 2):
    if line[ix] == line[ix + 2]:
      return True
  return False

count = 0
c = 0
for line in lines:
  if has_vowels(line) and has_double(line) and not(has_wrong(line)):
    count = count + 1
  if has_two(line) and has_other_two(line):
    c = c + 1


print has_two("uurcxstgmygtbstg")
print count
print c
