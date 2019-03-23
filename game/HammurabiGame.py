import City as city

class HammurabiGame:

    def main(self):
        """
            Hauptmethode, welche beim Spielstart ausgeführt wird und bis Spielende durchläuft

        """
        city_instance = city.City()
        city_instance.start()

game = HammurabiGame()
game.main()