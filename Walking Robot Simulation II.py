# A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

# The robot can be instructed to move for a specific number of steps. For each step, it does the following.

# Attempts to move forward one cell in the direction it is facing.
# If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
# After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

# Implement the Robot class:

# Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
# void step(int num) Instructs the robot to move forward num steps.
# int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
# String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".

# Key Insight(Calculation)

# The robot keeps walking along the boundary of the grid in a loop.

# Total cycle length:
# cycle = 2 * (width + height - 2)

# So instead of moving num steps one by one, we do:

# num = num % cycle

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South
        
        self.directions = ["East", "North", "West", "South"]
        self.cycle = 2 * (width + height - 2)

    def step(self, num: int) -> None:
        if self.cycle == 0:
            return
        
        num %= self.cycle
        
        # Special case (important!)
        if num == 0:
            num = self.cycle
        
        for _ in range(num):
            if self.dir == 0:  # East
                if self.x + 1 < self.w:
                    self.x += 1
                else:
                    self.dir = 1
                    self.y += 1
                    
            elif self.dir == 1:  # North
                if self.y + 1 < self.h:
                    self.y += 1
                else:
                    self.dir = 2
                    self.x -= 1
                    
            elif self.dir == 2:  # West
                if self.x - 1 >= 0:
                    self.x -= 1
                else:
                    self.dir = 3
                    self.y -= 1
                    
            else:  # South
                if self.y - 1 >= 0:
                    self.y -= 1
                else:
                    self.dir = 0
                    self.x += 1

    def getPos(self) -> [int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.directions[self.dir]
