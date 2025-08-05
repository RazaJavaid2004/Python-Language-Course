class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        print("Name: ", name)
        print("Math: ", marks1)
        print("Science: ", marks2)
        print("English: ", marks3)
        print("Average: ", (marks1+marks2+marks3) / 3)

s1 = Student("Raza", 100, 99, 98)