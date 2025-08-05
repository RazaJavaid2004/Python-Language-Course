mylist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = int(input("Enter the Element You want to Search: "))

i = 0
for val in mylist:
    if val == x:
        print(x, "Found at index: ", i)
        break
    i += 1
else:
    print(x, "Not Found")