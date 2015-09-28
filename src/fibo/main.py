def fibo(n):
    '''
    Returns the nth Fibonacci number
    '''
    # ensure `n` is an integer
    if not isinstance(n, int):
        raise ValueError('argument must be an integer')
    # ensure `n` is non-negative
    elif n < 0:
        raise ValueError('argument must be positive')

    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
