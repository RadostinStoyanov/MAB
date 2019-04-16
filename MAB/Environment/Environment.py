import numpy as np


# Environment Class
class Environment:

    def __init__(self, arms):
        self.arms = arms
        self.n_arms = len(arms)

    # Make the test with the settings
    def play(self, policy, horizon):
        # empty list for history of selected arms
        action_history = []
        # empty list for history of rewards
        reward_history = []

        # initialize
        policy.initialize()

        # for the number of times selected by the user
        for t in range(horizon):
            # select arm with the algorithm
            selected_arm = policy.select_arm()
            # get reward
            reward = self.arms[selected_arm].pull()
            # update results in lists
            policy.update(selected_arm, reward)
            # add selected arm to the list of actions
            action_history.append(selected_arm)
            # add reward to the list
            reward_history.append(reward)

        return np.array(action_history), np.array(reward_history)




