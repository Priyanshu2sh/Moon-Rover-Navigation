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
    plateau_x, plateau_y = upper_right
    rovers = []
    for info in rover_info:
        x, y, facing = info[0], info[1], info[2]
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

def get_upper_right():
    while True:
        try:
            upper_right = input("Enter the upper-right coordinates of the plateau (x y): ").strip().lower()
            if len(upper_right.split()) != 2:
                print("\nBoth x and y coordinates are required.")
                continue
            plateau_x, plateau_y = map(int, upper_right.split())
            return plateau_x, plateau_y
        except ValueError:
            print("\nInvalid input. Both x and y coordinates should be integers.")

def get_rover_info(rover_num, plateau_x, plateau_y):
    while True:
        try:
            x, y, facing = input(f"Enter rover {rover_num} position (x y facing - N, E, W, S)\nFor Example: 1 4 E\n ").strip().lower().split()
            x, y = int(x), int(y)
            if facing not in ['n', 'e', 'w', 's']:
                print("\nFacing direction should be N, E, W, or S.")
                continue
            if x < 0 or x > plateau_x or y < 0 or y > plateau_y:
                print("\nRover position should be within plateau boundaries. Please enter again.")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter integers for coordinates.")
    
    while True:
        try:
            instructions = input(f"Enter rover {rover_num} instructions: ").upper()
            if any(instruction not in ['L', 'R', 'M'] for instruction in instructions):
                print("\nInvalid instructions. Only 'L', 'R', 'M' are allowed.")
                continue
            return x, y, facing.upper(), instructions
        except ValueError:
            print("\nInvalid input. Please enter valid instructions.")

def run_tests():
    try:
        # Test 1: Rover moves within the plateau boundaries
        upper_right = (5, 5)
        rover_info = [(1, 2, 'N', "LMLMLMLMM")]
        expected_output = ["1 3 N"]
        assert format_output(navigate_plateau(upper_right, rover_info)) == expected_output

        # Test 2: Rover moves within the plateau boundaries
        rover_info = [(3, 3, 'E', "MMRMMRMRRM")]
        expected_output = ["5 1 E"]
        assert format_output(navigate_plateau(upper_right, rover_info)) == expected_output

        # Test 3: Rover moves outside the plateau boundaries
        rover_info = [(2, 4, 'E', "MLMRMLM")]
        expected_output = ["4 5 N"]
        assert format_output(navigate_plateau(upper_right, rover_info)) == expected_output

        print("\nAll test cases passed!")
    except AssertionError as e:
        print(f"\nTest failed: {e}")
    except Exception as e:
        print(f"\nAn error occurred during testing: {e}")

def main():
    try:
        # Get upper right coordinates
        plateau_x, plateau_y = get_upper_right()

        # Get number of rovers
        while True:
            try:
                rover_count = int(input("Enter the number of rovers: ").strip())
                if rover_count < 1:
                    print("\nNumber of rovers should be greater than or equal to 1.")
                    continue
                break
            except ValueError:
                print("\nInvalid input. Please enter an integer.")

        # Get rover information
        rover_info = []
        for i in range(rover_count):
            x, y, facing, instructions = get_rover_info(i + 1, plateau_x, plateau_y)
            rover_info.append((x, y, facing, instructions))

        # Navigate plateau
        rovers = navigate_plateau((plateau_x, plateau_y), rover_info)

        # Format and print output
        print("\nFinal positions of the rovers:")
        for position in format_output(rovers):
            print(position)
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    run_tests()
    main()
