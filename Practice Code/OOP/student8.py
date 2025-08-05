class Student:
    def __init__(self, math, sci, eng):
        self.math = math
        self.science = sci
        self.english = eng

    @property
    def calcPercent(self):
        return (self.math + self.science + self.english) / 3

s1 = Student(100, 99, 98)
print(s1.math)
print(s1.science)
print(s1.english)
print(s1.calcPercent)

s1.math = 97
print(s1.math)
print(s1.calcPercent)