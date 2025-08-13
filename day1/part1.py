infile = "part1.txt"

with open(infile, "r") as f:
  content = f.read()
  
  nums = content.splitlines()[:600]
  ops = content.splitlines()[600]
  nums = [int(num) for num in nums]

  ans = nums[0]
  for (el, op) in zip(nums[1:], ops):
    if op == '+':
      ans += el
    else:
      assert op == '-'
      ans -= el
  print(ans)
