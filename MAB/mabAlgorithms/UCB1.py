import math

from Algorithm import Algorithm

# UCB1 policy Class
class UCB1(Algorithm):

    def __init__(self, n_arms):
        # Number of arms
        self.n_arms = n_arms
        # Number of times each arm is pulled
        self.arm_times_pulled = dict()
        # Summed reward for each arm
        self.arm_summed_reward = dict()

    def initialize(self):
        # Number of arms
        n_arms = self.n_arms
        # Initialize 0 values for the times each arm is picked up
        self.arm_times_pulled = {arm : 0 for arm in range(n_arms)}
        # 0-value means for each arm
        self.arm_summed_reward = {arm : 0.0 for arm in range(n_arms)}

        # Choose Arm
    def select_arm(self):
        # Number of arms
        n_arms = self.n_arms
        # Initialize a list with 0-values for each arm
        ucb = [0.0 for arm in range(n_arms)]

        # Explore

        # In the beginning, pull each arm once,
        # if the number of pulls for the arm is 0
        # choose that arm
        for arm in range(n_arms):
            if self.arm_times_pulled[arm] == 0:
                return arm

        # Exploit
        for arm in range(n_arms):

            # Calculate mean for each arm
            mean = self.arm_summed_reward[arm] / self.arm_times_pulled[arm]
            # Calculate values for each arm with the ucb1 algorithm
            ucb[arm] = mean + math.sqrt((2 * math.log(self.arm_times_pulled[arm])) / float(self.arm_times_pulled[arm]))

        # return the index of the arm with biggest value from the ucb algorithm
        return ucb.index(max(ucb))

    # add the new reward to the list of rewards for the chosen arm
    # and increase number of pulls for the arm
    def update(self, selected_arm, reward):
        self.arm_times_pulled[selected_arm] += 1
        self.arm_summed_reward[selected_arm] += reward



