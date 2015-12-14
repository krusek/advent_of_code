import re

#f = open('day11.data', 'r')
#lines = f.readlines()

double = re.compile(r'(.)\1.*(.)\2')
other = re.compile(r'i|o|l')

def check_doubles(line):
  if double.search(line):
    return True
  else:
    return False

def check_others(line):
  if other.search(line):
    return False
  else:
    return True

def add_letters(a, count):
  return chr(ord(a) + count)

def next_letter(c):
  if c == 'z':
    return ""
  return add_letters(c, 1)

def make_three(a):
  if a == 'y' or a == 'z':
    return ""
  b = next_letter(a)
  return a + b + next_letter(b) 

def replace_letter(w, c, i):
  if i < 0:
    i = i + len(w)
  return w[:i] + c + w[i + 1:]

def add_word(w):
  for i in range(1, len(w) + 1):
    l = w[-i]
    c = next_letter(l)
    if c == "":
      w = replace_letter(w, 'a', -i)
    else:
      w = replace_letter(w, c, -i)
      return w
  return w

sets = map(lambda i: make_three(add_letters('a', i)), range(26))
sets = filter(lambda s: len(s) > 2, sets)
sets = filter(lambda s: check_others(s), sets)

def check_seq(w):
  for s in sets:
    if s in w:
      return True
  return False  
  
def check_word(w):
  return check_doubles(w) and check_others(w) and check_seq(w)

lines = ['hijklmmn', 'abbceffg', 'abbcegjk']

for line in lines:
  print line, check_word(line)

def next_word(line):
  while not(check_word(line)):
    line = add_word(line)
  return line
