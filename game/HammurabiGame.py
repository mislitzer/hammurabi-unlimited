import City as city
import View as view
import GameResult as gs
import tkinter as tk
from config import GuiConstants as GUICONSTANTS


class HammurabiGame:
    def __init__(self):
        self.tk = tk.Tk()
        self.setup(False)

    def setup(self, reboot = False):
        if (reboot):
            self.tk.destroy()
            self.tk = tk.Tk()

        self.game_state = []
        self.city = city.City(self)

        self.write_game_state()

        self.tk.geometry(str(GUICONSTANTS.GAME_VIEW_WIDTH) + "x" + str(GUICONSTANTS.GAME_VIEW_HEIGHT))
        self.tk.title(GUICONSTANTS.GAME_TITLE)

        self.view = view.View(self.tk, self)
        self.fill_view_output()
        
    def start_new_game(self):
        self.setup(True)

    def write_game_state(self):
        self.game_state.append(gs.GameResult(self.city.year, self.city.population, self.city.acres, self.city.store))

    def trigger_play(self):
        if (self.city.gameOver):
            self.view.destroy_view_output_components()

            # game over state plot
            import ResultChart as rc
            rc.ResultChart(self.game_state)

        self.city.buy_or_sell = self.view.acre_amount_slider.get()
        self.city.feed = self.view.feed_people_slider.get()
        self.city.plant = self.view.store_slider.get()
        self.city.process()

        if (self.city.gameOver == False):
            self.write_game_state()
            self.fill_view_output()

        if (self.city.store < 0):
            self.city.gameOver = True

    def trigger_slider_change(self, acres):
        buy_or_sell = self.view.acre_amount_slider.get()
        feed = self.view.feed_people_slider.get()
        plant = self.view.store_slider.get()

        new_value = int(buy_or_sell) * self.city.trade_value
        new_value += feed
        new_value += plant

        self.view.update_view_bushels(self.view.view_bushels_value - new_value)

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
