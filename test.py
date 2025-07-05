''' This module is to test the fibonachi list'''
def fibonacci_list(n):
    ''' this is actual function which takes a number
    and run for loop on it to give you fib series'''
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci_list(10))
