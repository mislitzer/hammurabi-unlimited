import City as city
import View as view
import tkinter as tk
from config import GuiConstants as GUICONSTANTS

class HammurabiGame:

    def __init__(self):
        self.tk = tk.Tk()
        self.city = city.City()
        self.setUp()
        self.view = view.View(self.tk, self)

        self.fill_view_output()

    def setUp(self):
        self.tk.geometry(str(GUICONSTANTS.GAME_VIEW_WIDTH) + "x" + str(GUICONSTANTS.GAME_VIEW_HEIGHT))
        self.tk.title(GUICONSTANTS.GAME_TITLE)

    def trigger_play(self):
        self.city.buy_or_sell = self.view.acre_amount_slider.get()
        self.city.feed = self.view.feed_people_slider.get()
        self.city.plant = self.view.store_slider.get()
        self.city.process()

        self.fill_view_output()

    def trigger_slider_change(self, acres):
        buy_or_sell = self.view.acre_amount_slider.get()
        feed = self.view.feed_people_slider.get()
        plant = self.view.store_slider.get()

        print(buy_or_sell)
        print(feed)
        print(plant)

        new_value = self.view.view_bushels_value - (int(acres) * self.city.trade_value)
        self.view.update_view_bushels(new_value)

    def run(self):
        """
            Hauptmethode, welche beim Spielstart ausgeführt wird und bis Spielende durchläuft

        """

        self.tk.deiconify()
        self.tk.mainloop()

    def fill_view_output(self): 
        self.view.update_output(self.city)
        self.view.additional_output = self.city.output

game = HammurabiGame()
game.run()