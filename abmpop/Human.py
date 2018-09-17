import numpy as np
import random


class Human:

    def __init__(self, age_in_yrs = 0, infection_status='not infected', health_status='healthy', no_of_infections=0, days_wo_infection=0):

        self.age_in_yrs = age_in_yrs

        self.infection_status = infection_status

        self.health_status = health_status

        x_coordinate = np.random.randint(0, 100)
        y_coordinate = np.random.randint(0, 100)

        self.coordinate = (x_coordinate, y_coordinate)  # place

        self.no_of_infections = no_of_infections  # no of infections lifetime total
        self.days_wo_infection = days_wo_infection  # days since last infection clearance



    def move(self):
        self.coordinate[0] += np.random.randint(-2, 2)  # the humans position moves by up to +- 2 in every direction
        self.coordinate[1] += np.random.randint(-2, 2)

    def age(self, human):
        human.age_in_yrs += 1/365
        human.days_wo_infection += 1

    def infection(self, human):

        human.no_of_infections +=1
        human.days_wo_infection = 0
        human.infection_status = 'infected'
        if human.age_in_yrs < 11:
            human.health_status = 'sick'
        elif human.no_of_infections < 4:
            human.health_status = 'sick'
        else:
            human.health_status = 'immune'




    def illness(self, human):

        if human.health_status == 'sick':
            chance = np.random.randint(0, 20)
            if chance == 1:
                human = None

