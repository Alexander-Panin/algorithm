def power(x, n, op):
    if (n == 0): return identity_elem(op)
    while (n & 1) == 0:
        n >>= 1
        x = op(x, x)
    result = x
    n >>= 1
    while n != 0:
        x = op(x, x)
        if (n & 1) != 0: result = op(result, x)
        n >>= 1
    return result

def func(x,y):
    return [ (x[0] * y[0] + x[1] * y[2]), (x[0] * y[1] + x[1] * y[3]),
             (x[2] * y[0] + x[3] * y[2]), (x[2] * y[1] + x[3] * y[3])]

def fib_power(n):
    if n == 0: return 0
    else: return power([1,1,1,0], n-1, func)[0]

def fib(n):
    if n >= 0: return fib_power(n)
    if n & 1: return fib_power(-n)
    return -fib_power(-n)

def solution(n):
    return fib(n)

print fib(36), '=', 930352
print fib(8), '=', 21
