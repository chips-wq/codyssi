import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

with open(infile, "r") as f:
  content = f.read().strip()
  p1, p2 = content.split("\n\n")
  amounts = {}

  for line in p1.strip().splitlines():
    name, amount = line.split(" HAS ")
    name = name.strip()
    amount = int(amount)
    amounts[name] = amount

  for line in p2.strip().splitlines():
    giver = line.split("TO")[0].strip().split("FROM ")[1].strip()
    receiver = line.split("TO")[1].strip().split("AMT")[0].strip()
    amt = int(line.split("AMT")[1].strip())

    if amounts[giver] - amt < 0:
      amt = amounts[giver]

    amounts[giver] -= amt
    amounts[receiver] += amt

  a = amounts.values()
  b = list(a)
  b.sort(reverse=True)
  ans = b[0] + b[1] + b[2]


  print(ans)
  print(type(a))
  print(a)
