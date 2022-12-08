def parse_input(input: str) -> list:
  tree_matrix = []
  for line in list(open(input)):
    row = []
    line = line.replace("\n", "")
    for char in line:
      row.append(int(char))
    tree_matrix.append(row)
  return tree_matrix

def is_visible_horizontally(matrix: list, x: int, y: int) -> bool:
  row = matrix[x]
  column = y
  value = row[y]

  left_visible = True
  right_visible = True

  #Loop the row from start to value-index
  for i in range(0, column):
    if row[i] >= value:
      left_visible = False
      break
  
  #Loop from value-index to end of row
  for i in range(column + 1, len(row)):
    if row[i] >= value:
      right_visible = False
      break
  return left_visible or right_visible

def is_visible_vertically(matrix: list, x: int, y: int) -> bool:
  row = x
  value = matrix[x][y]

  top_visible = True
  bottom_visible = True

  #Loop the rows and check the corresponding column-value (at index y) from top
  for i in range(0, row):
    if matrix[i][y] >= value:
      top_visible = False
      break

  #Loop the rows and check the corresponding column-value (at index y) to bottom
  for i in range(row + 1, len(matrix)):
    if matrix[i][y] >= value:
      bottom_visible = False
      break

  return top_visible or bottom_visible



def get_edge_visibles(matrix: list) -> int:
  horizontal_exterior_visibles = len(matrix[0]) * 2
  vertical_exterior_visibles = len(matrix) * 2
  overlappers = 4 #corners
  edge_visibles = horizontal_exterior_visibles + vertical_exterior_visibles - overlappers
  return edge_visibles


def get_number_of_visibles(tree_matrix: list) -> int:
  visibles = 0
  edge_visibles = get_edge_visibles(tree_matrix)

  x_length = len(tree_matrix)
  y_length = len(tree_matrix[0])

  for x in range(1, x_length - 1):
    for y in range(1, y_length - 1):
      if is_visible_horizontally(tree_matrix, x, y):
        print(f"Coordinate {x},{y} with value {tree_matrix[x][y]} is visible HORIZONTALLY at least")
        visibles += 1
        continue
      if is_visible_vertically(tree_matrix, x, y):
        print(f"Coordinate {x},{y} with value {tree_matrix[x][y]} is visible VERTICALLY at least")
        visibles += 1
        continue
  

  return visibles + edge_visibles


def get_scenic_score(tree_matrix: list) -> int:
  x_length = len(tree_matrix)
  y_length = len(tree_matrix[0])

  best_score = 0

  for x in range(0, x_length):
    for y in range(0, y_length):
      score = calculate_score_of_point(tree_matrix, x, y)
      if score > best_score:
        best_score = score

  return best_score


def calculate_score_of_point(matrix: list, x: int, y: int) -> int:
  #TO RIGHT
  value = matrix[x][y]
  width = len(matrix[0])
  height = len(matrix)

  right, left, top, bottom = 0, 0, 0, 0

  #RIGHT
  for i in range(y + 1, width):
    right += 1
    if matrix[x][i] >= value:
      break
  
  #LEFT
  for i in range(y - 1, -1, -1):
    left += 1
    if matrix[x][i] >= value:
      break

  #TOP
  for i in range(x - 1, -1, -1):
    top += 1
    if matrix[i][y] >= value:
      break
  
  #BOTTOM
  for i in range(x + 1, height):
    bottom += 1
    if matrix[i][y] >= value:
      break

  return right * left * top * bottom
  

input = "input.txt"
tree_matrix = parse_input(input)
# visibles = get_number_of_visibles(tree_matrix)
# print("Number of visible trees:", visibles) #PART ONE ANSWER

scenic_score = get_scenic_score(tree_matrix)
print("Scenic score of best tree is:", scenic_score) #PART TWO ANWER
