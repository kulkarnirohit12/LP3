def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fib_iterative(n)



def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

n = int(input("Enter number of terms: "))
for i in range(n):
    print(fib_recursive(i), end=" ")
