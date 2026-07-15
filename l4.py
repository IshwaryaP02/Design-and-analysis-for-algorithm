# Iterative Fibonacci

n = 6

a = 0
b = 1

print("Iterative Fibonacci:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()


# Recursive Fibonacci

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("Recursive Fibonacci:")

for i in range(n):
    print(fibonacci(i), end=" ")