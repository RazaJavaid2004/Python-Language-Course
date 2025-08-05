class person:
    name = "Anonymous"

class changeName(person):
    def __init__(self, name):
        self.name = name

p1 = changeName("Raza")

print(p1.name)
print(person.name)