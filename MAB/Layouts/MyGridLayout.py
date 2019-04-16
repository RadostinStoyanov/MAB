from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# Custom Grid Layout for list of arms(labels and text fields)
class MyGridLayout(GridLayout):

    # Add N labels and text fields to the layout.
    def add_items(self, n_arms_lbl, error):

        # wrong value message
        error_message = "Please enter whole number for Number of arms," \
                        "\nNumber of experiments and Number of episodes." \
                        "\nEnter a correct digit for arm probability"

        # Check if values are digits
        if not n_arms_lbl.isdigit():

            error.text = error_message

        # Check if values are 0
        elif int(float(n_arms_lbl)) == 0:
            error.text = error_message

        else:
            error.text = ''
            # empty the layout every time it is called
            self.clear_widgets()
            # get number of arms from label
            n_arms = int(float(n_arms_lbl))

            self.size_hint_y = None
            # set big height, to be scrollable
            self.height = Window.height * int(float(n_arms_lbl)) / 12
            # set 2 columns (label | text field)
            self.cols = 2

            # add N labels and N text fields for each arm
            for i in range(1, n_arms + 1):
                # Label for each arm
                arm_lbl = Label(id='arm_lbl_' + str(i),
                                text='Arm #' + str(i),
                                keep_ratio=True,
                                size_hint_x=1,
                                size_hint_y=None,
                                font_size=50)
                # Text field for each arm
                arm_txt = TextInput(id='arm_txt_' + str(i),
                                    keep_ratio=True,
                                    allow_stretch=False,
                                    size_hint_x=1,
                                    size_hint_y=None,
                                    background_normal='res/icon_buttons/text_background.png',
                                    background_active='res/icon_buttons/text_background.png',
                                    cursor_color=(1, 140 / 255, 0, 1),
                                    foreground_color=(1, 1, 1, 1),
                                    font_size=50,
                                    multiline=False)
                # Add label to the GridLayout
                self.add_widget(arm_lbl)
                # Add label to the GridLayout
                self.add_widget(arm_txt)

