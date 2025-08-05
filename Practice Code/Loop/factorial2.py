n = int(input("Enter the Number: "))

fact = 1
i = n
while i > 0:
    fact *= i
    i -= 1

print(fact)