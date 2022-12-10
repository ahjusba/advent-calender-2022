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
        if dir == "R":
            self.x += 1
        if dir == "D":
            self.y -= 1
        if dir == "L":
            self.x -= 1

    def follow(self, other: Vector2, dir: str):
        offset = Vector2(0, 0)
        if dir == "U":
            offset.y += 1
            offset.x += other.x - self.x

        if dir == "R":
            offset.x += 1
            offset.y += other.y - self.y
        if dir == "D":
            offset.y -= 1
            offset.x += other.x - self.x
        if dir == "L":
            offset.x -= 1
            offset.y += other.y - self.y
        
        self.x += offset.x
        self.y += offset.y

    def is_farther_than_one_space(self, other):
        if not isinstance(other, Vector2):
            return NotImplemented #Dont allow comparing with other classes

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

            for i in range(1, len(knots)): #The last knot only follows

                if knots[i].is_farther_than_one_space(knots[i - 1]):
                    knots[i].follow(knots[i - 1], dir)

                if i == knot_to_follow - 1:
                    if knot_is_in_unique_place(knots[i], unique_positions):
                        # print(f"Knot {i+1} is in unique position {knots[i].x},{knots[i].y}")
                        unique_pos = Vector2(knots[i].x, knots[i].y)
                        unique_positions.append(unique_pos)

            print(f"Command: {command}", end="")
            for knot in knots:
                print(f"[{knot.x},{knot.y}]", end="")
            print("")



    return unique_positions


def knot_is_in_unique_place(T_pos: Vector2, unique_positions: list) -> bool:
    is_unique = True
    for pos in unique_positions:
        if T_pos.__eq__(pos):
            is_unique = False
    return is_unique

input = "test-input.txt"
commands = parse_input(input)
unique_positions = get_unique_positions(commands, 10, 10)

print("Number of unique positions:", len(unique_positions))
