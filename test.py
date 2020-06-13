class Oranges:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        self.mold = 0

    def rot(self, time, temp):
        self.mold = time * temp


fruit = Oranges(50, 'red')
fruit.rot(5, 30)

print(fruit.mold)
