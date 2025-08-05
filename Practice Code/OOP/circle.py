class circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return (22 / 7) * self.r * self.r

    def perimeter(self):
        return 2 * (22 / 7) * self.r
    
c1 = circle(4)
print(c1.area())
print(c1.perimeter())