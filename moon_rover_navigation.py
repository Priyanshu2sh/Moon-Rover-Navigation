class Rover:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing

    def turn_left(self):
        if self.facing == 'N':
            self.facing = 'W'
        elif self.facing == 'W':
            self.facing = 'S'
        elif self.facing == 'S':
            self.facing = 'E'
        elif self.facing == 'E':
            self.facing = 'N'

    def turn_right(self):
        if self.facing == 'N':
            self.facing = 'E'
        elif self.facing == 'E':
            self.facing = 'S'
        elif self.facing == 'S':
            self.facing = 'W'
        elif self.facing == 'W':
            self.facing = 'N'

    def move_forward(self, plateau_x, plateau_y):
        if self.facing == 'N' and self.y < plateau_y:
            self.y += 1
        elif self.facing == 'E' and self.x < plateau_x:
            self.x += 1
        elif self.facing == 'S' and self.y > 0:
            self.y -= 1
        elif self.facing == 'W' and self.x > 0:
            self.x -= 1

def navigate_plateau(upper_right, rover_info):
    plateau_x, plateau_y = map(int, upper_right.split())
    rovers = []
    for info in rover_info:
        x, y, facing = info[0], info[1], info[2]
        facing=facing.upper()
        rover = Rover(int(x), int(y), facing)
        instructions = info[3]
        for instruction in instructions:
            if instruction == 'L':
                rover.turn_left()
            elif instruction == 'R':
                rover.turn_right()
            elif instruction == 'M':
                rover.move_forward(plateau_x, plateau_y)
        rovers.append(rover)
    return rovers

def format_output(rovers):
    output = []
    for rover in rovers:
        output.append(f"{rover.x} {rover.y} {rover.facing}")
    return output

def get_input():
    print("Please enter the upper-right coordinates of the plateau in the format 'x y': ")
    upper_right = input("Example: 5 5\n")

    rover_info = []
    print("\nPlease enter the rover's position and instructions for each rover.")
    print("Each line should contain the rover's position (x y facing) followed by instructions (e.g., LMRMLM).")
    print("Type 'done' when you're finished.\n")

    while True:
        rover_position = input("Rover position and instructions: ").strip().upper()
        if rover_position.lower() == 'done':
            break
        rover_info.append(tuple(rover_position.split()))
    return upper_right, rover_info

# Main program
upper_right, rover_info = get_input()
rovers = navigate_plateau(upper_right, rover_info)
output = format_output(rovers)

# Print Output
print("\nFinal positions of the rovers:")
for position in output:
    print(position)
