import City as city

class HammurabiGame:

    city = city.City()
    city.start()


    def main(self):
        """
            Hauptmethode, welche beim Spielstart ausgeführt wird und bis Spielende durchläuft

        """
        city_instance = city.City()

game = HammurabiGame()
game.main()