import tkinter as tk
from panels import OutputPanel as op
from config import GuiConstants as GUICONSTANTS


class View():
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller

        self.output_panel = op.OutputPanel(self.master)

        self.acre_amount_label = None
        self.acre_amount_slider = None
        self.feed_people_label = None
        self.feed_people_slider = None
        self.store_label = None
        self.store_slider = None
        self.view_bushels_label = None
        self.play_btn = None

        self.additional_output = []
        self.view_bushels_value = 0

        self.create_gui_elements()

    def create_gui_elements(self):
        self.acre_amount_label = tk.Label(self.master, text=GUICONSTANTS.GAME_LABEL_ACRES)
        self.acre_amount_label.pack()
        self.acre_amount_slider = tk.Scale(self.master, from_=-100, to=100, orient="horizontal", command=self.controller.trigger_slider_change)
        self.acre_amount_slider.pack()

        self.feed_people_label = tk.Label(self.master, text=GUICONSTANTS.GAME_LABEL_FEED_PEOPLE)
        self.feed_people_label.pack()
        self.feed_people_slider = tk.Scale(self.master, from_=0, to=2000, orient="horizontal", command=self.controller.trigger_slider_change)
        self.feed_people_slider.pack()

        self.store_label = tk.Label(self.master, text=GUICONSTANTS.GAME_LABEL_STORE)
        self.store_label.pack()
        self.store_slider = tk.Scale(self.master, from_=0, to=100, orient="horizontal", command=self.controller.trigger_slider_change)
        self.store_slider.pack()

        self.view_bushels_label = tk.Label(self.master, text=str(self.view_bushels_value) + GUICONSTANTS.GAME_LABEL_VIEW_BUSHELS, fg="green")
        self.view_bushels_label.pack()

        self.play_btn = tk.Button(self.master, text="Play", command = self.controller.trigger_play)
        self.play_btn.pack()

    def update_view_bushels(self, value):
        self.view_bushels_value = value
        self.view_bushels_label.config(text=str(self.view_bushels_value) + GUICONSTANTS.GAME_LABEL_VIEW_BUSHELS)

    def update_output(self, model):
        self.output_panel.clear_additional_labels()

        self.update_view_bushels(model.store)
        self.output_panel.year.config(text=GUICONSTANTS.GAME_YEAR + str(model.year))
        self.output_panel.population.config(text=GUICONSTANTS.GAME_POPULATION + str(model.population))
        self.output_panel.acres.config(text=GUICONSTANTS.GAME_ACRES + str(model.acres))
        self.output_panel.store.config(text=GUICONSTANTS.GAME_BUSHELS_IN_STORE + str(model.store))
        self.output_panel.trade_value.config(text=GUICONSTANTS.GAME_TRADE_VALUE + str(model.trade_value))

        for output in self.additional_output:
            self.output_panel.add_additional_label(output)

        