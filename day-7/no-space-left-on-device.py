from __future__ import annotations
from operator import attrgetter

class Directory:
  def __init__(self, data, previous_dir):
    self.data = data
    self.previous_dir = previous_dir
    self.files = []
    self.dirs = []
    self.size = 0

  def __str__(self):
    return self.data

  def add_file(self, file: File):
    self.add_size_to_this_and_upper_folders(file.size)
    self.files.append(file)

  def add_dir(self, dir):
    self.dirs.append(dir)

  def get_sub_folder(self, sub_folder_data) -> Directory:
    if len(self.dirs) == 0:
      print("Something went wrong: you're trying to access a folder even though the folder hasn't been instantiated yet")

    for dir in self.dirs:
      if dir.data == sub_folder_data:
        return dir

  def add_size_to_this_and_upper_folders(self, size):
    self.size += size
    if self.previous_dir != None:
      self.previous_dir.add_size_to_this_and_upper_folders(size)

  def list_of_dirs_over_size(self, size: int, list_of_dirs: list) -> list:
    if self.size >= size:
      list_of_dirs.append(self)

    for dir in self.dirs:
      dir.list_of_dirs_over_size(size, list_of_dirs)

    return list_of_dirs

  def list_of_dirs_below_size(self, size: int, list_of_dirs: list) -> list:
    if self.size <= size:
      list_of_dirs.append(self)

    for dir in self.dirs:
      dir.list_of_dirs_below_size(size, list_of_dirs)

    return list_of_dirs

class File:
  def __init__(self, size, data):
    self.size = int(size)
    self.data = data

def get_commands_from_input(input: str):
  commands = []
  for line in list(open(input)):
    line = line.replace("\n", "")
    commands.append(line)
  return commands

def create_tree(commands: str) -> Directory:
  root_dir = None
  current_dir = None
  for c in commands:

    print_statment = ""

    if c[0] != "$":
      if c[0:3] == "dir":
        dir_info = c.split(" ")
        dir_data = dir_info[1]
        new_dir = Directory(dir_data, current_dir)
        current_dir.add_dir(new_dir)
        print_statment += (f"dir {dir_data}")

      else:
        file_info = c.split(" ")
        file_size = file_info[0]
        file_data = file_info[1]
        new_file = File(file_size, file_data)
        current_dir.add_file(new_file)
        print_statment += (f"file {file_data}")        

    if c == "$ ls":
      print_statment += ("$ ls")

    if c == "$ cd /":
      first_dir = Directory("root", None)
      current_dir = first_dir
      root_dir = first_dir
      print_statment += ("$ cd /")
      print(print_statment)
      continue
    
    if c == "$ cd ..":
      previous_dir = current_dir.previous_dir
      print_statment += (f"$ cd .. || current_dir: {current_dir} opened_dir: {previous_dir}")  
      current_dir = previous_dir
      print(print_statment)
      
      continue

    if c[0:5] == "$ cd ":
      splitted_command = c.split(" ")
      dir_data = splitted_command[2]
      opened_dir = current_dir.get_sub_folder(dir_data)
      print_statment += (f"$ cd {dir_data} || current_dir: {current_dir} opened_dir: {opened_dir}")  
      current_dir = opened_dir

    print(print_statment)

  return root_dir

#MAIN
commands = get_commands_from_input("input.txt")
root_node = create_tree(commands)

list_of_dirs = []
list_of_dirs = root_node.list_of_dirs_below_size(100000, list_of_dirs)
total_sum = 0
for dir in list_of_dirs:
  total_sum += dir.size

#################################################
print("Total sum:", total_sum) #PART ONE SOLUTION
#################################################


total_space = 70000000
update_size = 30000000
used_space = root_node.size
unused_space = total_space - used_space
required_space = update_size - unused_space

list_of_dirs = []
list_of_dirs = root_node.list_of_dirs_over_size(required_space, list_of_dirs)

smallest_possible_dir = min(list_of_dirs, key=attrgetter('size'))

#########################################################
print(f"{smallest_possible_dir.size}") #PART TWO SOLUTION
#########################################################