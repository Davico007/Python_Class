# numbers = (1,2,3)
# print(numbers[1])
#
# coordinates = (1,2,3)
# x, y, z = coordinates
# print(z)

import random


class Dice:
    def roll(self):

        outcome = (random.randint(1,6),random.randint(1,6))
        return outcome

dice = Dice()
print(dice.roll())