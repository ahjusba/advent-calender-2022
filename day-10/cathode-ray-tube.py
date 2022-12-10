def parse_input(input: str) -> list:
    commands = []
    for line in open(input):
        line = line.replace("\n", "")
        if line == "noop":
            command = [1, 0]
        else:
            splitted_line = line.split(" ")
            command = [2, int(splitted_line[1])]
        commands.append(command)    
    return commands

def get_strength_at_cycle(cycle: int, commands: list) -> int:
    register_value = 1
    current_cycle = 0
    for command in commands:
        current_cycle += command[0]
        if current_cycle >= cycle:
            return register_value * cycle
        else:
            register_value += command[1]

def get_sum_of_strengths_with_step(start: int, end: int, step: int, commands: list) -> int:
    sum = 0
    for i in range(start, end + 1, step):
        strength = get_strength_at_cycle(i, commands)
        sum += strength
        print(f"Str at {i} is {strength}")
    return sum



def draw_screen(commands: list, crt_screen: list, row_length: int) -> list:
    register_value = 1
    current_cycle = 0
    current_row = 0
    for command in commands:
        for cycle in range(command[0]):
            if register_value - 1 <= current_cycle % row_length <= register_value + 1:
                crt_screen[current_row] += "#"
            else:
                crt_screen[current_row] += "."
            current_cycle += 1
            if current_cycle % row_length == 0:
                current_row += 1        
        register_value += command[1]
    return crt_screen

def create_crt_screen(commands: list, row_length: int) -> list:
    crt_screen = []
    cycles = 0

    for command in commands:
        cycles += command[0]
    
    rows = cycles // row_length
    print(f"Number of rows: {rows} and cycles: {cycles}")

    for row in range(rows):
        crt_screen.append("")
    return crt_screen
    




input = "input.txt"
commands = parse_input(input)
sum_of_strengths = get_sum_of_strengths_with_step(20, 220, 40, commands)
print("SUM:", sum_of_strengths) #PART ONE ANSWER

crt_screen = create_crt_screen(commands, 40)
drawn_screen = draw_screen(commands, crt_screen, 40)

for row in drawn_screen:
    print(row) #PART TWO ANSWER
