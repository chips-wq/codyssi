import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

def receive(amounts : dict[str, int], debts : dict[str, list[tuple[int,str]]], receiver : str, amt):
  amounts[receiver] += amt
  # Repay all of the debts that amounts[receiver] has
  while len(debts[receiver]):
    # Pay as much as you can from amounts[receiver]
    c_debt, to = debts[receiver][0]
    debts[receiver] = debts[receiver][1:]

    if amounts[receiver] >= c_debt:
      amounts[receiver] -= c_debt
      receive(amounts, debts, to, c_debt)
    else:
      c_debt = c_debt - amounts[receiver]
      to_recv = amounts[receiver]
      amounts[receiver] = 0
      debts[receiver].insert(0, (c_debt, to))

      receive(amounts, debts, to, to_recv)
      break

with open(infile, "r") as f:
  content = f.read().strip()
  p1, p2 = content.split("\n\n")
  amounts = {}
  debts = {}

  for line in p1.strip().splitlines():
    name, amount = line.split(" HAS ")
    name = name.strip()
    amount = int(amount)

    amounts[name] = amount
    debts[name] = []

  for line in p2.strip().splitlines():
    giver = line.split("TO")[0].strip().split("FROM ")[1].strip()
    receiver = line.split("TO")[1].strip().split("AMT")[0].strip()
    amt = int(line.split("AMT")[1].strip())

    if amounts[giver] - amt < 0:
      # How much does he owe ?
      debt = amt - amounts[giver]
      debts[giver].append((debt, receiver)) 

      amt = amounts[giver]

    amounts[giver] -= amt
    receive(amounts, debts, receiver, amt)


  print(amounts)
  print(debts)

  a = amounts.values()
  b = list(a)
  b.sort(reverse=True)
  ans = b[0] + b[1] + b[2]


  print(ans)
  print(type(a))
  print(a)
