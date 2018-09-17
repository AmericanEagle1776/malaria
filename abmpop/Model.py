import numpy as np
import matplotlib.pyplot as plt
from Human import Human
from Mosquito import Mosquito


class Model:

    def __init__(self, nh, nm):  # initialise the starting situation

        self.humans = []  # our humans
        self.mosquitoes = []  # our mosquitoes

        self.n_human = nh
        self.n_mosquito = nm

        for h in range(self.n_human): # TODO: initialise with an age range of humans (also mosquitoes)
            self.humans.append(Human())

        for mosquitoes in range(self.n_mosquito):
            self.mosquitoes.append(Mosquito())

    def update(self):  # new timestep
        for human in self.humans:  # human activity
            human.move()
            human.age(human)
            if human.infection_status:
                human.illness(human)

        for mosquito in self.mosquitoes:  # mosquito activity
            mosquito.move()

            for victim in self.humans:  # bite if in vicinity # TODO: only bite once per timestep should have worked
                if abs(victim.coordinate[0] - mosquito.coordinate[0]) <= 3 and abs(victim.coordinate[1] -
                                                                                   mosquito.coordinate[1]) <= 3:
                    mosquito.bite(victim)
                    #chance = np.random.randint(0, 5)
                    #if chance == 2:
                    #    victim.infection(victim)
                    break

            chance = np.random.randint(0, 10)  # for a random occurrence
            if mosquito.blood_meals == 2 and chance >= 5:  # breeds half the time it already has fed twice
                mosquito.breed(self.mosquitoes)
            elif mosquito.blood_meals >= 3:  # always breeds if it has fed 3 times
                mosquito.breed(self.mosquitoes)
            else:
                continue

    def simulate(self, time_steps=30, visualise=False):

        times = range(time_steps)
        human_population_history = []
        mosquito_population_history = []

        for x in times:
            self.update()
            human_population_history.append(self.n_human)
            mosquito_population_history.append(self.n_mosquito)

        if visualise:
            fig = plt.figure()
            
            plot1 = fig.add_subplot(211)
            plot1.plot(times, human_population_history, label='no of humans')
            plot1.legend(fontsize='small')
            plot2 = fig.add_subplot(212)
            plot2.plot(times, human_population_history, label='no of mosquitoes')
            plot2.set_xlabel('days')
            plot2.legend(fontsize='small')
            plt.show()
