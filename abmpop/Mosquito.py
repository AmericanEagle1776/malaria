import numpy as np


class Mosquito:

    def __init__(self, blood_meals=0):
        x_coordinate = np.random.randint(0, 100)
        y_coordinate = np.random.randint(0, 100)

        self.coordinate = (x_coordinate, y_coordinate)

        self.blood_meals = blood_meals

    def bite(self, mosquito):
        mosquito.blood_meals += 1

    def move(self, mosquito):
        mosquito.coordinate[0] += np.random.randint(-2, 2)  # the mosquitoes position moves by up to +- 2 in every direction
        mosquito.coordinate[1] += np.random.randint(-2, 2)

    def breed(self, mosquitoes):
        mosquitoes.append(Mosquito())

