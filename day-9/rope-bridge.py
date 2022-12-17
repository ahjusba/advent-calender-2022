from __future__ import annotations

def parse_input(input: str) -> list:
    commands = []
    for line in list(open(input)):
        line = line.replace("\n", "")
        splitted_line = line.split(" ")
        command = [splitted_line[0], int(splitted_line[1])]
        commands.append(command)
    return commands

class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: Vector2) -> bool:
        if not isinstance(other, Vector2):
            return NotImplemented #Dont allow comparing with other classes
        return self.x == other.x and self.y == other.y

    def move(self, dir: str):
        if dir == "U":
            self.y += 1
        if dir == "D":
            self.y += -1
        if dir == "R":
            self.x += 1
        if dir == "L":
            self.x += -1

    def follow(self, other: Vector2):
        delta_x = other.x - self.x
        delta_y = other.y - self.y

        offset_x = 0
        offset_y = 0
        #PLEWse dont ready THIS
        if abs(delta_x) >= 2:
          if delta_x > 0:
            offset_x = 1
          else:
            offset_x = -1
            
          offset_y = (delta_y)
          if offset_y == 2:
            offset_y = 1
          if offset_y == -2:
            offset_y = -1

        elif abs(delta_y) >= 2:
          if delta_y > 0:
            offset_y = 1
          else:
            offset_y = -1

          offset_x = (delta_x)
          if offset_x == 2:
            offset_x = 1
          if offset_x == -2:
            offset_x = -1

        self.x += offset_x
        self.y += offset_y
          

    def is_farther_than_one_space(self, other):
        # if not isinstance(other, Vector2):
        #     return NotImplemented #Dont allow comparing with other classes

        return abs(self.x - other.x) >= 2 or abs(self.y - other.y) >= 2


def get_unique_positions(commands: list, knot_amount: int, knot_to_follow: int) -> list:
    knots = []
    for i in range(knot_amount):
        knots.append(Vector2(0, 0))
    unique_positions = [Vector2(0, 0)]

    for command in commands:

        dir = command[0]
        moves = command[1]

        for move in range(moves):
            knots[0].move(dir)

            for i in range(1, len(knots)):

                if knots[i].is_farther_than_one_space(knots[i - 1]):
                    knots[i].follow(knots[i - 1])

                if i == knot_to_follow - 1:
                    if knot_is_in_unique_place(knots[i], unique_positions):
                        # print(f"Knot {i+1} is in unique position {knots[i].x},{knots[i].y}")
                        unique_pos = Vector2(knots[i].x, knots[i].y)
                        unique_positions.append(unique_pos)

            # print(f"Command: {command}", end="")
            # for knot in knots:
            #     print(f"[{knot.x},{knot.y}]", end="")
            # print("")
    return unique_positions


def knot_is_in_unique_place(T_pos: Vector2, unique_positions: list) -> bool:
    is_unique = True
    for pos in unique_positions:
        if T_pos.__eq__(pos):
            is_unique = False
    return is_unique

input = "input.txt"
commands = parse_input(input)
unique_positions = get_unique_positions(commands, 10, 10)

print("Number of unique positions:", len(unique_positions)) #PART TWO ANSWER
