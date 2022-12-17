class Monkey:

  def __init__(self, items, operation, test_number, true_monkey, false_monkey):
    self.items = items
    self.operation = operation
    self.test_number = test_number
    self.true_monkey = true_monkey
    self.false_monkey = false_monkey

    self.inspections = 0

  def inspect_and_throw_items(self, monkeys: list, part_one: bool, common_modulo: int):
    while len(self.items) > 0:
      self.inspections += 1
      item = self.items.pop(0)
      worry_level = self.operation.do_operation(item)
      if(part_one):
        worry_level = worry_level // 3
      else:
        worry_level = worry_level % common_modulo

      if worry_level % self.test_number == 0:
        monkeys[self.true_monkey].items.append(worry_level)
      else:
        monkeys[self.false_monkey].items.append(worry_level)

      

class Operation:

  def __init__(self, add, multiply, fixed_value):
    self.add = add
    self.multiply = multiply
    self.fixed_value = fixed_value

  def do_operation(self, item_value):
    #The value added/multiplied is a fixed value, eg. 15 / 9 / 2
    if self.fixed_value != None:
      if self.add:
        return item_value + self.fixed_value
      elif self.multiply:
        return item_value * self.fixed_value
      
    #The value added/multiplied is the value inputted
    elif self.fixed_value == None:
      if self.add:
        return item_value + item_value
      elif self.multiply:
        return item_value * item_value

def parse_input(input: str) -> list:
  file = list(open(input))
  number_of_monkeys = (len(file) + 1) // 7
  parsed_monkeys = []
  for i in range(number_of_monkeys):
    parsed_monkeys.append([])

  for i in range(len(file)):
    if i % 7 == 6 or 1 % 7 == 0:
      continue

    line = file[i]
    line = line.replace("\n", "")
    monkey_index = i // 7
    current_monkey = parsed_monkeys[monkey_index]

    if i % 7 == 1:
      line = line.replace("  Starting items: ", "")
      splitted_line = line.split(", ")
      items = []
      for j in range(len(splitted_line)):
        items.append(int(splitted_line[j]))
      current_monkey.append(items)
    
    if i % 7 == 2:
      line = line.replace("  Operation: new = old ", "")
      line = line.replace(" ", "")
      operation_text = line
      current_monkey.append(operation_text)

    if i % 7 == 3:
      line = line.replace("  Test: divisible by ", "")
      line = line.replace(" ", "")
      test_number = int(line)
      current_monkey.append(test_number)

    if i % 7 == 4:
      line = line.replace("    If true: throw to monkey ", "")
      true_monkey = int(line)
      current_monkey.append(true_monkey)
    if i % 7 == 5:
      line = line.replace("    If false: throw to monkey ", "")
      false_monkey = int(line)
      current_monkey.append(false_monkey)

  return parsed_monkeys

def create_operation(operation_text: str) -> Operation:
  add = False
  multiply = False
  fixed_value = -1

  if(operation_text[0] == "+"):
    add = True
  if(operation_text[0] == "*"):
    multiply = True

  value = operation_text[1:len(operation_text)]
  fixed_value = int(value) if value.isdecimal() else None
  return Operation(add, multiply, fixed_value)

def create_monkeys(parsed_input: list) -> list:

  monkeys = []

  for element in parsed_input:
    items = element[0]
    operation = create_operation(element[1])
    test_number = element[2]
    true_monkey = element[3]
    false_monkey = element[4]

    monkey = Monkey(items, operation, test_number, true_monkey, false_monkey)
    monkeys.append(monkey)
    
  return monkeys

def calculate_monkey_business(rounds: int, monkeys: list) -> int:
  common_module = 1
  for monkey in monkeys:
    common_module *= monkey.test_number

  for i in range(rounds):
    for monkey in monkeys:
      monkey.inspect_and_throw_items(monkeys, False, common_module)
    
  for monkey in monkeys:
    print(f"Monkey {monkeys.index(monkey)}: {monkey.items}")

  inspections = []
  for monkey in monkeys:
    inspections.append(monkey.inspections)

  largest = max(inspections)
  inspections.remove(largest)
  second_largest = max(inspections)

  monkey_business = largest * second_largest
  return monkey_business

######MAIN##########

print("running...")

input = "input.txt"
parsed_input = parse_input(input)
monkeys = create_monkeys(parsed_input)
rounds = 10000
monkey_business = calculate_monkey_business(rounds, monkeys)

for monkey in monkeys:
  print(f"Monkey {monkeys.index(monkey)} inspected items {monkey.inspections} times.")
print(f"Monkey business: {monkey_business}") #PART TWO ANSWER, note that the method Monkey.inspect_and_throw_items() decreased_worry_level is changed to accommodate PART TWO

