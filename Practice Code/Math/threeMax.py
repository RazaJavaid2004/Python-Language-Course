a = int(input("Enter First Integer: "))
b = int(input("Enter Second Integer: "))
c = int(input("Enter Third Integer: "))

if a > b and a > c:
    print(a, " is Maximum")
elif b > a and b > c:
    print(b, " is Maximum")
else:
    print(c, " is Maximum")