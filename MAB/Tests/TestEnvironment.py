from Environment.Environment import Environment
from mabAlgorithms.UCB1 import UCB1
from armDistributions.Bernoulli import Bernoulli
import numpy as np
import unittest


class TestEnvironment(unittest.TestCase):

    arm1 = Bernoulli(0.1)
    arm2 = Bernoulli(0.3)

    testEnvironment = Environment([arm1, arm2])

    def testPlay(self):
        policy = UCB1(2)
        horizon = 10

        (action_history, reward_history) = self.testEnvironment.play(policy, horizon)
        print(action_history, reward_history)
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
