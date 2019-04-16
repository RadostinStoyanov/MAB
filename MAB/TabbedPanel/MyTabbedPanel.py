import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from Environment import Environment
from armDistributions import Bernoulli
from mabAlgorithms import UCB1


# Custom TabbedPanel class
class MyTabbedPanel(TabbedPanel):

    """"
    # Override tab switching method to animate on tab switch,
    # when going through the tabs
    def switch_to(self, header):
        anim = Animation(opacity=0, d=.24, t='in_out_quad')

        def start_anim(_anim, child, in_complete, *lt):
            _anim.start(child)

        def _on_complete(*lt):
            if header.content:
                header.content.opacity = 0
                anim = Animation(opacity=1, d=.43, t='in_out_quad')
                start_anim(anim, header.content, True)
            super(MyTabbedPanel, self).switch_to(header)

        anim.bind(on_complete=_on_complete)
        if self.current_tab.content:
            start_anim(anim, self.current_tab.content, False)
        else:
            _on_complete()
    """

    # Make new Tab and represent a graph there with the results from the calculations

    def make_new_tab(self, n_arms_lbl, my_grid, horizon, n_experiments, error):
        l_arms = []

        # wrong value message
        error_message = "Please enter whole number for Number of arms," \
                        "\nNumber of experiments and Number of episodes." \
                        "\nEnter a correct digit for arm probability"

        # error message label
        error_lbl = Label(text=error_message)

        # BoxLayout foe new tab with error message
        error_box_layout = BoxLayout()

        # BoxLayout add label
        error_box_layout.add_widget(error_lbl)

        # check if values are digits
        if not n_arms_lbl.isdigit() or not horizon.text.isdigit() or not n_experiments.text.isdigit():

            error.text = error_message

            return error_box_layout

        # check if values are 0
        elif int(float(n_arms_lbl)) == 0 or int(float(horizon.text)) == 0 or int(float(n_experiments.text)) == 0:

            error.text = error_message

            return error_box_layout

        else:

            # Receives values from input, transform into lists
            # Append to list only input values from the text fields
            # For each arm check if it is a float or equal to 0
            for child in my_grid:

                l_arms.append(child.text)

            arms1 = l_arms[0::2]

            for arm in arms1:

                if not isfloat(arm):

                    error.text = error_message

                    return error_box_layout

                elif float(arm) == 0.0:

                    error.text = error_message

                    return error_box_layout

                else:

                    error.text = ''

                    l_arms = []

                    for child in my_grid:

                        # Receives values from input, transform into lists
                        l_arms.append(child.text)

                    # Append to list only input values from the text fields
                    arms1 = l_arms[0::2]

                    arms = []

                    for arm1 in arms1:

                        a = float(arm1)

                        # Append to list transformed to floats input values
                        # That is the list of arms with their probabilities
                        arms.append(a)

                    # Number of arms
                    n_arms_int = int(float(n_arms_lbl))

                    # Number of episodes per experiment
                    horizon = int(float(horizon.text))

                    # Number of experiments
                    n_experiments = int(float(n_experiments.text))

                    # Reward history experiment-averaged
                    reward_history_avg = np.zeros(horizon)

                    # History of each action
                    action_history_sum = np.zeros((horizon, horizon))

                    # Perform tests with the user input settings
                    perform_tests(n_experiments, arms, n_arms_int, horizon, reward_history_avg, action_history_sum)

                    # average
                    reward_history_avg /= np.float(n_experiments)

                    # Plot action history results
                    graph_action = plot_action_history(n_arms_int, action_history_sum, n_experiments, horizon)

                    # Clear plot. Ready for the second plot
                    plt.clf()

                    # Plot the reward history
                    graph_reward = plot_reward_history(reward_history_avg, n_experiments, horizon)

                    # BoxLayout for the tab
                    box_layout = BoxLayout(id='new_tab_content' + n_arms_lbl,
                                           orientation='horizontal',
                                           keep_ratio=True)

                    # Add first plot image to the BoxLayout
                    box_layout.add_widget(graph_action)

                    # Add second plot image to the BoxLayout
                    box_layout.add_widget(graph_reward)

                    return box_layout


# check if value is float
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def plot_reward_history(reward_history_avg, n_experiments, horizon):
    plt.plot(reward_history_avg)
    plt.xlabel("Episode number", fontsize=15)
    plt.ylabel("Rewards collected".format(n_experiments), fontsize=15)
    plt.title("Bandit reward history averaged over {} experiments".format(n_experiments), fontsize=15)
    ax = plt.gca()
    ax.set_xscale("log", nonposx='clip')
    plt.xlim([1, horizon])

    return save_img()


def plot_action_history(n_arms_int, action_history_sum, n_experiments, horizon):

    # Plot action history results
    for i in range(n_arms_int):
        action_history_sum_plot = 100 * action_history_sum[:, i] / n_experiments

        plt.plot(list(np.array(range(len(action_history_sum_plot))) + 1),
                 action_history_sum_plot,
                 linewidth=2.0,
                 label="Bandit #{}".format(i + 1))

    plt.xlabel("Episode Number", fontsize=15)
    plt.ylabel("Bandit Action Choices (%)", fontsize=15)
    plt.title("Bandit action history averaged over {} experiments".format(n_experiments), fontsize=15)

    leg = plt.legend(loc='upper left',
                     shadow=True,
                     fontsize=10)

    ax = plt.gca()
    ax.set_xscale("log", nonposx='clip')

    plt.xlim([1, horizon])
    plt.ylim([0, 100])

    for leg_obj in leg.legendHandles:
        leg_obj.set_linewidth(16.0)

    return save_img()


def save_img():
    # Format for save image
    save_format = ".png"

    # Output file name for second plot
    output_file = "img" + str(int(random.randint(1, 1001))) + save_format

    # Save image file
    plt.savefig('res/graph_images/'+output_file, box_inches="tight", transparent=True)

    # Image Widget for the second plot
    graph = Image(source='res/graph_images/'+output_file,
                  keep_ratio=True,
                  allow_stretch=True)

    return graph


# Perform tests with the user input settings
def perform_tests(n_experiments, arms, n_arms_int, horizon, reward_history_avg, action_history_sum):

    for k in range(n_experiments):

        # Initialize environment
        environment = Environment([Bernoulli(p) for p in arms])

        # Initialize policy
        policy = UCB1(n_arms_int)
        (action_history, reward_history) = environment.play(policy, horizon)

        # Sum up reward (it will be used to show average)
        reward_history_avg += reward_history

        # Sum up action history
        for j, (a) in enumerate(action_history):

            action_history_sum[j][a] += 1
