from Arm import Arm
import numpy as np


# Bernoulo distribution Class
class Bernoulli(Arm):

    def __init__(self,probability):
        self.probability = probability

# Receive reward (1.0 for success, 0.0 for failure)
    def pull(self):
        rand = np.random.random()
        if rand > self.probability:
            return 0.0
        else:
            return 1.0
