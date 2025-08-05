class Student:
    def __init__(self, name):
        self.__name = name

    def disName(self):
        print(self.__name)

s1 = Student("Raza")

s1.disName()