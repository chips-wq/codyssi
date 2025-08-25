import sys
import string

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

mapping = {}
for i in range(9 + 1):
  mapping[str(i)] = i

for i, el in enumerate(string.ascii_uppercase):
  mapping[el] = i + 10

for i, el in enumerate(string.ascii_lowercase):
  mapping[el] = i + 36

for i, el in enumerate("!@#$%^"):
  mapping[el] = i + 62

def convert(str_num : str, base: int):
  ans = 0
  for i, el in enumerate(str_num[::-1]):
    ans += mapping[el] * (base ** i)
  return ans

reverse_mapping = {}
for letter, idx in mapping.items():
  reverse_mapping[idx] = letter
    
"""
reminder

say this is base 16
A12
210
10 * 16^2 + 1 * 16^1 + 2 * 16^0

3519
3210

9 * 10^0 + 1 * 10^1

How does one conver from base 10 to another base

if you do % 68, that's the 
"""

ans = 0
for line in open(infile):
  line = line.strip()
  str_num, base = line.split(" ")
  base = int(base)
  
  num = convert(str_num, base)
  ans += num
  
ans2 = ""
while ans > 0:
  ans2 += reverse_mapping[ans % 68]
  ans //= 68
print(ans2[::-1])
