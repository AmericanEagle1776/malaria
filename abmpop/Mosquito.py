import numpy as np


class Mosquito:

    def __init__(self, blood_meals=0):
        x_coordinate = np.random.randint(0, 20)
        y_coordinate = np.random.randint(0, 20)

        self.coordinate = (x_coordinate, y_coordinate)
        self.history =[]

        self.blood_meals = blood_meals

    def bite(self, victim):
        self.blood_meals += 1
        victim.infection(victim)

    def move(self):

        x_coordinate = self.coordinate[0]
        y_coordinate = self.coordinate[1]
        x_coordinate += np.random.randint(-2, 2)  # the mosquitos position moves by up to +- 2 in every direction
        y_coordinate += np.random.randint(-2, 2)
        self.update_coordinate(x_coordinate, y_coordinate)

    def update_coordinate(self, x_coordinate, y_coordinate):

        self.history.append(self.coordinate)
        self.coordinate = (x_coordinate, y_coordinate)

    def breed(self, mosquitoes):
        mosquitoes.append(Mosquito())

