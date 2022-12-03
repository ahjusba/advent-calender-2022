#Points
#Rock: 1        Paper: 2        Scissors: 3
#Lose: 0        Draw: 3         Win: 6

#A = X = Rock
#B = Y = Paper
#C = Z = Scissors

class Action():
  def __init__(self, input: str, enemy_hand_value: int):
    self.input = input
    if(enemy_hand_value == -1):
      self.value = self.get_action(self.input)
    else:
      self.value = self.get_action_based_on_enemy_action(input, enemy_hand_value)
  
  def get_action(self, input: str) -> int:
    if input == "A": #ROCK
      return 1
    if input == "B": #PAPER
      return 2
    if input == "C": #SCISSORS
      return 3

  def get_action_based_on_enemy_action(self, input: str, enemy_hand_value: int) -> int:
    victories = {
      3: [2], #Scissors beats paper
      2: [1], #Paper beats rock
      1: [3]  #Rock beats scissors
    }

    if input == "X": #MUST LOSE
      return victories[enemy_hand_value][0]
    if input == "Y": #MUST DRAW
      return enemy_hand_value
    if input == "Z": #MUST WIN
      winning_action = (enemy_hand_value + 1) % 4
      if winning_action == 0:
        winning_action = 1
      return winning_action

class Game():
  def __init__(self, my_hand: Action, enemy_hand: Action):
    self.my_hand = my_hand
    self.enemy_hand = enemy_hand

    self.win_points = self.calculate_win_points(self.my_hand, self.enemy_hand)
    self.action_points = self.my_hand.value
    self.total_points = self.win_points + self.action_points

    # print(f"{self.enemy_hand.input}{self.enemy_hand.value} VS. {self.my_hand.input}{self.my_hand.value} = {self.total_points} points [{self.win_points}, {self.action_points}]")

  def calculate_win_points(self, my_hand: Action, enemy_hand: Action) -> int:
    victories = {
      3: [2], #Scissors beats paper
      2: [1], #Paper beats rock
      1: [3]  #Rock beats scissors
    }

    defeats = victories[my_hand.value] #Which hand our hand beats?
    
    if my_hand.value == enemy_hand.value:
      return 3 #DRAW
    elif enemy_hand.value in defeats:
      return 6 #WIN
    else:
      return 0 #LOSE
  
def create_games(input: list) -> list:
  game_list = []
  for item in input:
    enemy_hand = Action(item[0], -1)
    my_hand = Action(item[1], enemy_hand.value)
    game = Game(my_hand, enemy_hand)
    game_list.append(game)
  return game_list

def listify_input(input: str) -> list:
  input_list = []
  with open(input) as file:
    for line in file:
      line = line.replace("\n", "") #Remove linebreaks
      line = line.replace(" ", "")  #Remove empty spaces
      input_list.append(line)
    return input_list      

def calculate_points(game_list: list) -> int:
  points = 0
  for game in game_list:
    points += game.total_points
  print("Total points:", points)
  return points

input_list = listify_input("input.txt")
game_list = create_games(input_list)
points = calculate_points(game_list)