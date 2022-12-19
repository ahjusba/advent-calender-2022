
import math

class Node:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.distance = math.inf
  
  def __str__(self) -> str:
    return f"[{self.x},{self.y},D{self.distance}]"



  def get_neighbors(self, nodes: list) -> list:
    neighbors = []
    for node in nodes:
      if node.z - self.z > 1: #Too steep climb
        continue
      
      x_offset = abs(node.x - self.x)
      if x_offset > 1:  #Not on an adjancent column
        continue
      
      y_offset= abs(node.y - self.y)
      if y_offset > 1: #Not on an adjancent row
        continue

      if x_offset == 1 and y_offset == 1:
        continue #Diagonally adjacent

      if x_offset == 0 and y_offset == 0:
        continue #This node
      
      neighbors.append(node)     
    return neighbors

def parse_input(input: str):
  file = open(input)
  input_text = list(file)
  file.close()

  grid = []
  key_positions = [(0,0,0), (0,0,0)]

  for y in range(len(input_text)):
    line = input_text[y]
    line = line.replace("\n", "")
    row = []
    for x in range(len(line)):
      z = ord(line[x])
      z -= 97 #ASCII order offset
      if(line[x] == "S"):
        z = ord("a") - 97
        key_positions[0] = (x, y, z)
      if(line[x] == "E"):
        z = ord("z") - 97
        key_positions[1] = (x, y, z)      
      row.append(z)
    grid.append(row)
  return [grid, key_positions]

def create_nodes(grid: list) -> list:
  nodes = []

  for y in range(len(grid)):
    for x in range(len(grid[y])):
      z = grid[y][x]
      node = Node(x, y, z)
      nodes.append(node)

  return nodes

def dikjstra(nodes: list, start: tuple, end: tuple) -> int:
  unvisited = list(nodes)

  source = None
  target = None
  for node in unvisited:    
    if node.x == start[0] and node.y == start[1]:      
      source = node
    if node.x == end[0] and node.y == end[1]:      
      target = node
  
  print(f"Start node: [{source.x},{source.y}]")
  print(f"Target node: [{target.x},{target.y}]")

  source.distance = 0

  ##START PART TWO SPECIFIC###
  for node in nodes:
    if node.z == source.z:
      node.distance = 0
  ##END PART TWO SPECIFIC###

  current = source

  while (current != None and target in unvisited and len(unvisited) > 0):
    unvisited.remove(current)
    neighbors = current.get_neighbors(nodes)
    for neighbor in neighbors:
      dist = current.distance + 1
      if dist < neighbor.distance:
        neighbor.distance = dist    

    current = None
    dist = math.inf 
    for node in unvisited:
      if node.distance < dist:
        dist = node.distance
        current = node
  
  minimum_number_of_steps = target.distance
  return minimum_number_of_steps


input = "input.txt"
parsed_data = parse_input(input)
grid = parsed_data[0]
key_positions = parsed_data[1]
nodes = create_nodes(grid)
minimum_number_of_steps = dikjstra(nodes, key_positions[0], key_positions[1])


# def print_grid(grid, nodes):
#   for y in range(len(grid)):
#     for x in range(len(grid[y])):
#       for node in nodes:
#         if(node.x == x and node.y == y):
#           value = node.distance
#           string = f"{value} "
#           if value < 10:
#             string += " "
#           print(string, end="")
#     print("")
# print_grid(grid, nodes)



print(f"Minimum number of steps: {minimum_number_of_steps}")