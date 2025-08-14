infile = "part1.txt"

with open(infile, "r") as f:
  content = f.read()
  ans = 0
  for line in content.splitlines():
    r1, r2 = line.split(" ")
    a, b = [int(el) for el in r1.split("-")]
    c, d = [int(el) for el in r2.split("-")]

    ans += b-a+1 + d-c+1

  print(ans)
