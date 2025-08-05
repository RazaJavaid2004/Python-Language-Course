class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showComplex(self):
        print(self.real, " + ", self.img, "i")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal, newImg)

c1 = complex(3, 5)
c1.showComplex()

c2 = complex(4, 3)
c2.showComplex()

res = c1 + c2
res.showComplex()

res = c1 - c2
res.showComplex()