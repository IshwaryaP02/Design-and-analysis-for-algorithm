# Iterative Power

x = 2
n = 10

result = 1

for i in range(n):
    result *= x

print("Iterative Power =", result)


# Recursive Fast Power

def power(x, n):

    if n == 0:
        return 1

    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half

    else:
        return x * power(x, n - 1)


print("Recursive Fast Power =", power(x, n))