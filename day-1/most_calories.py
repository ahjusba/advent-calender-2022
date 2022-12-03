def create_elves(file_name: str) -> list:
  elves = []
  with open(file_name) as new_file:
    elf = []
    for line in new_file:
      line = line.replace("\n", "")

      #empty line, add the elf to elves and start a new elf
      if line == "":            
        elves.append(elf)
        elf = []
      else:
        elf.append(int(line))

  return elves
  
def get_calories_of_wealthiest_elves(elves: list, how_many: int) -> int:
  elves.sort(key=sum)
  total_calories = 0
  for i in range(how_many):
    total_calories += sum(elves[len(elves) - (i + 1)],0 )
  return total_calories


elves = create_elves("calories.txt")
calories = get_calories_of_wealthiest_elves(elves, 3)
print("Most calories", calories)
