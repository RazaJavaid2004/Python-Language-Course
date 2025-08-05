class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def getmarks(self):
        return self.marks

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        return sum / 3

s1 = Student("Raza", [100, 98, 99])

print(s1.getmarks())

print(s1.name, " has Average: ", s1.average())
