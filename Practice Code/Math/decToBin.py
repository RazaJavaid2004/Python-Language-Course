def decToBin(num):
    while num >= 1:
        bin = num % 2
        num /= 2
        print(bin)

num = int(input("Enter the Number: "))

decToBin(num)