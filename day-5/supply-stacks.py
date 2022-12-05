import re

def parse_stacks(input: str) -> list:
  chars_per_column = 4
  stacks = []

  for line in reversed(list(open(input))):
    #FIRST ITERATION: CREATE STACKS
    if len(stacks) <= 0:
      length = len(line)      
      columns = length // chars_per_column + 1 #The last column isn't followed by whitespace
      for i in range(columns):
        stacks.append([])
      continue
    
    #ADD LETTERS TO STACKS
    for i in range(len(stacks)):
      char_index = 1 + i * chars_per_column
      if line[char_index] == " ":
        continue
      stacks[i].append(line[1 + i * chars_per_column])
    
  return stacks

def parse_instructions(input: str) -> list:
  instructions = []
  for line in list(open(input)):
    line = line.replace("\n", "")
    text_instruction = re.split(r'move | from | to ', line)
    text_instruction.remove("")
    number_instruction = [eval(i) for i in text_instruction]
    instructions.append(number_instruction)
  return instructions

def executed_stacks(instructions: list, stacks: list) -> list:
  for ins in instructions:
    moves = ins[0]
    start = stacks[ins[1] - 1]
    end = stacks[ins[2] - 1]

    for i in range(moves):
      popped = start.pop()
      end.append(popped)

  return stacks

def executed_stacks_part2(instructions: list, stacks: list) -> list:
  for ins in instructions:
    moves = ins[0]
    start = stacks[ins[1] - 1]
    end = stacks[ins[2] - 1]

    block = start[len(start) - moves: len(start)]

    for i in range(len(block)):
      start.pop()
      end.append(block[i])

  return stacks

def get_top_letters(stacks: list) -> str:
  top_letters = ""

  for stack in stacks:
    char = stack[-1]
    top_letters += char

  return top_letters

    
      
stacks = parse_stacks("initial-setup.txt")
instructions = parse_instructions("instructions-input.txt")
# reorganized_stacks = executed_stacks(instructions, stacks)
# top_letters = get_top_letters(reorganized_stacks)
# print("Top Letters:", top_letters) #PART ONE ANSWER, note that the stacks will be mutated if you run both PART ONE and PART TWO

reorganized_stacks_part2 = executed_stacks_part2(instructions, stacks)
top_letters = get_top_letters(reorganized_stacks_part2)
print("Top Letters:", top_letters) #PART TWO ANSWER

