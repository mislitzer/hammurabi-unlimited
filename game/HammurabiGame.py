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
        print("play triggered")
        # self.city.process()
        # self.fill_view_output()

    def run(self):
        """
            Hauptmethode, welche beim Spielstart ausgeführt wird und bis Spielende durchläuft

        """

        self.city.start()


        while self.city.gameOver == False:
            self.city.process()

        self.tk.deiconify()
        self.tk.mainloop()

    def fill_view_output(self): 
        self.view.update_output(self.city)

game = HammurabiGame()
game.run()