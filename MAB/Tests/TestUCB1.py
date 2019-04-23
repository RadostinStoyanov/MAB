from mabAlgorithms.UCB1 import UCB1
import unittest

class TestUCB1(unittest.TestCase):

    testUCB1 = UCB1(2)

    testUCB1.initialize()
    testUCB1.select_arm()


    def test_initialize(self):

        test_arm_times_pulled = {arm: 0 for arm in range(self.testUCB1.n_arms)}

        test_arm_summed_reward = {arm: 0.0 for arm in range(self.testUCB1.n_arms)}

        shared_arm_times_pulled = len({arm: test_arm_times_pulled[arm] for arm in test_arm_times_pulled \
                                    if arm in self.testUCB1.arm_times_pulled and\
                                    test_arm_times_pulled[arm] == self.testUCB1.arm_times_pulled[arm]})

        shared_arm_summed_reward = len({arm: test_arm_summed_reward[arm] for arm in test_arm_summed_reward \
                                    if arm in self.testUCB1.arm_summed_reward and \
                                    test_arm_summed_reward[arm] == self.testUCB1.arm_summed_reward[arm]})

        self.assertEqual(shared_arm_times_pulled, self.testUCB1.n_arms)
        self.assertEqual(shared_arm_summed_reward, self.testUCB1.n_arms)

    def test_select_arm(self):

        self.testUCB1.arm_summed_reward[0] = 10
        self.testUCB1.arm_summed_reward[1] = 20
        self.testUCB1.arm_times_pulled[0] = 4
        self.testUCB1.arm_times_pulled[1] = 2
        for arm in self.testUCB1.arm_times_pulled:

            if self.testUCB1.arm_times_pulled.get(arm) == 0:

                self.assertEqual(self.testUCB1.select_arm(), self.testUCB1.arm_times_pulled.get(arm))

            else:
                print(arm)
                self.assertEqual(self.testUCB1.select_arm(), 1)

    def test_update(self):

        selected_arm = 0
        reward = 1

        before_update_arm_pulled = self.testUCB1.arm_times_pulled.get(selected_arm)
        before_update_reward = self.testUCB1.arm_summed_reward.get(selected_arm)

        self.testUCB1.update(selected_arm, reward)

        after_update_arm_pulled = self.testUCB1.arm_times_pulled.get(selected_arm)
        after_update_reward = self.testUCB1.arm_summed_reward.get(selected_arm)

        self.assertEqual(before_update_arm_pulled+1, after_update_arm_pulled)
        self.assertEqual(before_update_reward+reward,after_update_reward)




if __name__ == "__main__":

    unittest.main()
