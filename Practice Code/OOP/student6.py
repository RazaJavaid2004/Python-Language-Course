class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Raza", 138)

print(s1.name)
print(s1.roll)
print(s1)

del s1
print(s1)