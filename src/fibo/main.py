def fib(n):
    a = [0, 1]
    if n < 0:
        raise ValueError("Argument must be positive")
    for i in range(2, n+1):
            a.append(a[i-1] + a[i-2])
    return a[n]
