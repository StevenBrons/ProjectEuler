MAX = 4000000  # 4 million

a = 1
b = 1
fib = 1
tot = 0

while fib <= MAX:
    a = b
    b = fib
    fib = a + b
    if fib % 2 == 0:
        tot += fib

print(tot)
