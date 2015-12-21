wstring = '''Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0'''

astring = '''Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5'''

rstring = '''Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3'''

class Person(object):
  def __init__(self):
    self.health = 100
    self.attack = 0
    self.defense = 0
    self.cost = 0
    self.items = []

  def use_items(self, items):
    self.items = items
    for item in items:
      self.attack += item.attack
      self.defense += item.defense
      self.cost += item.cost

  def damage_for_defense(self, defense):
    return max(self.attack - defense, 1)

class Item(object):
  def __init__(self):
    self.name = ''
    self.cost = 0
    self.attack = 0
    self.defense = 0

  def __repr__(self):
    return "%s: -> %d\n\t(*) %d\n\t$ %d" % (self.name, self.attack, self.defense, self.cost)

enemy_item = Item()
enemy_item.attack = 8
enemy_item.defense = 2

def make_item(line):
  parts = line.split(' ')
  parts = filter(lambda x: x != '', parts)
  item = Item()
  item.name = parts[0]
  item.cost = int(parts[1])
  item.attack = int(parts[2])
  item.defense = int(parts[3])
  return item

def make_items(desc):
  items = []
  for line in desc.split('\n'):
    item = make_item(line)
    items.append(item)
  return items

weapons = make_items(wstring)
armors = make_items(astring)
rings = make_items(rstring)

from itertools import combinations
def item_generator(items, minimum, maximum):
  for c in range(minimum, maximum + 1):
    for i in combinations(items, c):
      yield i

def fight_with_items(hero, enemy):
  while hero.health > 0 and enemy.health > 0:
    enemy.health -= hero.damage_for_defense(enemy.defense)
    if enemy.health <= 0:
      return
    hero.health -= enemy.damage_for_defense(hero.defense)

def did_perform_better(new_hero, old_hero, enemy):
  if hero.health > 0:
    return False
  if old_hero == None:
    return True
  return new_hero.cost > old_hero.cost

min_hero = None
for ws in item_generator(weapons, 1, 1):
  for ar in item_generator(armors, 0, 1):
    for rr in item_generator(rings, 0, 2):
      items = ws + ar + rr
      hero = Person()
      enemy = Person()
      hero.use_items(items)
      enemy.use_items([enemy_item])
      fight_with_items(hero, enemy)
      if did_perform_better(hero, min_hero, enemy):
        min_hero = hero

# def item_generator(list, minimum, maximum):
#   for ixs in index_generator(len(list), minimum, maximum):
#     arr = []
#     for ix in ixs:
#       arr.append(list[ix])
#     yield arr
