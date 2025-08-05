class person:
    name = "Anonymus"

class changeName(person):
    def __init__(self, name):
        self.__class__.name = name

p1 = changeName("Raza")

print(p1.name)
print(person.name)