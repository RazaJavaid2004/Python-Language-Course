def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact *= i
    return fact

print(factorial(5))