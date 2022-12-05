import re

class Assignment:
  def __init__(self, min: int, max: int):
    self.min = min
    self.max = max

class Pair:
  def __init__(self, sections: list):
    self.a1 = Assignment(sections[0], sections[1])
    self.a2 = Assignment(sections[2], sections[3])

def create_pairs(sections: list) -> list:
  pairs = []
  for section in sections:
    pair = Pair(section)
    pairs.append(pair)
  return pairs

def parse_input(input: str) -> list:
  sections = []
  with open(input) as file:
    for line in file:
      line = line.replace("\n", "")
      splitted_text = re.split(r',|-', line)
      splitted_numbers = [eval(i) for i in splitted_text]
      sections.append(splitted_numbers)
  return sections

def get_contained_pairs(pairs: list) -> int:
  contained_pairs = 0
  for pair in pairs:
    if pair_is_contained(pair):
      contained_pairs += 1
  return contained_pairs

def get_overlapping_pairs(pairs: list) -> int:
  overlapping_pairs = 0
  for pair in pairs:
    if pair_is_overlapping(pair):
      overlapping_pairs += 1
  return overlapping_pairs

def pair_is_overlapping(pair: Pair) -> bool:
  if pair.a1.max < pair.a2.min: #  a1.min < a1.max < a2.min < a2.max
    return False
  if pair.a2.max < pair.a1.min: #  a2.min < a2.max < a1.min < a1.max
    return False
  return True

def pair_is_contained(pair: Pair) -> bool:
  if pair.a1.min >= pair.a2.min and pair.a1.max <= pair.a2.max: #  a2.min < a1.min < a1.max < a2.max
    return True
  if pair.a2.min >= pair.a1.min and pair.a2.max <= pair.a1.max: #  a1.min < a2.min < a2.max < a1.max
    return True
  return False  

sections = parse_input("input.txt")
pairs = create_pairs(sections)
contained_pairs = get_contained_pairs(pairs)
overlapping_pairs = get_overlapping_pairs(pairs)
print("Contained pairs:", contained_pairs)
print("Overlapping pairs:", overlapping_pairs)

