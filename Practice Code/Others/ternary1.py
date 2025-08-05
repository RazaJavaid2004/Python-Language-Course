age = int(input("Enter Your Age: "))

vote = "Yes" if age >= 18 else "No"

print("Can You Vote: ", vote)

salary = int(input("Enter Your Salary: "))

tax = salary * (0.1 if salary <= 50000 else 0.2)

print("Tax: ", tax)