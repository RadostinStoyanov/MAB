from armDistributions.Bernoulli import Bernoulli
import numpy as np
import unittest

class TestBernoulli(unittest.TestCase):

    testArm = Bernoulli(3)

    def testPull(self):

        rand = np.random.random()

        if rand > self.testArm.probability:

            self.assertEqual(self.testArm.pull(), 0.0)

        else:

            self.assertEqual(self.testArm.pull(), 1.0)


if __name__ == "__main__":
    unittest.main()