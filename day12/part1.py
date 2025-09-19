import sys
from commands.abc_command import Instruction
from commands.parser import parse
infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

print(sys.path)

# You could use something like command pattern
"""
If you would like OOP, then you could have an object called 

class Grid:

It would use composition to have multiple "commands".

Each command has an execute function that takes in a grid and performs that particular action on it.

We don't have interfaces in python, (we have abstract classes though)
"""


class Grid:
  def __init__(self, grid: list[list[int]], instructions : list[Instruction], flow_control: list[str]):
    self.grid = grid
    self.instructions = instructions
    self.flow_control = flow_control

  def apply_commands(self):
    # self.instructions[0].execute(self.grid)
    # self.instructions[1].execute(self.grid)
    # self.instructions[2].execute(self.grid)
    for command in self.instructions:
      command.execute(self.grid)

  def apply_flow_control(self):
    taken = None
    for flow in self.flow_control:
      if flow == "TAKE":
        assert taken == None
        taken = self.instructions.pop(0)
      elif flow == "CYCLE":
        assert taken != None
        self.instructions.append(taken)
        taken = None
      elif flow == "ACT":
        assert taken != None
        taken.execute(self.grid)
        taken = None

  def apply_all_flow_control(self):
    while self.instructions:
      taken = None
      for flow in self.flow_control:
        if flow == "TAKE":
          assert taken == None
          if not self.instructions: break
          taken = self.instructions.pop(0)
        elif flow == "CYCLE":
          assert taken != None
          self.instructions.append(taken)
          taken = None
        elif flow == "ACT":
          assert taken != None
          taken.execute(self.grid)
          taken = None

  def get_max_row_sum(self):
    row_sums = [sum(row) for row in self.grid]
    return max(row_sums)

  def get_max_col_sum(self):
    col_sums = [sum(col) for col in zip(*self.grid)]
    return max(col_sums)

  def pretty_print(self):
    for row in self.grid:
      print(row)


def part_1(grid: Grid):
  grid.pretty_print()
  grid.apply_commands()
  print()
  grid.pretty_print()

  print(max(grid.get_max_col_sum(), grid.get_max_row_sum()))

def part2(grid: Grid):
  grid.pretty_print()
  grid.apply_flow_control()
  print()
  grid.pretty_print()

  print(max(grid.get_max_col_sum(), grid.get_max_row_sum()))

def part3(grid: Grid):
  grid.pretty_print()
  grid.apply_all_flow_control()
  print()
  grid.pretty_print()

  print(max(grid.get_max_col_sum(), grid.get_max_row_sum()))


with open(infile, "r") as f:
  contents = f.read().strip()
  grid, instructions, flow = contents.split("\n\n")
  
  grid = [[int(el) for el in row.split(" ")] for row in grid.splitlines()]

  instructions = instructions.strip().splitlines()
  instructions = [parse(instruction) for instruction in instructions]

  flow = flow.strip().splitlines()
  
  grid = Grid(grid, instructions, flow)

  part3(grid)
