
def fibonacci(fib_list):
    return fib_list + [fib_list[-1] + fib_list[-2]]

fibonacci_list = [1,1]
while len(str(fibonacci_list[-1])) < 1000:
    fibonacci_list = fibonacci(fibonacci_list)
print(len(fibonacci_list))
