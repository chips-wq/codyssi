from collections import deque, defaultdict
import heapq
import sys

infile = "example.in" if len(sys.argv) < 2 else sys.argv[1]

"""
graph[some_str] -> [l1, l2, l3]

a walk in a graph = a sequence of edges that are consecutive
(e1, e2), (e2, e3)
(you can repeat them, walk back on them etc)

a trail in a graph = a sequence where edges don't repeat themselves

a path = a sequence of edges where nodes don't repeat themselves

a cycle = a path that starts and ends at the same point.


3<-----|
|
|
BDD<-----
|       |
|       |
AIB-----|

st = [3,4,5]

"""

def process_cycle(st : list[tuple[str, int]],cost, neigh : str):
  c_node, c_cost = st.pop()

  ans = cost
  while st:
    p_node, p_cost = st.pop()

    ans += c_cost
    # print(f"{p_node} -> {c_node} for {c_cost}")

    c_node = p_node
    c_cost = p_cost
    if c_node == neigh:
      break
  print(f"{ans=}")

def dfs(node: str, old_cost : int, st: list[tuple[str, int]], graph: dict[str, list[tuple[str, int]]], color: dict[str, int]):
  color[node] = 1
  st.append((node, old_cost))
  for (neigh, cost) in graph[node]:
    if color[neigh] == 1:
      # You found a cycle (this is a back-edge)
      process_cycle(st.copy(), cost, neigh)
      continue
    dfs(neigh, cost, st, graph, color)
    
  st.pop()
  color[node] = 0
  return


INF = 10 ** 18 + 5

with open(infile, "r") as f:
  graph = defaultdict(list)

  lines = f.read().strip().splitlines()
  for line in lines:
    edge_str, cost = line.split("|")
    cost = int(cost.strip())

    fro, to = edge_str.strip().split("->")
    fro = fro.strip()
    to = to.strip()

    graph[fro].append((to, cost))

    # print(f"{fro} -> {to}")

  st = []
  color = defaultdict(int)
  dfs("STT", 0, st, graph, color)
  # assert sum(color.values()) == len(color) * 2

  # bitmask dp (kind-of, except we do it with a set)
  # Space complexity
  # O(n * 2^n * n)
  # O(n^2 * 2^n)
  # pretty decent considering the size of the graph for n = 40
  # def dp(x, U, target):
  #   # print(f"{x=}")
  #   # print(f"{target=}")
  #   # print(f"{U=}")
  #   if x == target and len(U) > 0:
  #     return 0

  #   ans = -1e9
  #   for neigh, cost in graph[x]:
  #     if neigh != target and neigh in U: continue
  #     ans = max(ans, cost + dp(neigh, U | {x}, target))
    
  #   return ans

  # nodes = list(graph.keys())
  # print(f"{len(nodes)=}")
  # print(f"{nodes=}")
  # for x in nodes:
  #   ans = dp(x, set(), x)
  #   if ans > 0:
  #     print(f"running dp for {x}, got {ans=}")

  # x = "BDD"
  # ans = dp(x, set(), x)
  # print(f"{ans=}")


"""
I can think of a way where starting from x won't give you the longest cycle

------------------------------
|                            |
|                            |
x9  ->  x ---> x1 ---> x2 --> x3

^ 




"""
