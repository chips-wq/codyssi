
def is_prime(n : int):
  if n == 1: return False
  i = 2
  while i * i <= n:
    if n % i == 0: return False
    i += 1
  return True

if __name__ == "__main__":
  print(is_prime(1))
  print(is_prime(2))
  print(is_prime(3))
  print(is_prime(4))
  print(is_prime(5))
  print(is_prime(1073741823))
