def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
n=5
print("Fibonacci sequence:",fib(n))
