# Iterative Factorial

n = 5

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Iterative Factorial =", fact)


# Recursive Factorial

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("Recursive Factorial =", factorial(n))