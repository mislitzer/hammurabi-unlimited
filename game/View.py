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
        self.play_btn = None
        self.create_gui_elements()

    def update_bushels(self):
        pass

    def create_gui_elements(self):
        self.acre_amount_label = tk.Label(self.master, text=GUICONSTANTS.GAME_LABEL_ACRES)
        self.acre_amount_label.pack()
        self.acre_amount_slider = tk.Scale(self.master, from_=-100, to=100, orient="horizontal")
        self.acre_amount_slider.pack()

        self.feed_people_label = tk.Label(self.master, text=GUICONSTANTS.GAME_LABEL_FEED_PEOPLE)
        self.feed_people_label.pack()
        self.feed_people_slider = tk.Scale(self.master, from_=0, to=100, orient="horizontal")
        self.feed_people_slider.pack()

        self.store_label = tk.Label(self.master, text=GUICONSTANTS.GAME_LABEL_STORE)
        self.store_label.pack()
        self.store_slider = tk.Scale(self.master, from_=0, to=100, orient="horizontal")
        self.store_slider.pack()

        self.play_btn = tk.Button(self.master, text="Play", command = self.controller.trigger_play)
        self.play_btn.pack()

    def update_output(self, model):
        print("printed output", model.store)
        print("print", model.population)

        