# Variables and binding names to variables

```
--------------------------
|
|   Stack
|     |
|     | x,y -> references (pointers) to the string "something"
|
|
|
|     |
|     |  <- "something"
|    Heap
|
|   .bss(data initialized to 0)
| other_data (initialized to something else)
|   .text <- Python Interpreter Compiled Code
---------------------------------------------------|
```

**In Python**, every single object is heap-allocated.

```python
x = "something"
y = "something"

print(id(x))
print(id(y))
```

```
--------------------------
|     |  <- 1, 2, 3, ... 256
|     |                                                  <- lower memory addresses
|   Stack
|     |
|     | x (address pointing to 1)
|
|
|     |
|     |
|    Heap
|
|   .bss(data initialized to 0)
| other_data (initialized to something else)
|   .text <- Python Interpreter Compiled Code              <- higher memory addresses
---------------------------------------------------|
```

```python
x = 1
y = 1
print(id(x))
print(id(y))

x = x + 1 # Binding x to the object `2`.
```

# The Global Interpreter Lock

A single **OS Thread** can execute python bytecode at a time.

You would like to have two threads doing some computation in python.

```python
def random_computation():
  ans = 0
  for i in range(1_000_000):
    ans += i * i
  print(ans)
```

                                              <- Execute these in two different threads at the same time

```python
def random_computation():
  ans = 0
  for i in range(1_000_000):
    ans += i * i
  print(ans)
```

Every thread has it's stack frame.

create_thread_1(random_computation)
create_thread_2(random_computation)

---

| Stack1
| |
| |
|
|
|
|
| Stack2
| |
| |
|

---

## What does CPython do ?

```
pthread_mutex_lock(GIL)
[... Goes on executing python code ...]

[... use library requests for fetching something ...] <- give up the GIL


pthread_mutex_unlock(GIL)
```

# Bibliography

1. [Python 101 #3 - Memory management, Stack and Heap, Object Mutability](https://www.youtube.com/watch?v=OdQSWuG78Sk)
2. [Python **slots** and object layout explained](https://www.youtube.com/watch?v=Iwf17zsDAnY)
3. [Nina Zakharenko - Memory Management in Python - The Basics - PyCon 2016](https://www.youtube.com/watch?v=F6u5rhUQ6dU)
