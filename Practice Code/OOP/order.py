class order:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = order("Tea", 30)
ord2 = order("Biscuit", 20)

print(ord1 > ord2)