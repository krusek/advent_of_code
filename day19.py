rstring = '''Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg'''

# rstring = '''H => HO
# H => OH
# O => HH'''

med = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'

# med = 'HOH'
replacements = []
def get_replacement(line):
  global replacements
  parts = line.split("=>")
  parts = map(lambda p: p.strip(), parts)
  replacements.append(parts)

def get_indexes(line, part):
  ix = 0
  found = True
  while ix >= 0:
    ix = line.find(part, ix)
    if ix >= 0:
      yield ix
      ix += 1

found = {}
def found_instance(med):
  if not found.has_key(med):
    found[med] = 0
  found[med] += 1

def all_substitutions(s):
  global replacements
  for r in replacements:
    for ix in get_indexes(s, r[0]):
      yield s[0:ix] + r[1] + s[ix + len(r[0]):]

lines = rstring.split('\n')
for line in lines:
  get_replacement(line)

for s in all_substitutions(med):
  found_instance(s)
print len(found)
m = float("inf")
def find_length(s, d):
  global m, med
  if s == med:
    return d
  if d >= m:
    return -1
  for ss in all_substitutions(s):
    e = find_length(ss, d + 1)
    if e >= 0:
      m = min(e, m)
      return e
  return -1


replacements = map(lambda parts: [parts[1], parts[0]], replacements)

start = med
med = "e"
print find_length(start, 0)
