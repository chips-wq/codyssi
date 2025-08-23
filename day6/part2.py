import sys
import string

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

dict = {}

for ch in string.ascii_lowercase:
  dict[ord(ch) - ord('a') + 1] = ch

for ch in string.ascii_uppercase:
  dict[ord(ch) - ord('A') + 27] = ch


def mapping(c : str) -> int:
  assert c in string.ascii_letters
  if c in string.ascii_lowercase:
    return ord(c) - ord('a') + 1
  elif c in string.ascii_uppercase:
    return ord(c) - ord('A') + 27
  return -1


def int_to_ch(num : int):
  while (num < 1):
    num += 52
  assert num <= 52
  while (num > 52):
    num -= 52
  assert num >= 1
  return dict[num]

for line in open(infile):
  line = line.strip()

  ans = [mapping(ch) for ch in line if ch in string.ascii_letters]
  print(sum(ans))

  