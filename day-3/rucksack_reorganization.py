# Order-value of chars:
# a = 97    z = 122
# A = 65    Z = 90


class Compartment:
  def __init__(self, items: str):
    self.items = items
    self.item_values = self.get_item_value_list()
  
  def get_item_value_list(self) -> list:
    item_value_list = []

    for char in self.items:
      #All characters have an order number in ascii, with a-z [97, 122] and A-Z [65, 90]
      #Thus we can modify them to values 1-52 my substracting the appropriate offset
      if char.isupper():
        offset = 64 - 26
      else:
        offset = 96      
      value = ord(char) - offset
      item_value_list.append(value)
    return item_value_list

  def debug_list(self) -> str:
    i = 0
    string = ""
    while i < len(self.items):
      string += f"{self.items[i]}:{self.item_values[i]}, "
      i += 1
    return string


class Rucksack:
  def __init__(self, item_list: str):
    self.item_list = item_list
    self.create_compartments(self.item_list)
    self.item_values = self.comp1.item_values + self.comp2.item_values

  def create_compartments(self, item_list: str):
    halfway = len(item_list)//2
    end = len(item_list)
    self.comp1 = Compartment(item_list[0:halfway])
    self.comp2 = Compartment(item_list[halfway:end])



def create_rucksacks(input: str) -> list:
  rucksacks = []
  with open(input) as file:
    for line in file:
      line = line.replace("\n", "") #Remove linebreaks
      r = Rucksack(line)
      rucksacks.append(r)
  return rucksacks

def get_common_value(rucksack: Rucksack) -> int:
  comp1 = rucksack.comp1.item_values
  comp2 = rucksack.comp2.item_values
  if comp1 == [] or comp2 == []:
    return -2

  for value in comp1:
    if value in comp2:
      return value

  return -1 #Each rucksack should have one common value
  
def get_sum_of_common_values(rucksacks: list) -> int:
  sum = 0
  for rucksack in rucksacks:
    value = get_common_value(rucksack)
    sum += value
  return sum


def get_badge_value(rucksack1: Rucksack, rucksack2: Rucksack, rucksack3: Rucksack) -> int:

  items = rucksack1.item_values

  for item in items:
    if(item in rucksack2.item_values and item in rucksack3.item_values):
      return item

def get_sum_of_badge_values(rucksacks: list) -> int:
  sum = 0
  i = 0
  while i < len(rucksacks):
    sum += get_badge_value(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2])
    i += 3  
  return sum


rucksacks = create_rucksacks("input.txt")

badge_sum = get_sum_of_badge_values(rucksacks)



print(f"Badges value: {badge_sum}")


