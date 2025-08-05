class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding a New Student")

s1 = Student("Raza", 100)
print(s1.name)
print(s1.marks)

s2 = Student("Muzzammil", 99)
print(s2.name)
print(s2.marks)