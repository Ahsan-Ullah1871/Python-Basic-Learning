class Pointer:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
          print("draw")

    def move(self):
          print("move")


point1 = Pointer(20,10)
point1.x = 10
# point1.y = 20
point1.draw()
print(point1.x)
