class person:
    name = "Anonymous"
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = person()
p1.changeName("Raza")
print(p1.name)