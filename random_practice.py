import random

# for i in range(3):
#     print(random.randint(10,20))


class Dice: 
    def roll(self):
        output = (random.randint(1,10),random.randint(1,10))
        return output


dice1 = Dice()
print(dice1.roll())