infile = "part1.txt"

with open(infile, "r") as f:
  content = f.read()
  
  nums = content.splitlines()[:600]
  ops = content.splitlines()[600]

  nums2 = []
  for i in range(0, len(nums), 2):
    n1, n2 = int(nums[i]), int(nums[i+1])
    nums2.append(n1 * 10 + n2)

  print(nums2)
  # nums = [int(num) for num in nums]

  ops = "".join(reversed(ops))
  ans = nums2[0]
  for (el, op) in zip(nums2[1:], ops):
    if op == '+':
      ans += el
    else:
      assert op == '-'
      ans -= el
  print(ans)
