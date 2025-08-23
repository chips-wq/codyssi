import sys
import string

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

dict = {}

for ch in string.ascii_lowercase:
  dict[ord(ch) - ord('a') + 1] = ch

for ch in string.ascii_uppercase:
  dict[ord(ch) - ord('A') + 27] = ch


def ch_to_int(c : str) -> int:
  assert c in string.ascii_letters
  if c in string.ascii_lowercase:
    return ord(c) - ord('a') + 1
  elif c in string.ascii_uppercase:
    return ord(c) - ord('A') + 27
  return -1


def int_to_ch(num : int):
  while (num < 1):
    num += 52
  assert num >= 1
  while (num > 52):
    num -= 52
  assert num <= 52
  return dict[num]

for line in open(infile):
  line = line.strip()

  new_line = line[0] 
  for i, ch in enumerate(line[1:]):
    ch_prev = new_line[i]
    assert ch_prev in string.ascii_letters

    if ch not in string.ascii_letters:
      ch_prev_val = ch_to_int(ch_prev) * 2 - 5
      ch_this = int_to_ch(ch_prev_val)
      new_line += ch_this
    else:
      new_line += ch

  print(sum(ch_to_int(ch) for ch in new_line))

  print(new_line)

      

  