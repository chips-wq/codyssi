# {ADD/SUB/MULTIPLY} {amount} {ROW/COL} {number}

from commands.abc_command import Instruction
from commands.constants import MOD

class AddRowInstruction(Instruction):
  def __init__(self, amount : int, row : int):
    self.amount = amount
    self.row = row

  def execute(self, grid: list[list[int]]):
    grid[self.row] = [(val + self.amount) % MOD for val in grid[self.row]]

