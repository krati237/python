def fibonacci(n):
    a,b=0,1
    while b<n:
        yield b
        a,b=b,a+b
data=fibonacci(100)
# print(data)
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))