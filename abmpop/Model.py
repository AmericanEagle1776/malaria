import numpy as np
import matplotlib as plt
from Human import Human
from Mosquito import Mosquito


class Model:

    def __init__(self, nh, nm):  # initialise the starting situation

        self.humans = []  # our humans
        self.mosquitoes = []  # our mosquitoes

        self.n_human = nh
        self.n_mosquito = nm

        for humans in range(self.n_human): # TODO: initialise with a age range of humans (also mosquitoes)
            self.humans.append(Human())

        for mosquitoes in range(self.n_mosquito):
            self.mosquitoes.append(Mosquito())

    def update(self):  # new timestep
        for human in self.humans:  # human activity
            human.move()
            human.age()

        for mosquito in self.mosquitoes:  # mosquito activity
            mosquito.move()

            for victim in self.humans:  # bite if in vicinity # TODO: only bite once per timestep should have worked
                if abs(victim.coordinate - mosquito.coordinate) <= (3, 3):
                    mosquito.bite()
                    break

            chance = np.random.randint(0, 10)  # for a random occurrence
            if (mosquito.blood_meals == 2 and chance >= 5):  # breeds half the time it already has fed twice
                mosquito.breed(self.mosquitoes)
            elif (mosquito.blood_meals == 3):  # always bites if it has fed 3 times
                mosquito.breed(self.mosquitoes)
            else:
                continue

    def simulate(self, time_steps=1000, visualise=False):
        times = range(time_steps)
        for x in times:
            self.update()
