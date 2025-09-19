from commands.abc_command import Instruction
from commands.multiply_all_command import MultiplyAllInstruction
from commands.add_all_command import AddAllInstruction
from commands.multiply_column_command import MultiplyColumnInstruction
from commands.multiply_row_command import MultiplyRowInstruction
from commands.add_column_command import AddColumnInstruction
from commands.add_row_command import AddRowInstruction
from commands.shift_col_command import ShiftColumnInstruction
from commands.shift_row_command import ShiftRowInstruction

def _parse_all(args: list[str]) -> Instruction:
  assert args[2] == "ALL"
  amount = int(args[1])
  if args[0] == "MULTIPLY":
    return MultiplyAllInstruction(amount)
  
  assert (args[0] == "ADD" or args[0] == "SUB")

  if args[0] == "SUB":
    amount = amount * -1

  return AddAllInstruction(amount)

def _parse_row_or_col(args: list[str]):
  # {ADD/SUB/MULTIPLY} {amount} {ROW/COL} {number}
  amount = int(args[1])
  row_or_col = args[2]
  row_or_col_num = int(args[3]) - 1

  if args[0] == "MULTIPLY":
    if row_or_col == "ROW":
      return MultiplyRowInstruction(amount, row_or_col_num)
    else:
      assert row_or_col == "COL"
      return MultiplyColumnInstruction(amount, row_or_col_num)

  if args[0] == "SUB":
    amount = amount * -1
  
  if row_or_col == "ROW":
    return AddRowInstruction(amount, row_or_col_num)
  else:
    assert row_or_col == "COL"
    return AddColumnInstruction(amount, row_or_col_num)

def _parse_shift(args: list[str]):
  assert args[0] == "SHIFT"
  assert args[3] == "BY"
  row_or_col = args[1]
  row_or_col_num = int(args[2]) - 1
  amount = int(args[4])
  
  if row_or_col == "ROW":
    return ShiftRowInstruction(amount, row_or_col_num)
  else:
    assert row_or_col == "COL"
    return ShiftColumnInstruction(amount, row_or_col_num)

def parse(command : str) -> Instruction:
  print(f"parsing {command}")
  args = command.strip().split()
  if args[0] == "SHIFT":
    return _parse_shift(args)
  if args[-1] == "ALL":
    return _parse_all(args)
  return _parse_row_or_col(args)


